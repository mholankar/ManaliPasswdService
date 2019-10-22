import pprint

DEFAULT_FILE_PATH = "/etc/"
USERS_FILE_NAME = "passwd"
GROUP_FILE_NAME = "group"

DEFAULT_USERS_FILE = DEFAULT_FILE_PATH + USERS_FILE_NAME
DEFAULT_GROUP_FILE = DEFAULT_FILE_PATH + GROUP_FILE_NAME

USERS_FILE_COLS = 7
GROUP_FILE_COLS = 4

#NOTE: for now user_file_name and group_file_name can be changed
#for testing purposes
user_file_name = DEFAULT_USERS_FILE
group_file_name = DEFAULT_GROUP_FILE


def read_users_file(ufile_name=user_file_name):
    read_users = []
    with open(ufile_name) as fp:
        line = fp.readline()
        line = line.rstrip()
        while line:
            line_vals = line.split(':')
            if len(line_vals) == USERS_FILE_COLS:
                utmp = {
                    'name': line_vals[0],
                    'uid': line_vals[2],
                    'gid': line_vals[3],
                    'comment': line_vals[4],
                    'home': line_vals[5],
                    'shell': line_vals[6]
                }
                read_users.append(utmp)

            line = fp.readline()
            line = line.rstrip()

    return read_users


def read_group_file(gfile_name=group_file_name):
    read_group = []
    with open(gfile_name) as fp:
        line = fp.readline()
        line = line.rstrip()
        while line:
            line_vals = line.split(':')
            if len(line_vals) == GROUP_FILE_COLS:
                gmembers = line_vals[3].split(',') if line_vals[3] else []
                gtmp = {
                    'name': line_vals[0],
                    'gid': line_vals[2],
                    'members': gmembers
                }
                read_group.append(gtmp)

            line = fp.readline()
            line = line.rstrip()

    return read_group


def read_users_by_query(req_name=None,
                        req_uid=None,
                        req_gid=None,
                        req_comment=None,
                        req_home=None,
                        req_shell=None):

    q_users = read_users_file()
    if req_name:
        q_users = filter(lambda x: x['name'] == req_name, q_users)

    if req_uid:
        q_users = filter(lambda x: x['uid'] == req_uid, q_users)

    if req_gid:
        q_users = filter(lambda x: x['gid'] == req_gid, q_users)

    if req_comment:
        q_users = filter(lambda x: x['comment'] == req_comment, q_users)

    if req_home:
        q_users = filter(lambda x: x['home'] == req_home, q_users)

    if req_shell:
        q_users = filter(lambda x: x['shell'] == req_shell, q_users)

    return q_users


def read_group_by_query(req_name=None,
                        req_gid=None,
                        req_members=[]):

    q_grps = read_group_file()
    if req_name:
        q_grps = filter(lambda x: x['name'] == req_name, q_grps)

    if req_gid:
        q_grps = filter(lambda x: x['gid'] == req_gid, q_grps)

    if req_members:
        q_grps = filter(lambda x: set(req_members).issubset(set(x['members'])), q_grps)

    return q_grps


def read_group_by_gid_list(req_gid_list):

    q_grps = read_group_file()
    q_grps = filter(lambda x: x['gid'] in req_gid_list, q_grps)

    return q_grps