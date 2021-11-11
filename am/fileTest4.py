'''
Created on 2021. 11. 10.

@author: class02
'''
fs = open("file_write.txt", "rb")
content = fs.read() # 파일의 내용을 읽기
fs.close()
print(content) # 바이너리 형식의 데이터 출력
print("----------- 원래대로 표현하려면 decode시켜야 한다. -----------")
str = content.decode("utf-8")
print(str)