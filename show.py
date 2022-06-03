from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/show')

def show():
  person1 = {"name": "Amy", "phone": "0922-222-444", "age": "22"}
  person2 = {"name": "JJ", "phone": "0922-222-666", "age": "28"}
  person3 = {"name": "KK", "phone": "0922-222-999", "age": "32"}
  all_person = [person1, person2, person3]
  return render_template('show.html', **locals())


if __name__ == '__main__':
  app.run()