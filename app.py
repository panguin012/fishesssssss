#Flask 클래스와 함수 둘을 가져옴
from flask import Flask, render_template, request

#Flask 어플리케이션 객체를 app에 저장
app = Flask(__name__)  #현재 실행 중인 파일의 이름

#진단용 데이터
disease = {
    "백점병": {
        "흰점": 50,
        "몸비빔": 20,
        "식욕감소": 10,
        "호흡곤란": 10 
    },

    "부레병": {
        "옆으로뜸": 50,
        "뒤집힘": 50,
        "수영이상": 30,
        "가라앉음": 20 
    },

    "부식병": {
        "지느러미손상": 50,
        "지느러미변색": 30,
        "식욕감소": 10,
        "무기력": 10 
    },

    "기적병": {
        "몸비빔": 30,
        "호흡곤란": 30,
        "무기력": 20,
        "식욕감소": 10 
    }

}

#설명용 데이터
disease_info = {

    "백점병": {
        "설명": "백점충에 의해 발생하는 대표적인 기생충 질환입니다.",
        "치료": "수온을 천천히 올리고 백점병 치료제를 사용합니다."
    },

    "부레병": {
        "설명": "부레 기능 이상으로 인해 균형을 잡지 못하는 질환입니다.",
        "치료": "절식 후 수질을 개선하고 원인 질환을 치료합니다."
    },

    "부식병": {
        "설명": "세균 감염으로 지느러미가 닳거나 찢어지는 질환입니다.",
        "치료": "수질 개선 후 항균제를 사용합니다."
    },

    "기적병": {
        "설명": "아가미에 기생충이 감염되어 호흡에 문제가 생기는 질환입니다.",
        "치료": "기생충 구제제를 사용하고 산소 공급을 늘립니다."
    }

}

@app.route('/') # 사용자가 메인 주소('/')로 접속?
def home(): # 이 home() 함수를 실행
    return render_template("index.html") # index.html 화면을 보여줘

#사용자가 주소('/result')로 접속?
@app.route('/result', methods=['POST'])
def result():
    selected = request.form.getlist("symptoms") #"symptoms"인 값을 모아 리스트로 저장
    scores = {}

    #disease 딕셔너리에서 질병 이름, 증상을 하나씩 꺼내서 반복
    for disease_name, symptoms in disease.items():
        score = 0

        for symptom in selected: #선택한 증상 하나씩 꺼내서 반복
            if symptom in symptoms: #선택한 증상이 질병의 증상에 있으면
                score += symptoms[symptom] #증상에 할당된 점수를 더해줘

        scores[disease_name] = score #질병 이름과 점수를 scores 딕셔너리에 저장

    #scores.items을 점수를 기준으로 정렬
    ranking = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True #높은 순서부터 낮은 순서로 정렬
    )

    top_disease = ranking[0][0] #점수 가장 높은 질병의 이름 저장

    #result.html에 ranking, top_disease, 설명, 치료 정보를 전달
    return render_template(
        'result.html',
        ranking=ranking,
        disease=top_disease,
        description=disease_info[top_disease]["설명"],
        treatment=disease_info[top_disease]["치료"]
    )

# 코드를 수정하고 저장하면 웹 서버가 자동으로 재시작
app.run(port=3030, debug=True) 