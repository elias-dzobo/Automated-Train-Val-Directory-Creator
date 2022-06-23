import os 
import imghdr 

root = '../Cocoa Price Prediction/'

def getSubDirCount(root):
    subDir = []
    for subdirs in next(os.walk(root))[1]:
        subDir.append(subdirs)
    return len(subDir)

def fileCount(directory):
    path = os.path.join(root, directory)
    count = len(os.listdir(path))
    return count 

def createTrainingDirectory():
    path = 'Training'
    completepath = os.path.join(root, path)
    os.mkdir(completepath)
    return completepath

def createValidationDirectory():
    path = 'Validation'
    completepath = os.path.join(root, completepath)
    os.mkdir(completepath)
    return completepath

def isImageFile(file):
    fileType = imghdr.what(file)
    if fileType:
        return True 
    else:
        return False

def countSubDirectories(root):
    pass 

if __name__ == '__main__':
    print(isImageFile('test.py'))
