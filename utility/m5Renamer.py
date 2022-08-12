#This is script rename each file in folders/* which their digest (MD5)
#also works with a single file ;)


import hashlib
import os
import sys

#return the MD5 hexdigest of file
def doHashMD5(pathFile):
	result = hashlib.md5(pathFile.encode())

	return result.hexdigest()

#return dict with the path of each file
def scanFolder(path):
	dictFile = set()
	for root, directories, files in os.walk(path, topdown=False):
		for name in files:
			dictFile.add(str(os.path.join(root, name)))

	return dictFile

def renameFile(path,newName):
	extension = path.split(".")[1] #get the file extension
	#get the folder of the file
	pathFolder = path.split(".")[0].rsplit("/",1)[0] #split on last '/' removing the old name
	
	destination=pathFolder+"/"+newName+"."+extension
	os.rename(path,destination)



def main(path):
	if(os.path.isfile(path)):
		print("processing your file")
		renameFile(path,doHashMD5(path))
	else:
		print("processing your folder")
		for i in scanFolder(path):
			renameFile(i,doHashMD5(i))

	
	print("Done!")




path = input ("Insert the path: ")
main(path)
