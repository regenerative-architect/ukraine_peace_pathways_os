"""Compatibility source-map contract tests, including negative and backward-compatibility cases."""
import json,importlib.util,tempfile,unittest,shutil
from pathlib import Path
P=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('matrix_build',P/'build.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
class CompatibilityTests(unittest.TestCase):
 def setUp(self):
  self.t=tempfile.TemporaryDirectory();self.addCleanup(self.t.cleanup);self.root=Path(self.t.name)
  for folder in ['data','schemas']:shutil.copytree(P/folder,self.root/folder)
  for file in ['index.template.html','app.js','styles.css','sw.js']:shutil.copy2(P/file,self.root/file)
  previous=b.ROOT;b.ROOT=self.root;self.addCleanup(setattr,b,'ROOT',previous)
 def mutate(self,fn):
  f=self.root/'data/compatibility-matrix.json';x=json.loads(f.read_text());fn(x);f.write_text(json.dumps(x))
 def test_coverage_and_sources(self):
  d=b.validate();c=d['compatibility-matrix'];a=d['legal-atlas']
  self.assertEqual(len(c['mechanisms']),16);self.assertEqual(len(a['jurisdictions']),28)
  self.assertEqual(len(c['assessments']),115);self.assertEqual(16*28,448)
  self.assertIn('not-assessed',{x['id'] for x in c['statuses']})
  self.assertEqual({x['researchClass'] for x in c['assessments']},{'source-mapped-preliminary'})
 def test_bogus_mechanism_rejected(self):
  self.mutate(lambda x:x['assessments'][0].update(mechanismId='not-a-real-mechanism'))
  self.assertRaisesRegex(ValueError,'unknown mechanism',b.validate)
 def test_bogus_jurisdiction_rejected(self):
  self.mutate(lambda x:x['assessments'][0].update(jurisdictionId='zz'))
  self.assertRaisesRegex(ValueError,'unknown jurisdiction',b.validate)
 def test_wrong_source_rejected(self):
  self.mutate(lambda x:x['assessments'][0].update(sourceIds=['law-999']))
  self.assertRaisesRegex(ValueError,'unknown sourceId',b.validate)
 def test_duplicate_pair_rejected(self):
  def f(x):
   x['assessments'][1]['mechanismId']=x['assessments'][0]['mechanismId'];x['assessments'][1]['jurisdictionId']=x['assessments'][0]['jurisdictionId']
  self.mutate(f);self.assertRaisesRegex(ValueError,'duplicate jurisdiction / mechanism pair',b.validate)
 def test_approval_cannot_be_fabricated(self):
  self.mutate(lambda x:x['assessments'][0].update(status='approved'))
  self.assertRaisesRegex(ValueError,"'approved' is not one of",b.validate)
 def test_unmapped_os_ref_rejected(self):
  self.mutate(lambda x:x['mechanisms'][0].update(relatedOsIds=['arbitrary']))
  self.assertRaisesRegex(ValueError,'missing referenced OS mechanism',b.validate)
 def test_offline_build_and_reference(self):
  built,size=b.build(b.validate());self.assertLess(size,2000000)
  html=built.read_text();self.assertIn('compatibilityMatrix',html);self.assertIn('assess-local-plebiscite-ua',html)
  self.assertIn('compatibility',' '.join((P/'app.js').read_text().split()))
if __name__=='__main__':unittest.main()
