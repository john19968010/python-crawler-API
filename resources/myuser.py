from flask import jsonify ,make_response ,request
from flask_restful import Resource, reqparse
import pymysql

parser = reqparse.RequestParser()
parser.add_argument('today')
parser.add_argument('title')
parser.add_argument('location')
parser.add_argument('start_date')
parser.add_argument('end_date')
parser.add_argument('hours')
parser.add_argument('during')
parser.add_argument('price')

class Users(Resource):
    def db_init(self):
        db = pymysql.connect(
            '127.0.0.1',
            'root',
            'root',
            'test'
        )
        cursor = db.cursor(pymysql.cursors.DictCursor)
        return db, cursor

    def get(self):
        db, cursor = self.db_init()
        sql = 'SELECT * FROM test.toodayPCCU;'
        cursor.execute(sql)
        data = cursor.fetchall()
        db.close()

        return jsonify(data)

    def post(self):
        db, cursor = self.db_init()
        arg = parser.parse_args()
        data = {

            'today': arg['today'] or '1900-01-01',
            'title': arg['title'],
            'location': arg['location'],
            'start_date': arg['start_date'],
            'end_date': arg['end_date'],
            'hours': arg['hours'],
            'during': arg['during'],
            'price': arg['price'],
            
        }

        sql = """

        INSERT INTO `test`.`toodayPCCU` (`today`,`title`,location`,`start_date`,`end_date`,`hours`,`during`,`price`) 
        VALUES ('{}','{}','{}','{}','{}','{}','{}','{}');

        """.format(data['today'],data['title'],data['location'],data['start_date'],data['end_date'],data['hours'],data['during'],data['price'])
        result = cursor.execute(sql)
        db.commit()
        db.close()

        response = {"msg": "success"}
        code = 201
        if result == 0:
            response['msg'] = 'error'
            code =400
        return make_response(jsonify(response),code)

class User(Resource):
    def db_init(self):
        db = pymysql.connect(
            '127.0.0.1',
            'root',
            'root',
            'test'
        )
        cursor = db.cursor(pymysql.cursors.DictCursor)
        return db, cursor
    
    def delete(self, id): 
        db, cursor = self.db_init() #連結資料庫初始化
        sql = 'DELETE FROM `test`.`todayPCCU` WHERE id = {};'.format(id)
        result = cursor.execute(sql)
        db.commit()
        db.close() #一定要加close不然會過大而爆掉

        #產生的status code
        response = {"msg": "success"}
        code = 201
        if result == 0:
            response['msg'] = 'error'
            code =400
        return make_response(jsonify(response),code)

    def patch(self, id):
        db, cursor = self.db_init()
        arg = parser.parse_args()
        data = {

            'today': arg['today'] or '1900-01-01',
            'title': arg['title'],
            'location': arg['location'],
            'start_date': arg['start_date'],
            'end_date': arg['end_date'],
            'hours': arg['hours'],
            'during': arg['during'],
            'price': arg['price'],
            
        }

        query = []
        for key, value in data.items():
            if value != None:
                query.append(key + " = " + " '{}' ".format(value))
        query = ",".join(query)
        
        sql = """

        UPDATE `test`.`todayPCCU` 
        SET {}
        WHERE id = {};

        """.format(query, id)
        result = cursor.execute(sql)
        db.commit() 
        db.close()

        response = {"msg": "success"}
        code = 201
        if result == 0:
            response['msg'] = 'error'
            code =400
        return make_response(jsonify(response),code)




class Loc(Resource):

    def db_init(self):
        db = pymysql.connect(
        '127.0.0.1',
        'root',
        'root',
        'test'
        )
        
        cursor = db.cursor(pymysql.cursors.DictCursor)
        return db, cursor

    def get(self, loc):
        db, cursor = self.db_init()
        sql = 'SELECT * FROM test.toodayPCCU Where location = "{}" '.format(loc)
        cursor.execute(sql)
        data = cursor.fetchall()
        db.close()

        return jsonify(data)

class Hour(Resource):

    def db_init(self):
        db = pymysql.connect(
        '127.0.0.1',
        'root',
        'root',
        'test'
        )
        
        cursor = db.cursor(pymysql.cursors.DictCursor)
        return db, cursor

    def get(self, hour):
        db, cursor = self.db_init()
        sql = 'SELECT * FROM test.toodayPCCU Where hours {} '.format(hour)
        cursor.execute(sql)
        data = cursor.fetchall()
        db.close()

        return jsonify(data)

class Hours(Resource):

    def db_init(self):
        db = pymysql.connect(
        '127.0.0.1',
        'root',
        'root',
        'test'
        )
        
        cursor = db.cursor(pymysql.cursors.DictCursor)
        return db, cursor

    def get(self, hour1, hour2):
        db, cursor = self.db_init()
        sql = 'SELECT * FROM test.toodayPCCU Where hours between {} and {}'.format(hour1 ,hour2)
        cursor.execute(sql)
        data = cursor.fetchall()
        db.close()

        return jsonify(data)

class Price(Resource):

    def db_init(self):
        db = pymysql.connect(
        '127.0.0.1',
        'root',
        'root',
        'test'
        )
        
        cursor = db.cursor(pymysql.cursors.DictCursor)
        return db, cursor

    def get(self, price):
        db, cursor = self.db_init()
        sql = 'SELECT * FROM test.toodayPCCU Where price {} '.format(price)
        cursor.execute(sql)
        data = cursor.fetchall()
        db.close()

        return jsonify(data)

class Prices(Resource):

    def db_init(self):
        db = pymysql.connect(
        '127.0.0.1',
        'root',
        'root',
        'test'
        )
        
        cursor = db.cursor(pymysql.cursors.DictCursor)
        return db, cursor

    def get(self, price1, price2):
        db, cursor = self.db_init()
        sql = 'SELECT * FROM test.toodayPCCU Where hours between {} and {}'.format(price1 ,price2)
        cursor.execute(sql)
        data = cursor.fetchall()
        db.close()

        return jsonify(data)
    