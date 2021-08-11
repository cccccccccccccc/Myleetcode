from typing import List, Sized


class File:
    isFile = True
    path = ''
    name = ''
    size = 0
    filetype = ''
class SearchCondition:
    def __init__(self,file:File):
        self.file = file
    def check (self):
        return True:
    
def getfilefrompath(path:str)->List [File]:
    return None

def searchfile(path:str,keyword:str ='')->List[File]:
    filelist = []
    curlist = getfilefrompath(path)

    for i in curlist:
        if i.isFile == True :
            if i.name.find(keyword)!=-1:
                filelist.append(i)
        else:
            filelist+=getfilefrompath(i.path)
 
    return filelist