"""Official legal reference directory integrity and compile checks."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

REPO=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('legal_build',REPO/'build.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)

class LegalAtlasSuite(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
  self.root=Path(self.tmp.name)
  for sub in ('data','schemas'):shutil.copytree(REPO/sub,self.root/sub)
  shutil.copy2(REPO/'index.template.html',self.root/'index.template.html')
  old=b.ROOT;b.ROOT=self.root;self.addCleanup(setattr,b,'ROOT',old)
 def file(self):return self.root/'data'/'legal-atlas.json'
 def read(self):return json.loads(self.file().read_text())
 def write(self,obj):self.file().write_text(json.dumps(obj))
 def test_complete_directory_and_curated_sources(self):
  d=b.validate()['legal-atlas']
  self.assertEqual(len(d['jurisdictions']),28)
  self.assertEqual(len(d['documents']),65)
  self.assertTrue(all(x['url'].startswith('https://') for x in d['documents']))
  self.assertEqual(len({x['url'] for x in d['documents']}),65)
 def test_bogus_jurisdiction_rejected(self):
  d=self.read();d['documents'][0]['jurisdictionId']='zz';self.write(d)
  self.assertRaisesRegex(ValueError,'unknown jurisdiction',b.validate)
 def test_duplicate_record_rejected(self):
  d=self.read();d['documents'][1]['id']=d['documents'][0]['id'];self.write(d)
  self.assertRaisesRegex(ValueError,'duplicate id',b.validate)
 def test_insecure_url_rejected(self):
  d=self.read();d['documents'][0]['url']='http://example.com/law';self.write(d)
  self.assertRaises(ValueError,b.validate)
 def test_future_review_date_rejected(self):
  d=self.read();d['documents'][0]['reviewedOn']='2027-01-01';self.write(d)
  self.assertRaisesRegex(ValueError,'future review date',b.validate)
 def test_atlas_compiles_for_offline_metadata(self):
  compiled,size=b.build(b.validate());s=compiled.read_text()
  self.assertLess(size,2000000)
  self.assertIn('legalAtlas',s)
  self.assertIn('law-059',s)
  self.assertIn('Legal & documentation', (REPO/'app.js').read_text())

if __name__=='__main__':unittest.main()
