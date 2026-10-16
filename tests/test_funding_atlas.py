"""Funding evidence classifications and hard links should fail closed."""
import json, tempfile, shutil, unittest, importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('funding_builder',ROOT/'build.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
class FundingTests(unittest.TestCase):
 def setUp(self):
  self.t=tempfile.TemporaryDirectory();self.addCleanup(self.t.cleanup);self.root=Path(self.t.name)
  for d in ['data','schemas']:shutil.copytree(ROOT/d,self.root/d)
  shutil.copy2(ROOT/'index.template.html',self.root/'index.template.html')
  prev=mod.ROOT;mod.ROOT=self.root;self.addCleanup(setattr,mod,'ROOT',prev)
 def edit(self,fn):
  f=self.root/'data/funding-atlas.json';data=json.loads(f.read_text());fn(data);f.write_text(json.dumps(data))
 def test_coverage(self):
  d=mod.validate();f=d['funding-atlas'];self.assertEqual(len(f['profiles']),30);self.assertEqual(len(f['sources']),22);self.assertEqual(len(d['entities']),78)
  self.assertIn('potential-unverified',{x['status'] for x in f['profiles']});self.assertIn('confirmed-recurring',{x['status'] for x in f['profiles']})
  self.assertEqual(0,len({p['actorId'] for p in f['profiles']} - {a['id'] for a in d['entities']}))
 def test_unknown_source_rejected(self):
  self.edit(lambda x:x['profiles'][0].update(sourceIds=['invented']))
  self.assertRaisesRegex(ValueError,'missing funder source',mod.validate)
 def test_unknown_actor_rejected(self):
  self.edit(lambda x:x['profiles'][0].update(actorId='invented'))
  self.assertRaisesRegex(ValueError,'unknown funding actorId',mod.validate)
 def test_duplicates_rejected(self):
  self.edit(lambda x:x['profiles'].append(dict(x['profiles'][0])))
  self.assertRaisesRegex(ValueError,'duplicate id',mod.validate)
 def test_outcome_vocab_rejected(self):
  self.edit(lambda x:x['profiles'][0].update(status='approved'))
  self.assertRaisesRegex(ValueError,"'approved' is not one of|unknown funding status",mod.validate)
 def test_http_source_rejected(self):
  self.edit(lambda x:x['sources'][0].update(url='http://insecure.test'))
  self.assertRaisesRegex(ValueError,"does not match",mod.validate)
 def test_future_dated_source_rejected(self):
  self.edit(lambda x:x['sources'][0].update(date='2033-01-01'))
  self.assertRaisesRegex(ValueError,'future funding source',mod.validate)
 def test_embedded_in_offline_compilation(self):
  data=mod.validate();path,size=mod.build(data);self.assertLess(size,2000000)
  h=path.read_text();self.assertIn('fundingAtlas',h);self.assertIn('worldbank-urtf',h)
if __name__=='__main__':unittest.main()
