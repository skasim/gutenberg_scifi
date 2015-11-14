import unittest

from analyze.gender import gender_ratio
from analyze.gender import word_counter
from analyze.gender import both_genders

from scraper.ingest import open_several_files

def fun(x):
    return x + 1

class TestBase(unittest.TestCase):
    
    def test_addition_plus_one(self):
        self.assertEqual(fun(3), 4)

    def setUp(self):
        print 'In setUp()'
        self.text = """<h1>She was lifting weights while he was sewing clothes. His wife noticed that \
                        her husband was talking to his grandmother's ghost who was also the princess! The priest was the prince. </h1>"""
        self.fixture = range(1, 10)
        self.files = [['https://www.gutenberg.org/files/84/84-h/84-h.htm', 'frank_text.txt'],
        ['https://www.gutenberg.org/cache/epub/42/pg42.html', 'dr_JEKYLL.txt']
        ]
        self.files = open_several_files(self.files)

    def tearDown(self):
        print 'In tearDown()'
        del self.fixture

    def test(self):
        print 'in test()'
        self.failUnlessEqual(self.fixture, range(1, 10))



class TestAnalyzeGender(TestBase):
    def test_gender_ration(self):
        ratio = gender_ratio(self.text)
        self.assertEqual(ratio, 2)
        self.assertEqual(ratio, 2.0)
        self.assertEqual(type(ratio), type(1.0) )


    def test_word_counter(self):
        count = word_counter(self.text)
        self.assertIsInstance(count, dict)
        self.assertEqual(count['was'], 5)
        self.assertEqual(len(count), 27)

    # def test_both_genders(self):
    #     pass    

class TestFixtures(TestBase):

    def test_fixture(self):
        self.fixture = range(1, 11)
        self.assertEqual(self.fixture, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


class TestOpenFiles(TestBase):

    def test_open_files(self):
        self.assertEqual(self.files, ['frank_text.txt', 'dr_JEKYLL.txt'])
        self.assertNotEqual(self.files, ['frank_text.txt', '_JEKYLL.txt'])




if __name__ == '__main__':
    print 'hello'

    print len(word_counter(text))