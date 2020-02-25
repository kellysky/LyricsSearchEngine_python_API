from flask import Flask, jsonify,request,abort
import preprocessing
import json
import from_mongo_to_json
import from_mongo
import read_meta

app = Flask(__name__)
@app.route('/api/index',methods=['POST'])
def create_list():
    dada=request.json

    print(dada)
    s = json.loads(dada)
    print(s['query'])
    #from_mongo.query_mongo(s['query'])
    list=from_mongo_to_json.get_position(s['query'])
    answer={'ans':list}
    #print(list)
    return json.dumps(answer),201

@app.route('/api/metadata',methods=['POST'])
def create_metadata():
    data=request.json
    result=read_meta.return_metadata()
    result=result.strip("[]")
    answer = {'ans': result}
    return json.dumps(answer),201




@app.route('/api/preprocess', methods=['POST'])
def create_task():
    dada=request.json
    #print(dada['query'])
    s=json.loads(dada)
    print(s)
    #if not request.json or not 'title' in request.json:
    #    abort(400) #返回404错误
    pre = preprocessing.pre(s['query'])
    answer = {'ans':pre}
    return json.dumps(answer), 201  #并且返回这个添加的task内容和状态码。

if __name__ == '__main__':
    app.run(host='127.0.0.1')
