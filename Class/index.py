import os 
import shutil

# path = 'C:/Users/vijay/OneDrive/Desktop/whitehat-jr/C99/Class/'

# print('befor coping a file')
# print(os.listdir(path))

# source = 'C:/Users/vijay/OneDrive/Desktop/whitehat-jr/C99/Class/test/test.txt'

# destination = 'C:/Users/vijay/OneDrive/Desktop/whitehat-jr/C99/Class/' 

# dest = shutil.copy(source, destination)

# print('after coping a file')
# print(os.listdir(path))


# path = 'C:/Users/vijay/OneDrive/Desktop/whitehat-jr/C99/Class/'

# print('befor moving a file')
# print(os.listdir(path))

# source = 'C:/Users/vijay/OneDrive/Desktop/whitehat-jr/C99/Class/test/test.txt'

# destination = 'C:/Users/vijay/OneDrive/Desktop/whitehat-jr/C99/Class/' 

# dest = shutil.move(source, destination)

# print('after moving a file')
# print(os.listdir(path))

#!!! perogram to organise my file

path = input('enter the path:- ')
listOfFile =os.listdir(path)

for file in listOfFile:
	name,ext= os.path.splitext(file)
	ext = ext[1:]
	if ext == ' ':
		countinue
	
	if os.path.exists(path+'/'+ext):
		shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
	else:
		os.mkdir(path+'/'+ext)
		shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
		