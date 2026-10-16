"""Schema, semantic integrity, compilation safety. No test writes the live repository."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

REPO=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('peace_build',REPO/'build.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)

class BuildSuite(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
  self.root=Path(self.tmp.name)
  for sub in ('data','schemas'):
   shutil.copytree(REPO/sub,self.root/sub)
  shutil.copy2(REPO/'index.template.html',self.root/'index.template.html')
  old=b.ROOT;b.ROOT=self.root;self.addCleanup(setattr,b,'ROOT',old)
 def file(self,name):return self.root/'data'/f'{name}.json'
 def read(self,name):return json.loads(self.file(name).read_text())
 def write(self,name,content):self.file(name).write_text(json.dumps(content,ensure_ascii=False))
 def test_valid_and_atomic_compile(self):
  data=b.validate();target,n=b.build(data)
  self.assertGreater(n,200000)
  self.assertIn('type="application/json" id="catalog"',target.read_text())
  self.assertNotIn('__CATALOG_JSON__',target.read_text())
  self.assertIn('app.js',target.read_text())
 def test_missing_each_required_file_fails(self):
  for name in b.CORE:
   with self.subTest(file=name):
    fn=self.file(name);fn.rename(fn.with_suffix('.bak'))
    try:self.assertRaisesRegex(ValueError,'MISSING REQUIRED FILE',b.validate)
    finally:fn.with_suffix('.bak').rename(fn)
 def test_malformed_json_fails_with_previous_index_untouched(self):
  (self.root/'index.html').write_text('CANARY')
  self.file('evidence').write_text('{invalid:}')
  self.assertRaisesRegex(ValueError,'INVALID JSON',b.validate)
  self.assertEqual((self.root/'index.html').read_text(),'CANARY')
 def test_missing_structural_field(self):
  data=self.read('solutions');del data[0]['executionSteps'];self.write('solutions',data)
  self.assertRaisesRegex(ValueError,"executionSteps",b.validate)
 def test_invalid_solution_reference(self):
  data=self.read('pathway-catalog');data['pathways'][0]['solutionIds']=['nonexistent']
  self.write('pathway-catalog',data)
  self.assertRaisesRegex(ValueError,'invalid solutionId',b.validate)
 def test_invalid_evidence_reference(self):
  data=self.read('solutions');data[-1]['references'].append('not-a-source')
  self.write('solutions',data)
  self.assertRaisesRegex(ValueError,'missing evidence id',b.validate)
 def test_invalid_guide_relation(self):
  data=self.read('guide-bank');data[0]['entityId']='imaginary-party'
  self.write('guide-bank',data)
  self.assertRaisesRegex(ValueError,'unknown entityId',b.validate)
 def test_duplicate_id_fails(self):
  data=self.read('evidence');data.append(copy.deepcopy(data[0]));self.write('evidence',data)
  self.assertRaisesRegex(ValueError,'duplicate id',b.validate)
 def test_uncertainty_not_approval(self):
  data=self.read('solutions');data[0]['status']='ACCEPTED BY ALL PARTIES'
  self.write('solutions',data)
  self.assertRaisesRegex(ValueError,'status must clearly remain hypothetical',b.validate)
 def test_script_tag_cannot_inject(self):
  data=b.validate();data['solutions'][0]['outcome']='x</script><script>alert(1)</script>'
  p,n=b.build(data)
  self.assertNotIn('x</script><script>',p.read_text())
  self.assertIn('x\\u003c/script\\u003e\\u003cscript\\u003ealert(1)',p.read_text())
 def test_invalid_metric_reference(self):
  data=self.read('pathway-catalog');data['pathways'][0]['metricIds']=['wrong_metric']
  self.write('pathway-catalog',data)
  self.assertRaisesRegex(ValueError,'unknown metric id',b.validate)

class V4IntegrityTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
  self.root=Path(self.tmp.name)
  for sub in ('data','schemas'):shutil.copytree(REPO/sub,self.root/sub)
  shutil.copy2(REPO/'index.template.html',self.root/'index.template.html')
  old=b.ROOT;b.ROOT=self.root;self.addCleanup(setattr,b,'ROOT',old)
 def data(self,name):return self.root/'data'/f'{name}.json'
 def test_dependency_cycle_fails(self):
  a=json.loads(self.data('solutions').read_text())
  x=next(item for item in a if item['id']=='incident-verification')
  x['dependencyIds']=['verified-ceasefire']
  self.data('solutions').write_text(json.dumps(a))
  self.assertRaisesRegex(ValueError,'Circular implementation dependency',b.validate)
 def test_missing_dependency_rejected(self):
  a=json.loads(self.data('solutions').read_text());a[0]['dependencyIds']=['nonexistent-mechanism']
  self.data('solutions').write_text(json.dumps(a))
  self.assertRaisesRegex(ValueError,'missing dependency',b.validate)
 def test_bogus_review_audience_rejected(self):
  a=json.loads(self.data('demilitarization').read_text());a['reviewAudiences'][0]['scenarioIds']=['nonexistent']
  self.data('demilitarization').write_text(json.dumps(a))
  self.assertRaisesRegex(ValueError,'missing scenario',b.validate)
 def test_v4_full_guide_bank_embedded(self):
  data=b.validate();path,size=b.build(data);out=path.read_text()
  self.assertIn('ukraine__confidence-dialogue',out)
  self.assertIn('demilitarization',out)
  self.assertLess(size,2_000_000)
  self.assertTrue((self.root/'build-manifest.json').exists())
 def test_manifest_contains_integrity_digests(self):
  b.build(b.validate());m=json.loads((self.root/'build-manifest.json').read_text())
  self.assertEqual(len(m['files']['index.html']),64)
  self.assertIn('meaning',m)

if __name__=='__main__':unittest.main()
