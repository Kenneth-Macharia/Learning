from werkzeug.security import safe_str_cmp #for safely comparing string in python 2x

# ''' Managing users via data structures '''
# users = [
#     {
#         'id':1,
#         'username':'bob',
#         'password':'asdf'
#     }
# ]
#
# username_mapping = {'bob':
#     {
#         'id':1,
#         'username':'bob',
#         'password':'asdf'
#     }
# }
#
# useid_mapping = {1:
#     {
#         'id':'bob',
#         'username':'bob',
#         'password':'asdf'
#     }
# }
#
# ''' Custom methos for checking if a user exists '''
# def authenticate(username, password):
#     user = username_mapping.get(username, None)
#     if user is not None and safe_str_cmp(user.password, password):
#         return user
#
# ''' Identity method is unique to JWT '''
# def identity(payload):    # payload is the contents of the JWT token
#     user_id = payload['identity']
#     return userid_mapping.get(user_id, None)


''' Managing users via objects '''
class User(object):
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

users = [
    User(1, 'bob', 'asdf')
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

''' Custom methos for checking if a user exists '''
def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user is not None and safe_str_cmp(user.password, password):
        return user

''' Identity method is unique to JWT '''
def identity(payload):    # payload is the contents of the JWT token
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
