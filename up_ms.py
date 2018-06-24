from flask import Flask, request, render_template, jsonify
from flask_restful import Resource, Api
import MySQLdb

app = Flask(__name__)
api = Api(app)

IP = 'localhost'

def getConnection():
    connection = MySQLdb.connect(
        host = IP,
        user = 'root',
        passwd = 'j24-cb09-ygo94',
        db = 'UserMath'
    )
    return connection

@app.route('/getAll/<email>', methods=['GET'])
def getAll(email):
    query  = 'select * from User where User.email=\'{}\';'
    query = query.format(email)

    connection = getConnection()
    cursor = connection.cursor()

    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(result)

@app.route('/createUser/<email>/<pswd>', methods=['PUT'])
def createUser(email, pswd):
    query = 'insert into User(email, pswd) values (%s, %s); commit;'
    data = (email, pswd)

    connection = getConnection()
    cursor = connection.cursor()

    cursor.execute(query, data)
    result = cursor.fetchall()

    cursor.close()
    connection.close()

@app.route('/updateUser/<nemail>/<oemail>/<pswd>', methods=['POST'])
def updateUser(nemail, oemail, pswd):
    query = 'update User set email=%s, pswd=%s where email=%s; commit;'
    data = (nemail, pswd, oemail)

    connection = getConnection()
    cursor = connection.cursor()

    cursor.execute(query, data)
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(result)

@app.route('/deleteUser/<email>', methods=['DELETE'])
def deleteUser(email):
    query  = 'delete from User where email=\'{}\'; commit;'
    query = query.format(email)

    connection = getConnection()
    cursor = connection.cursor()

    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(result)

if __name__ == '__main__':
    app.run(host=IP, port=9080)