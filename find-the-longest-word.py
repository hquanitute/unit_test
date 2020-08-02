import unittest

def find_longest_word(word_string):  
    longest_word =  max(word_string.split(), key=len)
    return longest_word

class TestMethod(unittest.TestCase):
    def test_should_return_number(self):
        self.assertEqual(type(find_longest_word("The quick brown fox jumped over the lazy dog")) , str)
        
    def test_case1(self):
        self.assertEqual(find_longest_word("May the force be with you"), "force")

    def test_case2(self):
        self.assertEqual(find_longest_word("Google do a barrel roll"), "Google")

    def test_case3(self):
        self.assertEqual(find_longest_word("What if we try a super-long word such as otorhinolaryngology"), "otorhinolaryngology")

if __name__ == '__main__':
    unittest.main()
