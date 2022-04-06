
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import pseudocode
from pyflowchart import Flowchart

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/"

@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/display', methods = ['GET', 'POST'])
def save_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        f.save(app.config['UPLOAD_FOLDER'] + filename)
        pathtostatic="C:/Users/srava/Desktop/Flask-file-upload/static"
        finalpath=pathtostatic+"/"+filename
        pseudocode.main(finalpath)
        outputfilename=filename[0:len(filename)-3] + "-Pseudocode" + ".txt"
        file = open(app.config['UPLOAD_FOLDER'] + outputfilename,"r")
        content = file.read()
        
        with open(finalpath) as f:
            code = f.read()
        fc = Flowchart.from_code(code)
        print(fc.flowchart())
    return render_template('content.html', content=content) 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)

