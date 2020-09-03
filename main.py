import flask
from flask_restful import Api, Resource
from resources.myuser import Users, Loc, Hours, Hour, Prices, Price, User

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_AS_ASCII'] = False #讓網頁能正常中文解析
api = Api(app)

api.add_resource(Users,"/all")
api.add_resource(User,"/<id>")
api.add_resource(Loc,"/loc/<loc>")
api.add_resource(Hours,"/hours/<hour1>.<hour2>")
api.add_resource(Hour,"/hour/<hour>")
api.add_resource(Prices,"/prices/<price1>.<price2>")
api.add_resource(Price,"/price/<price>")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=36)
