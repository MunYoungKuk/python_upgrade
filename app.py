from flask import Flask ,render_template, request
import random
import requests
import json
from faker import Faker

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/lotto")
def lotto():
    # 이 부분
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text
    
    lotto_dict = json.loads(res)
    
    week_format_num = []
    
    for i in range(1,7):
        num = lotto_dict["drwtNo{}".format(i)]
        week_format_num.append(num)
        
    week_num = []
    drwtNo = ['drwtNo1','drwtNo2','drwtNo3','drwtNo4','drwtNo5','drwtNo6']
    for num in drwtNo:
        number = lotto_dict[num]
        week_num.append(number)
    
    bonus = lotto_dict["bnusNo"]
    
    # print(lotto_dict["drwNoDate"])
    # print(type(res))#str
    # print(type(json.loads(res)))#dictionary
    
    
    num_list = range(1,46)
    pick = random.sample(num_list,6)
    # pick = [2,25,28,30,33,6]
    sort_pick = sorted(pick)
    cnt = 0
    bn = 0
    for j in range(6):
        for k in range(6):
            if week_num[j] == sort_pick[k]:
                cnt += 1
            elif bonus == sort_pick[k]:
                bn = 1
    
    print(bn)
    print(cnt)
    if cnt == 3: #PYTHON특징!! If문에서 조건이 겹치면 위에 있는 조건부터 실행된다.
        result = "5등"
    elif cnt == 4:
        result = "4등"
    elif cnt == 5 and bn == 1:
        result = "2등"
    elif cnt == 5:
        result = "3등"
    
    elif cnt == 6:
        result = "1등"
    else:
       result = "꽝"
    

    return render_template("lotto.html", lotto = sort_pick, week_num = week_num, week_format_num = week_format_num,result = result)#html파일을 templates에서 탐색하고 사용자에게 lotto.html 파일을 보낸다. 파이썬 함수가 아닌 Flask 함수
    
    
@app.route("/ping")
def ping():
    return render_template("ping.html")
    

@app.route("/pong")
def pong():
    input_name = request.args.get('name')
    fake = Faker('ko_kr')
    fake_job = fake.job()
    fake_email = fake.email()
    fake_text = fake.text()
    return render_template("pong.html",html_name = input_name,fake_job = fake_job,fake_email = fake_email,fake_text = fake_text)