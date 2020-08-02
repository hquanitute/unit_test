import unittest

execfile('D:/KLTN/UnitTest/Python/basic/reverse-a-string.py')

class TestReverseString(unittest.TestCase):
    def test_should_return_string(self):
        self.assertEqual(type(reverseString("hello")) is str, True, "{{%<code>hello<code> should be return String%}}")
        print("{{<code>hello<code> should be return String}}")
        
    def test_case1(self):
        self.assertEqual(reverseString("hello"), "olleh","{{%<code>hello<code> should be return olleh%}}")
        print("{{<code>hello<code> should be return olleh}}")

    def test_case2(self):
        self.assertEqual(reverseString("Howdy"), "ydwoH", "{{%<code>Howdy<code> should be return ydwoH%}}")
        print("{{<code>Howdy<code> should be return ydwoH}}")

    def test_case3(self):
        self.assertEqual(reverseString("Greetings from Earth"), "htraE morf sgniteerG", "{{%<code>Greetings from Earth<code> should be return htraE morf sgniteerG%}}")
        print("{{<code>Greetings from Earth<code> should be return htraE morf sgniteerG}}")

if __name__ == '__main__':
    unittest.main()