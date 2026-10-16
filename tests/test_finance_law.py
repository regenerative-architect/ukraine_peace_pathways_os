"""Cross-layer source linking and non-authorization regressions."""
import importlib.util,json,shutil,tempfile,unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('bridgebuild',P/'build.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
class FinanceLawTests(unittest.TestCase):
 def setUp(self):
  self.t=tempfile.TemporaryDirectory();self.addCleanup(self.t.cleanup);self.root=Path(self.t.name)
  for folder in ('data','schemas'):shutil.copytree(P/folder,self.root/folder)
  shutil.copy2(P/'index.template.html',self.root/'index.template.html')
  old=b.ROOT;b.ROOT=self.root;self.addCleanup(setattr,b,'ROOT',old)
 def change(self,fn):
  p=self.root/'data/finance-law-bridge.json';d=json.loads(p.read_text());fn(d);p.write_text(json.dumps(d))
 def test_full_actor_linkage_and_offline_payload(self):
  data=b.validate();d=data['finance-law-bridge'];self.assertEqual(len(d['links']),60)
  self.assertEqual({x['fundingProfileId'] for x in d['links']},{x['id'] for x in data['funding-atlas']['profiles']})
  self.assertEqual(set(x['assessment'] for x in d['links']),{'research-only-unassessed'})
  built,size=b.build(data);self.assertLess(size,2000000);self.assertIn('financeLawBridge',built.read_text())
 def test_unknown_financing_id_rejected(self):
  self.change(lambda d:d['links'][0].update(fundingProfileId='ghost'))
  self.assertRaisesRegex(ValueError,'missing source funding record',b.validate)
 def test_unknown_alternative_rejected(self):
  self.change(lambda d:d['links'][0].update(regenerativeAlternativeId='ghost'))
  self.assertRaisesRegex(ValueError,'missing regenerative alternative',b.validate)
 def test_missing_jurisdiction_rejected(self):
  self.change(lambda d:d['links'][0].update(jurisdictionIds=['ru','nowhere']))
  self.assertRaisesRegex(ValueError,'unknown jurisdiction',b.validate)
 def test_false_approved_classification_rejected(self):
  self.change(lambda d:d['links'][0].update(assessment='approved'))
  self.assertRaises(ValueError,b.validate)
 def test_false_top_level_permission_field_rejected(self):
  self.change(lambda d:d['links'][0].update(authorized=True))
  self.assertRaises(ValueError,b.validate)
 def test_mode_mismatch_rejected(self):
  self.change(lambda d:d['links'][0].update(cooperationMode='parallel-now'))
  self.assertRaisesRegex(ValueError,'cooperation mode differs',b.validate)
 def test_duplicate_mapping_rejected(self):
  def mutate(d):d['links'][1]['fundingProfileId']=d['links'][0]['fundingProfileId'];d['links'][1]['regenerativeAlternativeId']=d['links'][0]['regenerativeAlternativeId']
  self.change(mutate);self.assertRaisesRegex(ValueError,'duplicate funding/alternative mapping',b.validate)
 def test_missing_one_actor_rejected(self):
  def mutate(d):d['links']=[x for x in d['links'] if x['fundingProfileId']!='rus-budget']
  self.change(mutate);self.assertRaisesRegex(ValueError,'every source funding profile',b.validate)
 def test_future_date_rejected(self):
  self.change(lambda d:d['links'][0].update(asOf='2027-01-01'))
  self.assertRaisesRegex(ValueError,'future asOf',b.validate)
 def test_legal_sources_for_finland_india(self):
  la=b.validate()['legal-atlas'];self.assertIn('fi',{x['id'] for x in la['jurisdictions']});self.assertIn('in',{x['id'] for x in la['jurisdictions']})
  self.assertIn('https://www.finlex.fi/en/legislation',{x['url'] for x in la['documents']})
if __name__=='__main__':unittest.main()
