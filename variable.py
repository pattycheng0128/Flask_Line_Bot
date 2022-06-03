from flask import Flask
from flask import render_template

app = Flask(__name__) # 建立 flask 物件
@app.route('/variable')

def variable():
  student = {'學號': '875423', '姓名': '張三', '性別': '男'}
  fruit = ['apple', 'banana', 'grape', 'watermelon']
  
  return render_template('variable.html', **locals())


if __name__ == '__main__':
  app.run()