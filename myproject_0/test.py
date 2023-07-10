from flask import Flask

# Flask는 우리가 지정하지 않으면 기본적으로 app.py를 시작점으로 인식해서
# Flask 패키지에 있는 클래스를 통해 어플리케이션의 입구를 만들어줍니다.
app = Flask(__name__)

@app.route('/')
def hello():
    return f'Hello, {__name__}'

# 라우팅 주소를 만들때에는 앞에 구분자(/), 경로명 까지만 적는다.
# 그 다음에 만들어질 하위 경로도 /경로명
@app.route('/okseok')
def hello_okseok():
    return f'Hello, okseok'

@app.route('/jjangu')
def hello_jjangu():
    return f'<b>JJANGU</b>'