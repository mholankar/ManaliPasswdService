import pprint

DEFAULT_FILE_PATH = "/etc/"
USERS_FILE_NAME = "passwd"
GROUP_FILE_NAME = "group"

DEFAULT_USERS_FILE = DEFAULT_FILE_PATH + USERS_FILE_NAME
DEFAULT_GROUP_FILE = DEFAULT_FILE_PATH + GROUP_FILE_NAME

USERS_FILE_COLS = 7
GROUP_FILE_COLS = 4


def read_users_file(ufile_name=DEFAULT_USERS_FILE):
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


def read_group_file(gfile_name=DEFAULT_GROUP_FILE):
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

