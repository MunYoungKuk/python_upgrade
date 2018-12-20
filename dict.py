import random
# winner = {
#     "김진우":22,"이승훈":22,"강승윤":21,"송민호":21
# }



# bts = {
#     "RM":20,
#     "슈가":21,
#     "진":22,
#     "제이홉":23
# }

# idol = {
#     "winner":winner,
#     "bts":bts
# }
# # print(idol)
# # print(idol["bts"]["RM"])
# score = {
#     '수학':80,
#     '영어':70,
#     '과학':90,
#     '국어':90
# }
# #for i in score는 딕셔너리에서 잘 쓰이지 않는다~
# # for key, value in score.items():
# #     print(key)
# #     print(value)
    
# # for key in score.keys():
# #     print(key)
# s = 0
# avg = 0
# for value in score.values():
#     s += value
# avg = s/len(score)
# print(avg)
    
ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gj1":  {
            "lecturer": "ChangE",
            "manager": "pro1",
            "class president": "서희수",
            "groups": {
                "두드림": ["구종민", "김녹형", "윤은솔", "이준원", "이창훈"],
                "런치타임": ["문영국", "박나원","박희승", "서희수", "황인식"],
                "Friday": ["강민지", "박현진", "서상준", "안현상", "최진호"],
                "TMM": ["김훈", "송건희", "이지선", "정태준", "조호근"],
                "살핌": ["문동식", "이중봉", "이지희", "차상권", "최보균"]
            }
        },
        "gj2": {
            "lecturer": "teacher2",
            "manager": "pro2"
        },
        "gj3": {
            "lecturer": "teacher3",
            "manager": "pro3"
        }
    }
}

#1. SSAFY를 진행하는 지역은 몇 개인 가요?
print(len(ssafy["location"]))
#2. python standard library에 'requests'가 잇나요?
a = 'requests'
if a in ssafy:
    print("requests가 존재합니다")
else:
    print("없습니다")
    
#3. gj1반의 반장의 이름을 출력하세요
print(ssafy['classes']['gj1']['class president'])

#4. ssafy에서 배우는 언어들을 출력하세요

for key in ssafy["language"].keys():
    print(key)
    
# 5. ssafy gj2의 강사와 매니저의 이름을 출력하세요
    # 예시) teacher2
    #       pro2
for value in ssafy["classes"]["gj2"].values():
    print(value)
# 6. framework들의 이름과 설명을 다음과 같이 출력하세요
    # 예시) 
    # flask는 micro이다.
    # django는 full-functioning이다.
for key, value in ssafy["language"]["python"]["frameworks"].items():
    print(key+"는 "+value+"이다")
# 7. 오늘 당번을 뽑기 위해 '살핌'조원중 1명을 랜덤으로 뽑아주세요
    # 예시)
    # 오늘 당번은 문동식입니다.

b = ssafy["classes"]["gj1"]["groups"]['살핌']
print(b)
for value in ssafy["classes"]["gj1"]["groups"]['살핌']:
        pick = random.sample(b,1)
print("오늘 당번은 ",pick,"입니다")
