from flask import Flask
from flask_restful import Api
from resources.recipe import RecipeListResource, RecipeResource

app = Flask(__name__)

api = Api(app)

# 경로와 API동작코드(Resource) 를 연결한다.
api.add_resource( RecipeListResource , '/recipes')
api.add_resource( RecipeResource  , '/recipes/<int:recipe_id>') # 특정 레시피 1개 데이터 가져오는 API


if __name__ == '__main__':
    app.run()











