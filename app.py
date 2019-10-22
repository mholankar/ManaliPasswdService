#!flask/bin/python
from flask import Flask
from flask import request, jsonify, abort
from app_lib import read_users_file, read_group_file, read_users_by_query, read_group_by_query, read_group_by_gid_list

app = Flask(__name__)


@app.route('/users', methods=['GET'])
def user_service():
    users_list = read_users_file()
    return jsonify(users_list)


@app.route('/users/<req_uid>', methods=['GET'])
def user_service_for_uid(req_uid):
    users_list = read_users_by_query(req_uid=req_uid)
    if not users_list:
        abort(404)
    return jsonify(users_list)


@app.route('/users/<req_uid>/groups', methods=['GET'])
def group_service_for_user(req_uid):
    users_list = read_users_by_query(req_uid=req_uid)
    gids = {}
    for each_user in users_list:
        gids.add(each_user['gid'])
    group_list = read_group_by_gid_list(list(gids))
    return jsonify(group_list)


@app.route('/group', methods=['GET'])
def group_service():
    group_list = read_group_file()
    return jsonify(group_list)


@app.route('/group/<req_gid>', methods=['GET'])
def group_service_for_gid(req_gid):
    group_list = read_group_by_query(req_gid=req_gid)
    if not group_list:
        abort(404)
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
    users_list = read_users_by_query(req_name, req_uid, req_gid, req_comment, req_home, req_shell)
    return jsonify(users_list)


@app.route('/groups/query', methods=['GET'])
def group_query_service():
    req_name = request.args.get('name', None)
    req_gid = request.args.get('gid', None)
    req_members = request.args.getlist('member', [])
    group_list = read_group_by_query(req_name, req_gid, req_members)
    return jsonify(group_list)


if __name__ == '__main__':
    app.run(debug=True)
