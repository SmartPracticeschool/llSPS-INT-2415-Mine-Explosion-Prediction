import numpy as np
import os
from sklearn.externals import joblib

from flask import Flask, request, render_template
#from werkzeug.util import secure_filename
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

'''
@app.route('flash/<messaage>')
def flash(message):
    message="NO Blast"
    return render_template("index.html", msg=message)
'''

@app.route('/predict', methods = ['POST', 'GET'])
def worky():
    if request.method == 'POST':
        n1=request.form.get('seismic')
        n2=request.form.get('seismo')
        n3=request.form.get('shift')
        n4=request.form.get('gnrg')
        n5=request.form.get('gplus')
        n6=request.form.get('gdnrg')
        n7=request.form.get('gdpluse')
        n8=request.form.get('ghaz')
        n9=request.form.get('nb')
        n10=request.form.get('nb2')
        n11=request.form.get('nb3')
        n12=request.form.get('nb4')
        n13=request.form.get('nb5')
        n14=request.form.get('nb6')
        n15=request.form.get('nb7')
        n16=request.form.get('nb89')
        n17=request.form.get('eng')
        n18=request.form.get('maxeng')

        if(n2 == "0"):
            b1,b2,b3=1,0,0
        elif(n2 == "1"):
            b1,b2,b3=0,1,0
        else:
            b1,b2,b3=0,0,1

        if(n8 == "0"):
            c1,c2,c3=1,0,0
        elif(n8 == "1"):
            c1,c2,c3=0,1,0
        else:
            c1,c2,c3=0,0,1

        n=[[b1, b2, b3, c1, c2, c3, int(n1), int(n3), int(n4), int(n5), int(n6), int(n7), int(n9), int(n10), int(n11), int(n12), int(n13), int(n14), int(n15), int(n16), int(n17), int(n18)]]

        model = joblib.load('seismic_pred.pkl')
        output = model.predict(n)

        if int(output)>=0.5:
            msg="Blast WILL occur"
        else:
            msg="Blast WILL NOT occur"

    return render_template("index.html", message="PREDICTION : "+ str(msg))

if __name__=='__main__':
    app.run(debug = True, threaded = False, host='0.0.0.0', port=6969)
