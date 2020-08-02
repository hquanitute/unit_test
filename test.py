import unittest

def reverseString(str):
    return str[::-1]

class TestReverseString(unittest.TestCase):
    def test_should_return_string(self):
        self.assertEqual(type(reverseString("hello")) is str, True)
        
    def test_case1(self):
        self.assertEqual(reverseString("hello"), "olleh")

    def test_case2(self):
        self.assertEqual(reverseString("Howdy"), "ydwoH")

    def test_case3(self):
        self.assertEqual(reverseString("Greetings from Earth"), "htraE morf sgniteerG")

if __name__ == '__main__':
    unittest.main()

#   var assert = require('assert');
#   describe('<br/>reverseString<br/>', function () {
#     it('<code>reverseString("hello")</code> should return a string. <br/>', function () {
#         assert(typeof reverseString("hello") === "string");
#     });
#     it('<code>reverseString("hello")</code> should become <code>"olleh"</code>. <br/>', function () {
#         assert(reverseString("hello") === "olleh");
#     });
#     it('<code>reverseString("Howdy")</code> should become <code>"ydwoH"</code>. <br/>', function () {
#         assert(reverseString("Howdy") === "ydwoH");
#     });
#     it('<code>reverseString("Greetings from Earth")</code> should return <code>"htraE morf sgniteerG"</code>. <br/>', function () {
#         assert(reverseString("Greetings from Earth") === "htraE morf sgniteerG");
#     });
# });
