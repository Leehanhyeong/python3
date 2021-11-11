'''
Created on 2021. 11. 10.

@author: class02
'''
fs = open("c:/mystudy/file_write.txt", "a", encoding="utf-8")
fs.write("\n반가워요~ Python!") #파일에 내용추가
fs.close()