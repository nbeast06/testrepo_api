# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 16:53:42 2021

@author: Nemesio Mangila IV
"""

from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

##dictionary
names = {"tim":{"age":19, "gender":"male"}, "bill":{"age":70,"gender":"male"}}


class HelloWorld(Resource):
   ## def get(self,name):
   ##     return{"data":"get"}
    def get(self,name,test):
        return{"name":name, "test":test}

api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")

if __name__ == "__main__":
    app.run(debug=False)

