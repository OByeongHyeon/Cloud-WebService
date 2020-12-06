from flask import Flask, render_template, request
import pandas as pd
import codecs

app = Flask(__name__)

@app.route('/main',methods = ['POST','GET'])
def main():
    if request.method == 'POST':
        fil = request.form

        f = pd.read_csv('해양수산부_해수욕장 개장 폐장 정보.csv', encoding = 'CP949', engine='python')

        sido = f['시도 주소'] == fil['sido']
        sigun = f['시군구 주소'] == fil['sigun']

        if fil['sido'] != "none" and fil['sigun'] != "none":
            data = f[sido & sigun][['해수욕장명','개장일','폐장일','홈페이지','연락처']]
        elif fil['sigun'] == "none":
            data = f[sido][['해수욕장명', '개장일', '폐장일', '홈페이지', '연락처']]
        else :
            data = f[sigun][['해수욕장명','개장일','폐장일','홈페이지','연락처']]

        key = data.to_dict().keys()
        v = data.to_dict().values()
        v = list(map(lambda x:list(x.values()), v))
        value=[]

        for i in range(5):
            d = {j:v[i][j] for j in range(len(v[i]))}
            value.append(d)

        result = dict(zip(key, value))

        return render_template('main.html',result = result)
    if request.method == 'GET':
        return render_template('main.html')

@app.route('/detail')
def detail():
    name = request.args.get('name')
    result = {}

    f = pd.read_csv('해양수산부_해수욕장 개장 폐장 정보.csv', encoding='CP949', engine='python')
    data = f[f['해수욕장명'] == name].to_dict()
    # data['해수욕장명']=

    # del data['연번']



    return render_template('detail.html')


if __name__ == '__main__':
    app.run(debug=True)







#
# f = open('해양수산부_해수욕장 개장 폐장 정보.csv', 'r')
# rdr = csv.reader(f)
# for line in rdr:
#     print(line)
# f.close()