from wordcloud import WordCloud, STOPWORDS
import numpy as np #for matrix used to generate word cloud
from PIL import Image #for displaying wc as image
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import json
import pandas as p   #needed to create word cloud from column with string

access_token =""#your details
access_secret = ""#your details
consumer_key = ""#your details
consumer_secret = ""#your details

#Max=200

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = API(auth, wait_on_rate_limit=True)

#data = Cursor(api.search, q='jkrowling').items(Max)
data = Cursor(api.search, q='jkrowling').items()

#data is stored in the form of a json file
hp = []
for tweet in data:
    hp.append(json.loads(json.dumps(tweet._json)))

t = p.DataFrame()
t['text'] = map(lambda tweet: tweet['text'].encode('utf-8'), hp)#removes emoticons
text = " ".join(t['text'].values.astype(str))
res = " ".join([word for word in text.split()
                        if 'http' not in word and not word.startswith('@') and word != 'RT'])


#fd=open('twitterWCtemp.txt','w')
#fd.write(res)

mask = np.array(Image.open('HogwartsMask.jpg'))
wc = WordCloud(font_path='C:\Windows\Fonts\FTLTLT.ttf',background_color='black',mask=mask, max_words=150, prefer_horizontal=0.9)
wc.generate(res)
wc.to_file('TwitterWCimage.png')
pic = wc.to_image()
pic.show()
