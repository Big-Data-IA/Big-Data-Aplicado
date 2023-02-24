# -*- coding: utf-8 -*-
"""mapper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yCwGyMXJT2qt3_58aLOOiJXO0GIaPcJd
"""



import sys
import io
import re
import nltk
nltk.download('stopwords',quiet=True)
from nltk.corpus import stopwords
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

stop_words = set(stopwords.words('english'))
input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='latin1')
for line in input_stream:
  line = line.strip()
  line = re.sub(r'[^\w\s]', '',line)
  line = line.lower()
  for x in line:
    if x in punctuations:
      line=line.replace(x, " ") 

  words=line.split()
  for word in words: 
    if word not in stop_words:
      print('%s\t%s' % (word, 1))