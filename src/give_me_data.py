# https://www.codewars.com/kata/57c5bc6ec60eb2ce67000076

def has_permission(user_info, accessing_data):

    last_perm = ''
    for  perm in user_info:
        if accessing_data in perm:
            last_perm = perm
        elif perm in ['*_allow', '*_deny']:
            last_perm = perm

    return True if 'allow' in last_perm else False