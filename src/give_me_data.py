# https://www.codewars.com/kata/57c5bc6ec60eb2ce67000076

def has_permission(user_info, accessing_data):

    if not user_info:
        return False
    specific_perms = []
    general_perms = []
    for  perm in user_info:
        if accessing_data in perm:
            specific_perms.append(perm)
        elif perm in ['*_allow', '*_deny']:
            general_perms.append(perm)

    specifics_a = [p for p in specific_perms if 'allow' in p]
    if specifics_a:
        return True
    specifics_d = [p for p in specific_perms if 'deny' in p]
    if specifics_d:
        return False

    if not general_perms:
        return True

    specifics_d = [p for p in general_perms if 'deny' in p]

    return False if specifics_d else True

