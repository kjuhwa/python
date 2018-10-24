import os
#파일및 디렉터리
# os.mkdir('test') #디렉터리 만들기
# os.rmdir('test') #경로 삭제
# os.remove('mathTest.py') #파일삭제
print( os.getcwd() )
print( os.listdir( r'd:\pythonTest') )
print( os.listdir( os.getcwd() )  )
print( os.path.isdir('test') )
print( os.path.isfile('sysTest.py') )
os.system('dir')
os.system('notepad')
