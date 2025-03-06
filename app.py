from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/project/<string:project_name>')
def project(project_name):
   
   return render_template('project.html', project_name=project_name)

if __name__ == '__main__':
   app.run(debug = True, port=5000)