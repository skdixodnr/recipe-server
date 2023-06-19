from flask import Flask
from flask_restful import Api
from resources.recipe import RecipeListResource, RecipeResource
from resources.user import UserLoginResource, UserRegisterResource

app = Flask(__name__)

api = Api(app)

# 경로와 API동작코드(Resource) 를 연결한다.
api.add_resource( RecipeListResource , '/recipes')
api.add_resource( RecipeResource  , '/recipes/<int:recipe_id>')
api.add_resource( UserRegisterResource , '/user/register') 
api.add_resource( UserLoginResource , '/user/login' )


if __name__ == '__main__':
    app.run()











