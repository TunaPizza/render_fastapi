from typing import Optional

from fastapi import FastAPI

import random  # randomライブラリを追加

from fastapi.responses import HTMLResponse #インポート

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]
    
    return {"result" : omikuji_list[random.randrange(10)]}

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>My HTML!</title>
        </head>
        <body>
            <h1>Look me! HTML!</h1>
            <h2>こんにちは<h2>
            <p>
            <a href="https://render-fastapi-v1h1.onrender.com/omikuji">おみくじを引きましょう！</a>
            <h3>ラインナップ</h3>
            <ol>
            <li>大吉 - 大吉！素晴らしい幸運が舞い込むでしょう。</li>
            <li>中吉 - 中吉！努力が実を結び、良い結果が待っています。</li>
            <li>小吉 - 小吉！ちょっとした幸運があなたの元にやってきます。</li>
            <li>吉 - 吉！安定した幸せな日々が続くでしょう。</li>
            <li>末吉 - 末吉！努力が実り始め、良い方向に進む時期です。</li>
            <li>凶 - 凶。悪いことが起こるかもしれませんが、気を引き締めてください。</li>
            <li>小凶 - 小凶。注意が必要な日です。慎重に行動しましょう。</li>
            <li>大凶 - 大凶。厳しい状況が訪れるかもしれませんが、乗り越えましょう。</li>
            </ol>
            </p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/present")
async def give_present(present):
    return {"response": f"サーバです。 {present}をくれてありがとう。とっても嬉しいです。"}  # f文字列というPythonの機能を使っている