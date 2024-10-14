# https://www.codewars.com/kata/57c5bc6ec60eb2ce67000076

def has_permission(user_info, accessing_data):

    prority_map = {f'{accessing_data}_deny' : 1,
                   f'{accessing_data}_allow' : 2,
                   '*_deny' : 3,
                   '*_allow': 4
                   }
    if not user_info:
        return False

    specific_perms = []
    for  perm in user_info:
        if accessing_data in perm:
            specific_perms.append(perm)
        elif perm in ['*_allow', '*_deny']:
            specific_perms.append(perm)

    if not specific_perms:
        return False
    else:
        mapped_perms = [(p, prority_map.get(p, None)) for p in specific_perms]
        good = [p for p in mapped_perms if p[1] is not None]
        sorted_perms = sorted(good, key=lambda x:x[1] )
        if not sorted_perms:
            return  False
        else:
            return 'allow' in sorted_perms[0][0]




