import json


def return_metadata():
    with open('D:\Intel Idea\lyrics_demo\Index\MetaData_index1.txt', 'r', encoding='gb18030') as f:
        x = f.readlines()

    return json.dumps([a.strip("\n") for a in x])