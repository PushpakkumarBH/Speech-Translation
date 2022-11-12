from flask import Flask, render_template,request
from werkzeug.utils import secure_filename
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = '/home/username/uploads'

@app.route('/upload')
def upload_file():
   return render_template('upload.html')


@app.route('/upload', methods = ['GET', 'POST'])
def upload_file1():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return '<h1>file uploaded successfully</h1>'

if __name__ == "__main__":
   app.run(debug=True)

