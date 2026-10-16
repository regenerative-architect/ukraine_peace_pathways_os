"""Source/data regression tests; independent approvals and funds are not inferred."""
import importlib.util,json,unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('pp_build_v41',P/'build.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
class RegenTests(unittest.TestCase):
 def setUp(self):self.payload=b.validate();self.r=self.payload['regenerative-funding']
 def test_alternative_source_and_funder_links(self):
  actors={f['id'] for f in self.r['funderKinds']};src={f['id'] for f in self.payload['evidence']}
  for i in self.r['alternatives']:
   self.assertTrue(set(i['stakeholderKinds'])<=actors)
   self.assertTrue(set(i['sourceIds'])<=src)
 def test_three_differentiated_gates(self):
  gates={x['cooperationMode'] for x in self.r['alternatives']}
  self.assertEqual(gates,{'parallel-now','reciprocal-conditional','post-agreement'})
  for o in self.r['alternatives']:
   self.assertFalse(o['cooperationMode']=='parallel-now' and o['fundingClass']=='subject-to-legal-resolution')
 def test_non_authorizing_statements(self):
  self.assertIn('Ukraine',self.r['responsibilityStatement'])
  for i in self.r['alternatives']:
   self.assertTrue(i['classification'].startswith('UNVERIFIED'))
   self.assertGreaterEqual(len(i['steps']),3)
   self.assertGreaterEqual(len(i['metrics']),3)
 def test_generated_static_offline_catalog(self):
  text=(P/'index.html').read_text()
  self.assertIn('regenerativeFunding',text)
  self.assertIn('Evidence-first reparations',text)
  self.assertIn('data/regenerative-funding.json',(P/'sw.js').read_text())
if __name__=='__main__':unittest.main()
