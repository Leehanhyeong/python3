'''
이제 매번 파일을 닫기 하는 것이 번거롭다면 
다음과 같이 with문을 이용하자!
'''
with open('file_write.txt', 'r', encoding="utf-8") as fs : # fs = open('file_write.txt','r')와 같다
    content = fs.read() #파일 내용 읽기
#with로 인해 자동으로 닫기가 이루어 지므로 닫기는 생략해도 된다.

print(content)    