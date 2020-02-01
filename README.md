# 파이썬으로 크롤링해보자

## 파이참 설치 및 개발환경 설정
디렉토리 및 파일 생성 : `static`, `templates/index.html`

1번째 `app.py`
```python
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
```

2번째 `app.py`
```python
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/about')
def about():
    return "여기는 기어바웃입니다"

if __name__ == '__main__':
    app.run()
```

## 크롤링한 데이터 html에 보여주기
`app.py`
```python
from flask import Flask, render_template
app = Flask(__name__)

#  크롤링 라이브러리 import
import requests
from bs4 import BeautifulSoup


@app.route('/')
def hello():

    req = requests.get("https://www.daum.net/")

    soup = BeautifulSoup(req.text, 'html.parser')

    # print(soup.select("#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li"))

    list_daum = []

    for i in soup.select("#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li") :
        # print(i.find("a").text)
        list_daum.append(i.find("a").text)



    return render_template("index.html", daum = list_daum)

@app.route('/about')
def about():
    return "여기는 어바웃입니다"

if __name__ == '__main__':
    app.run()
```
`templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <div>

        여기는 HTML

        <a href="/about">어바웃 페이지로 이동</a>

    </div>

    {% for i in daum %}

        {{ i }}

    {% endfor %}

    <ul>
    {% for i in daum %}

        <li>{{ i }}</li>

    {% endfor %}
    </ul>
</body>
</html>
```
