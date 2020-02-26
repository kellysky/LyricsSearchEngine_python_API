import pandas as pd
import numpy as np
import pymysql
import json

def getSimilairy(Id):
    file = "recommendation.csv"
    Id=int(Id)
    data = pd.read_csv(file, encoding='utf-8')
    tempIndex = data[data['id'] == Id].index.tolist()

    indexSimilarity = []
    if tempIndex:
        indexOfId = tempIndex[0]
        print(indexOfId)
        if indexOfId -2 < 0:
            indexSimilarity = [indexOfId+1,indexOfId+2,indexOfId+3,indexOfId+4]
        elif indexOfId+2 > len(data):
            indexSimilarity = [indexOfId-4,indexOfId-3,indexOfId-2,indexOfId-1]
        else:
            indexSimilarity = [indexOfId-2,indexOfId-1,indexOfId+1,indexOfId+2]
    res = []
    for i in range(1,201):
        res.append('vec_' + str(i))
    songLibrary = np.array(data.loc[:, res])
    songEmbedding = getSongEmbedding(Id)
    similairty = np.dot(songLibrary,songEmbedding)
    argsort_a  = np.argsort(similairty)
    if indexSimilarity:
        ans= argsort_a[::-1][:6].tolist() + indexSimilarity
        ans = list(set(ans))
    else:
        ans = argsort_a[::-1][:10].tolist()
    res = data.loc[ans,['id','singer','song_name', 'real_content']]
    ans = res[res['id'] != Id]
    return ans.to_string()


def getSongEmbedding(Id):
    con = pymysql.connect(host='8.209.74.127', port=3306, user='test', passwd='test', db='lyrics')
    cursor=con.cursor()
    sql = "SELECT * FROM SongEmbedding WHERE id = "+str(Id) 
    a_1 = pd.read_sql(sql,con)
    yy = list(a_1.iloc[0][1:])
    norm = np.linalg.norm(yy)
    con.close()
    if norm == 0:
        return []
    return yy/norm
