import unittest
from functions import *
import nltk

class TestSample(unittest.TestCase):

     def test_getNer_students_marks_courses(self):
         query_result1 = getNer("anvesh marks tir")
         result1 = {'Student': ['Anvesh'], 'attributes': ['foo:marks'], 'Faculty': [], 'Course': ['Topics In Information Retrieval']}
         query_result2 = getNer("How many marks did Anvesh and Nurendra get in Topics in IR and NLP?")
         result2 = {'Course': ['Natural Language Processing'], 'Faculty': [], 'Student': ['Nurendra', 'Anvesh'], 'attributes': ['foo:marks']}
         self.assertEqual(sorted(query_result1['Student']),sorted(result1['Student']))
         self.assertEqual(sorted(query_result2['Student']),sorted(result2['Student']))
         self.assertEqual(sorted(query_result1['attributes']),sorted(result1['attributes']))
         self.assertEqual(sorted(query_result2['attributes']),sorted(result2['attributes']))
         self.assertEqual(sorted(query_result1['Course']),sorted(result1['Course']))
         self.assertEqual(sorted(query_result2['Course']),sorted(result2['Course']))
         self.assertEqual(sorted(query_result1['Faculty']),sorted(result1['Faculty']))
         self.assertEqual(sorted(query_result2['Faculty']),sorted(result2['Faculty']))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSample)
    unittest.TextTestRunner(verbosity=2).run(suite)
