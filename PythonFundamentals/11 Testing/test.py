from tdd import analyze_text
import unittest
import os

class TestAnalysisTests(unittest.TestCase):

    def setUp(self):
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('To jest jakis tam test\n'
                    'pisania na klawiaturze\n'
                    'ktory jest kontynuwoany przez\n'
                    'kilka linii')

    def tearDown(self):
        try:
            os.remove(self.filename)
        except:
            pass

    def test_function_runs(self):
        analyze_text(self.filename)

    def test_line_count(self):
        self.assertEqual(analyze_text(self.filename)[0], 4)

    def test_character_count(self):
        self.assertEqual(analyze_text(self.filename)[1], 87)

    def test_no_such_file(self): 
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_no_deletion(self):
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))

