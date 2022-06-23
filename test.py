import unittest
from main import * 



class TestProgram(unittest.TestCase):

    def testSubDirectoryCount(self):
        self.assertEqual(getSubDirCount(root), 3, "Should be 3") 

    def testNumFilesInSubDir(self):
        self.assertEqual(fileCount('Monilia'), 211, ": 215")

    def isImage(self):
        self.assertTrue(isImageFile('test.py'), "False")

    #Test creation of train and validation

    #Test creation of subdir in these directories

    


if __name__ =='__main__':
    unittest.main()