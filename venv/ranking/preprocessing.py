#!/usr/bin/env python
# coding: utf-8

# In[1]:


from xml.dom.minidom import parse
import jieba
import pandas as pd
import nltk.stem
import jieba.posseg as pseg
#import mysql.connector
#from mysql.connector import Error

# In[2]:


def get_stopwords(filename):
    
    stopwords = []
    with open(filename, encoding="utf-8") as file:
        for f in file.readlines():
            stopwords.append(f.strip('\n').strip(' '))
    
    stopwords.append(' ')
    stopwords.append("\n")
    stopwords.append('作词')
    stopwords.append('作曲')
    
    return stopwords


# In[3]:


def pre(text):
    #print(text)
    stopwords = get_stopwords("StopWords.txt")
    stemmer = nltk.stem.SnowballStemmer("english")
    cutcorpus=pseg.cut(text)
    word_list=[]
    for i in cutcorpus:
        if i.word.lower() not in stopwords:
            word_list.append(stemmer.stem(i.word.lower()))  
    #print(word_list)
    return word_list

# def parse_xml(file_path, stopwords_file):
    
#     domTree = parse(file_path)
#     rootNode = domTree.documentElement
    
#     songs = rootNode.getElementsByTagName("song")
#     ID_list = []
#     songname_list = []
#     singer_list = []
#     lyric_list = []

#     for song in songs:
#         ID = song.getElementsByTagName('id')[0]
#         songname = song.getElementsByTagName('songname')[0]
#         singer = song.getElementsByTagName('singer')[0]
#         lyric = song.getElementsByTagName('lyric')[0]

#         if ID.childNodes==[] or songname.childNodes==[] or singer.childNodes==[] or lyric.childNodes==[]:
#             pass

#         else:
#             ID_list.append(ID.childNodes[0].data)
#             songname_list.append(songname.childNodes[0].data)
#             singer_list.append(singer.childNodes[0].data)
#             lyric_list.append(lyric.childNodes[0].data)
    
#     # turn list to dataframe
#     song_df = pd.DataFrame([ID_list, singer_list, songname_list, lyric_list]).T
#     song_df.rename(columns={0:'id', 1:'singer', 2:'song_name', 3:'content'}, inplace=True)
    
#     # preprocessing lyric
#     stopwords = get_stopwords(stopwords_file)
#     song_df['content'] = song_df['content'].apply(lambda x: pre(x, stopwords))
#     # reset id
#     song_df.id = song_df.index.values+1
    
#     return song_df


# In[5]:


# def main():
#     # df = parse_xml("musicdemo.xml", "StopWords2.txt")
#     # df.to_csv('song_df.csv', index=False, encoding="utf_8_sig")
#     return ["周杰伦","青花瓷"]


# # In[6]:


# if __name__ == '__main__':
#     main()

