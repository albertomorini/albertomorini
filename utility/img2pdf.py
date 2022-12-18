import os
from fpdf import FPDF
pdf = FPDF()

def scanFolder(path):
    dictFile = []
    for root, directories, files in os.walk(path, topdown=False):
        directories.sort()
        files.sort()
        for name in files:
            if(name!= ".DS_Store"):
                dictFile.append(str(os.path.join(root, name)))

    return dictFile


def doMerge(path, name):

    arr = scanFolder(path)
    arr.sort()
    for image in arr:
        pdf.add_page()
        pdf.image(image,0,0,210,297) #A4 size
    ## TODO: check if dir already exists
    pdf.output('./output/'+name+'.pdf','F')


path = input("Insert path: ")
name = input("Insert name of final PDF: ")

doMerge(path,name)