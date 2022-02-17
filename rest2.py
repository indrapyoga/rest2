from flask import Flask,request,jsonify
from flask_restful import Resource,Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

identitas = {}

class KResource(Resource):
    def get(self):
        response = identitas
        return jsonify(response)
    
    def post(self):
        nama = request.form["nama"]
        nim = request.form["nim"]
        identitas["nama mahasiswa"] = nama
        identitas["nim mahasiswa"] = nim
        return jsonify({"msg":"berhasil ditambah"})

api.add_resource(KResource,"/api",methods=["GET","POST"])

if __name__ == '__main__':
    app.run(debug=True,port=5011)
    