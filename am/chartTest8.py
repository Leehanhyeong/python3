'''
Created on 2021. 11. 10.

@author: class02
'''
import matplotlib.pyplot as plt

names = ["Python","Java","Spring","Flask","Vue"] #x축의 값을 의미
score = [155,301,125,107,98]#y축의 값을 의미

def korFont():
    from matplotlib import font_manager, rc
    font_name = font_manager.FontProperties(
        fname="c:/windows/fonts/HYBDAL.ttf").get_name()
    # 맥 사용자
    # font_name = font_manager.FontProperties(fname="/library/fonts/applegothic.ttf").get_name()
    rc("font", family=font_name)
    plt.rcParams["font.size"] = 13

korFont() #함수 호출!!

#plt.subplot(행의수, 열의수, 위치값)
plt.subplot(2, 1, 1) #화면은 2행 1열로 나눈 후 첫번째 위치에 챠트 지정
plt.plot(names, score, color="#f00") #챠트 지정

plt.title("2021년도 개발언어 순위")
plt.xlabel("Language")
plt.ylabel("Preference")

plt.subplot(2, 1, 2)
plt.bar(names, score, color="skyblue")

plt.show()






