'''
Created on 2021. 11. 10.

@author: class02
'''
fs = open("fileTest1.py", "r", encoding="utf-8") #파일 열기
str = fs.read()
fs.close() # 파일 닫기

print(str)
print("------ 한줄 단위로 읽기 -----------")
fs = open("fileTest1.py", "r", encoding="utf-8") #파일 열기
 # 한줄 단위로 읽기를 하지만 파일에 몇줄이 있는지 모르므로
 # 무한반복으로 처리한다.
while True:
    str = fs.readline()
    if str != '':
        print(str, end='') 
    else:
        break
fs.close()
print("------------- 끝 ---------------")    