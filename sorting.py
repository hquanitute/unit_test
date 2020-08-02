import unittest

def selection_sort(v):
    n = len(v)
    for i in range(n):
        minidx = i
        j = i + 1
        while j < n:
            if  v[j] < v[minidx] :
                v[j], v[minidx] = v[minidx], v[j]
            j += 1
    return(v)

# Example
a = [1,5,7,4,3,9,8,6,2]
b = selection_sort(a)

class TestMethod(unittest.TestCase):
    def test_should_return_list_with_same_len(self):
        self.assertEqual( len(a), len(b))
        
    def test_case1(self):
        self.assertEqual(selection_sort([1,4,2,9,4,7,5]), [1,2,4,4,5,7,9])

    def test_case2(self):
        self.assertEqual(selection_sort([10,200,4,0,-9]), [-9,0,4,10,200])

    def test_case3(self):
        self.assertEqual(selection_sort([1.5,1,0,3]), [0,1,1.5,3])

if __name__ == '__main__':
    unittest.main()
