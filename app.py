#!flask/bin/python
from flask import Flask
from flask import request, jsonify
from app_lib import read_users_file, read_group_file

app = Flask(__name__)


@app.route('/users', methods=['GET'])
def user_service():
    users_list = read_users_file()
    return jsonify(users_list)


@app.route('/group', methods=['GET'])
def group_service():
    group_list = read_group_file()
    return jsonify(group_list)


@app.route('/users/query', methods=['GET'])
def user_query_service():
    req_name = request.args.get('name', None)
    req_uid = request.args.get('uid', None)
    req_gid = request.args.get('gid', None)
    req_comment = request.args.get('comment', None)
    req_home = request.args.get('home', None)
    req_shell = request.args.get('shell', None)
    print req_name, req_uid, req_gid, req_comment, req_home, req_shell
    return "User Query Service"


@app.route('/groups/query', methods=['GET'])
def group_query_service():
    return "Group Query Service"


if __name__ == '__main__':
    app.run(debug=True)

