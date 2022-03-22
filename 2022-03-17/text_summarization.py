#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 21:07:03 2022

@author: serynn
"""

### 텍스트 요약 프로그램

from konlpy.tag import Okt
#from collections import Counter
import matplotlib.pyplot as plt
from nltk import Text
from wordcloud import WordCloud

okt = Okt()

raw_text = input('input the text you want to summarize: ')

nouns = okt.nouns(raw_text)

text_data = Text(nouns, name='러시아-우크라이나 기사')
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