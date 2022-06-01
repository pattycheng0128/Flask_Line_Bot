from flask import Flask
# 建立 flask 物件
app = Flask(__name__)

@app.route('/')
def index():
  return '歡迎來到首頁'


@app.route('/hello')
def hello():
  return '歡迎來到 hello 頁面'

if __name__ == '__main__':
  app.run()