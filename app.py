#!/usr/local/bin/python3

from flask import Flask, render_template
from config.loadConfig import loadConfigurations

app = Flask(__name__, template_folder='templates/', static_folder='statics/')

@app.route("/")
def home():
    config = loadConfigurations()
    testConfig = config['test']['config']
    return render_template('index.html', testConfig=testConfig)

@app.route("/status")
def status():
    status='READY'
    return render_template('status.html', status=status)
  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)