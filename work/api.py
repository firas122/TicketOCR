import flask
import ocr
from flask import jsonify
from flask import Flask, render_template, request
from werkzeug import secure_filename

import json
from json import JSONEncoder

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/do', methods=['GET', 'POST'])

def home():
       #UPLOAD PICTURE AND GET PATH TO PASS IN ARGS TO
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        p = f.filename
        print(p)
        resultTraitement = ocr.traitement(p)
        result = dict(name=resultTraitement.name, total=resultTraitement.total, rest=resultTraitement.rest,
                      products=resultTraitement.tup)
        return result
        #return 'okkaay man'
    if __name__ == '__main__':
        app.run(debug=True)


app.run()
