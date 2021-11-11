'''
Created on 2021. 11. 10.

@author: class02
'''
import matplotlib.pyplot as plt

names = ["Python","Java","Spring","Flask","Vue"] #x축의 값을 의미
score = [155,301,125,107,98]#y축의 값을 의미

plt.plot(names, score, color="#f00") #챠트 지정
plt.bar(names, score, color="skyblue")
plt.show()