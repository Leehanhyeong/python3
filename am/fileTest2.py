'''
파일이 존재하지 않아도 파일이 실제로 만들어진다.
하지만 경로가 정확해야 한다.
'''
fs = open("c:/mystudy/file_write.txt", "w", encoding="utf-8") #파일열기
fs.write("안녕하세요? INCREPAS에 오신것을 환영합니다.\n12345689")#파일쓰기
fs.close()#파일닫기