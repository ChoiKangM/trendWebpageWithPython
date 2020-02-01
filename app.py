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