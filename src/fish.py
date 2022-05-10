'''

https://app.codility.com/c/run/training7XEK8F-27D/
'''

def cross(container, size, dir, top_size, top_dir):
    if size >= top_size:
        container.pop()
        container.append((size, dir))
    else:
        # removing
        pass
    return container

def solution(A, B):
    # write your code in Python 3.6
    # https://app.codility.com/c/run/trainingUPYQM8-5MH/
    # Need two stacks, one for upstream and another for downstream
    # this is about stacks and queues
    # We can try to use a stack
    # we need to bear in mind direction

    # this might give a reference
    holder = []

    for idx, tpl in enumerate(zip(A, B)):
        size, dir = tpl
        if not holder:
            holder.append((size, dir))
        else:
            top_size, top_dir = holder[-1]
            if top_dir == 0 and dir == 1: # top is upstrea, we cannot catch it
                holder.append((size, dir))
            elif top_dir == dir:
                holder.append((size, dir))
            else:
                holder = cross(holder, size, dir, top_size, top_dir)

    return len(holder)