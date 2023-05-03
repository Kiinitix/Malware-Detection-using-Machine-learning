'''
 
'''

import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle


def sanitization(web):
    web = web.lower()
    token = []
    dot_token_slash = []
    raw_slash = str(web).split('/')
    for i in raw_slash:
        raw1 = str(i).split('-')
        slash_token = []
        for j in range(0,len(raw1)):
            raw2 = str(raw1[j]).split('.')
            slash_token = slash_token + raw2
        dot_token_slash = dot_token_slash + raw1 + slash_token
    token = list(set(dot_token_slash)) 
    if 'com' in token:
        token.remove('com')
    return token

urls = []
urls.append(input("Input the URL that you want to check (eg. google.com) : "))
#print (urls)

# Using whitelist filter as the model fails in many legit cases since the biggest problem is not finding the malicious urls but to segregate the good ones
whitelist = ['hackthebox.eu','root-me.org','gmail.com']
s_url = [i for i in urls if i not in whitelist]

#Loading the model
file = "Classifier/pickel_model.pkl"
with open(file, 'rb') as f1:  
    lgr = pickle.load(f1)
f1.close()
file = "Classifier/pickel_vector.pkl"
with open(file, 'rb') as f2:  
    vectorizer = pickle.load(f2)
f2.close()

#predicting
x = vectorizer.transform(s_url)
y_predict = lgr.predict(x)

for site in whitelist:
    s_url.append(site)
#print(s_url)

predict = list(y_predict)
for j in range(0,len(whitelist)):
    predict.append('good')
print("\nThe entered domain is: ", predict[0])
print("\n\nIf you feel that this prediction is wrong, or if you are not so sure about this output\nyou can contact us at kabirdhruw@protonmail.com we'll check the URL and update the machine\naccodingly. Thank you.")

