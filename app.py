from flask import Flask
from flask_restful import Api


app = Flask(__name__)

api = Api(app)

# 경로와 API동작코드(Resource) 를 연결한다.
api.add_resource(    , '/recipes')



if __name__ == '__main__':
    app.run()











