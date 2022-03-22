#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 09:33:57 2022

@author: serynn
"""

raw_text = """러시아군이 11일(현지시간) 우크라이나 서부 도시인 루츠크와 이바노-프란키우스크 등을 공습했다고 AP통신과 BBC 등 외신들이 보도했다. 그동안 우크라이나 북쪽에 위치한 수도 키이우(키예프)와 동남부 도시들에 집중됐던 러시아군의 공격이 폴란드와 인접한 서부로까지 넓어지면서 사실상 우크라이나 전역이 러시아군의 공격 아래 놓이게 됐다.
북서부 도시 루츠크 당국에 따르면 이날 새벽 러시아군의 공습으로 우크라이나 군인 2명이 숨지고 6명이 부상을 입었다. 공습은 군사 비행장과 전투기 수리 공장을 겨냥한 것으로 보인다고 외신들은 보도했다. 남서부 도시 이바노-프란키우스크에서도 러시아군에 의한 공습이 일어나 인근 지역 주민들이 대피했다.
러시아 국방부도 두 도시를 공습한 사실을 확인했다. 이고르 코나셴코프 러시아 국방부 대변인은 이날 “오전에 고정밀, 장거리 무기가 우크라이나 군사 기반 시설을 공격했다”며 “이바노-프란키우스크와 루츠크의 군용 비행장 2곳의 가동이 중단됐다”고 밝혔다고 스푸트니크 통신이 전했다.
우크라이나 중동부의 거점 도시 드니프로도 이날 처음으로 러시아의 공격을 받았다. 드니프로 구조 당국은 성명을 내고 “이날 일찍 드니프로에 세 차례 공습이 있었다”면서 “유치원 1곳과 아파트 1개 동, 2층짜리 신발공장이 공격을 받아 1명이 숨졌다”고 발표했다.
러시아군이 우크라이나 서부와 중부의 도시들을 새로운 타깃으로 삼은 것은 전쟁이 새로운 국면을 맞았음을 시사한다. 우크라이나인들이 키이우를 ‘요새화’한 가운데 러시아의 공격 범위와 전선이 확대되면서 민간인 피해가 더욱 커질 것이라는 우려가 나온다. 러시아는 그동안 키이우와 마리우폴 등 남동부 도시들을 집중 타격해왔다. 우크라이나 인구 4400만명 중 3분의 2 가량은 도시에 거주하고 있는데, 러시아군이 민간인들이 밀집한 도시를 상대로 동시다발적 공격을 벌이고 있는 셈이다. 잉나 소브순 우크라이나 의회 의원은 트위터에 “우크라이나에 안전한 도시는 없다”며 “비행금지구역 설정이 필요하다”고 적었다.

지난 9일 남부 마리우폴 산부인과 병원을 폭격해 국제사회의 공분을 산 러시아군은 이날도 키이우 서쪽 지토미르와 동부 하르키우주 등지의 병원을 잇따라 공격했다. 올레그 시네후보프 하르키우 주지사는 러시아군이 이날 하르키우주 아이지움 마을 인근 정신병원에 포격을 가했다고 밝혔다. 시네후보프 주지사는 당시 병원에 있던 330명 중 73명만 대피했다면서 “민간인에 대한 무자비한 공격”이라고 비난했다."""

### 1. KoNLPy를 활용 (형태소/명사 단위 태깅)
from konlpy.tag import Okt

okt = Okt()

#print(okt.morphs(raw_text))
#print(okt.nouns(raw_text))

### 2. 나눈 값을 토대로 가장 많이 나온 단어들을 출력
from collections import Counter #collections -> python 내장 함수, Counter -> 숫자 count하는 함수

nouns = okt.nouns(raw_text)
count = Counter(nouns)
noun_list = count.most_common(10) #가장 많이 등장하는 단어들을 100개 이내로 리스트에 담아줌
#for noun_freq in noun_list:
#    print(noun_freq)
    
### 3. 출력말고 저장 (txt, csv)
import csv

with open("noun_list.txt","w", encoding = "utf-8") as f:
    for noun_freq in noun_list:
        f.write(" ".join(map(str,noun_freq)))
        f.write("\n")
        
with open("noun_list.csv","w", newline = "", encoding = "euc-kr") as f:
    csvwriter = csv.writer(f)
    for noun_freq in noun_list:
        csvwriter.writerow(noun_freq)
    
### 4. 저장말고 그래프 (matplotlib)
import matplotlib.pyplot as plt
from nltk import Text

from matplotlib import rc 
rc('font', family='AppleGothic') 			
plt.rcParams['axes.unicode_minus'] = False #plot에서 한글 깨짐 해결

text_data = Text(nouns, name='러시아-우크라이나 기사')
plt.figure(figsize=(15,10))
plt.title('기사에 나온 명사 빈도수')
text_data.plot(20)
plt.show()

### 5. 보기에 예쁘게 바꾸기 (wordcloud)
from wordcloud import WordCloud

font = '/System/Library/Fonts/Supplemental/AppleGothic.ttf'
wc = WordCloud(
    max_words = 100,
    font_path=font,
    min_font_size=1,
    max_font_size=50,
    relative_scaling=0.2,
    background_color='white',
)

fd = text_data.vocab()

word_cloud = wc.generate_from_frequencies(fd)

plt.figure(figsize=(15,15))
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis('off')
plt.show()  

#=============================================================================

### 전체 코드
'''
from konlpy.tag import Okt
from collections import Counter 
import csv
import matplotlib.pyplot as plt
from nltk import Text
from wordcloud import WordCloud

from matplotlib import rc 
rc('font', family='AppleGothic') 			
plt.rcParams['axes.unicode_minus'] = False

okt = Okt()
raw_text = """러시아군이 11일(현지시간) 우크라이나 서부 도시인 루츠크와 이바노-프란키우스크 등을 공습했다고 AP통신과 BBC 등 외신들이 보도했다. 그동안 우크라이나 북쪽에 위치한 수도 키이우(키예프)와 동남부 도시들에 집중됐던 러시아군의 공격이 폴란드와 인접한 서부로까지 넓어지면서 사실상 우크라이나 전역이 러시아군의 공격 아래 놓이게 됐다.
북서부 도시 루츠크 당국에 따르면 이날 새벽 러시아군의 공습으로 우크라이나 군인 2명이 숨지고 6명이 부상을 입었다. 공습은 군사 비행장과 전투기 수리 공장을 겨냥한 것으로 보인다고 외신들은 보도했다. 남서부 도시 이바노-프란키우스크에서도 러시아군에 의한 공습이 일어나 인근 지역 주민들이 대피했다.
러시아 국방부도 두 도시를 공습한 사실을 확인했다. 이고르 코나셴코프 러시아 국방부 대변인은 이날 “오전에 고정밀, 장거리 무기가 우크라이나 군사 기반 시설을 공격했다”며 “이바노-프란키우스크와 루츠크의 군용 비행장 2곳의 가동이 중단됐다”고 밝혔다고 스푸트니크 통신이 전했다.
우크라이나 중동부의 거점 도시 드니프로도 이날 처음으로 러시아의 공격을 받았다. 드니프로 구조 당국은 성명을 내고 “이날 일찍 드니프로에 세 차례 공습이 있었다”면서 “유치원 1곳과 아파트 1개 동, 2층짜리 신발공장이 공격을 받아 1명이 숨졌다”고 발표했다.
러시아군이 우크라이나 서부와 중부의 도시들을 새로운 타깃으로 삼은 것은 전쟁이 새로운 국면을 맞았음을 시사한다. 우크라이나인들이 키이우를 ‘요새화’한 가운데 러시아의 공격 범위와 전선이 확대되면서 민간인 피해가 더욱 커질 것이라는 우려가 나온다. 러시아는 그동안 키이우와 마리우폴 등 남동부 도시들을 집중 타격해왔다. 우크라이나 인구 4400만명 중 3분의 2 가량은 도시에 거주하고 있는데, 러시아군이 민간인들이 밀집한 도시를 상대로 동시다발적 공격을 벌이고 있는 셈이다. 잉나 소브순 우크라이나 의회 의원은 트위터에 “우크라이나에 안전한 도시는 없다”며 “비행금지구역 설정이 필요하다”고 적었다.

지난 9일 남부 마리우폴 산부인과 병원을 폭격해 국제사회의 공분을 산 러시아군은 이날도 키이우 서쪽 지토미르와 동부 하르키우주 등지의 병원을 잇따라 공격했다. 올레그 시네후보프 하르키우 주지사는 러시아군이 이날 하르키우주 아이지움 마을 인근 정신병원에 포격을 가했다고 밝혔다. 시네후보프 주지사는 당시 병원에 있던 330명 중 73명만 대피했다면서 “민간인에 대한 무자비한 공격”이라고 비난했다."""

#print(okt.morphs(raw_text))
#print(okt.nouns(raw_text))

nouns = okt.nouns(raw_text)
count = Counter(nouns)
noun_list = count.most_common(10)

for noun_freq in noun_list:
    print(noun_freq)

with open("noun_list.txt","w", encoding = "utf-8") as f:
    for noun_freq in noun_list:
        f.write(" ".join(map(str,noun_freq)))
        f.write("\n")
        
with open("noun_list.csv","w", newline="", encoding = "euc-kr") as f:
    csvwriter = csv.writer(f)
    for noun_freq in noun_list:
        csvwriter.writerow(noun_freq)

article = Text(nouns, name='기사')
plt.figure(figsize=(15,10))

font = '/System/Library/Fonts/Supplemental/AppleGothic.ttf'
wc = WordCloud(
    max_words = 100,
    font_path=font,
    min_font_size=1,
    max_font_size=50,
    relative_scaling=0.2,
    background_color='white',
)

fd = article.vocab()

word_cloud = wc.generate_from_frequencies(fd)

plt.figure(figsize=(15,15))
plt.imshow(word_cloud, interpolation='bilinear')
plt.axis('off')
plt.show()
'''











