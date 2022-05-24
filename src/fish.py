'''

https://app.codility.com/c/run/training7XEK8F-27D/
'''

def cross_check(container, incoming_size, incoming_dir):
    top_size, top_dir = container[-1]
    if top_dir == 1 and incoming_dir == 0:
        #the two cross
        if incoming_size > top_size:
            container.pop()
            if not container:
                container.append((incoming_size, incoming_dir))
            else:
                cross_check(container, incoming_size, incoming_dir)
        else:
            print(f'top of stack bigger than incoming')
    else:
        container.append((incoming_size, incoming_dir))

def solution(A, B):
    # write your code in Python 3.6
    # https://app.codility.com/c/run/trainingUPYQM8-5MH/
    # Need two stacks, one for upstream and another for downstream
    # this is about stacks and queues
    # We can try to use a stack
    # we need to bear in mind direction

    # this might give a reference
    holder = []
    # change strategy
    for idx, tpl in enumerate(zip(A, B)):
        size, dir = tpl
        if not holder:
            holder.append((size, dir))
        else:
            cross_check(holder, tpl[0], tpl[1])

    return len(holder)