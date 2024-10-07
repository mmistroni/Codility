# https://www.codewars.com/kata/57c5bc6ec60eb2ce67000076

def has_permission(user_info, accessing_data):

    last_perms = []
    for  perm in user_info:
        if accessing_data in perm:
            last_perms.append(perm)
        elif perm in ['*_allow', '*_deny']:
            last_perms.append(perm)

    denies = [p for p in last_perms if 'deny' in p]
    allow = [p for p in last_perms if 'allow' in p]

    if denies:
        return False
    if allow:
        return True
    return False

    return True if 'allow' in last_perm else False