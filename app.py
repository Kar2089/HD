from flask import Flask, render_template, request, jsonify
import config
app = Flask(__name__)
@app.route('/')
def index():
    print("My tutor is Bal")
    return 'My name is Karan'
@app.route("/predict", methods = ['GET','POST'])
def fun_name():
    return jsonify(request.values()) 
if __name__=='__main__':
    print("Server Started")
    app.run(host=config.flask_host, port=config.flask_port, debug= config.flask_debug)
    print("Server Closed")
# Column 
# "Age", "Sex", "ChestPainType", "RestingBP", "Cholesterol", "FastingBS", "RestingECG", "MaxHR", "ExerciseAngina", "Oldpeak", "ST_Slope"
