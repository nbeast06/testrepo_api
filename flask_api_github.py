# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 10:29:47 2021

@author: Nemesio Mangila IV
"""
from flask import json
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome guys'

@app.route('/github', methods=['POST'])
def api_gh_message():
    if request.headers['Content-Type'] == 'application/json':
        my_info = json.dumps(request.json)
        print(my_info)
        return my_info
    
if __name__ == '__main__':
    app.run(debug=False)

