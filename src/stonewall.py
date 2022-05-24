# https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/
# https://www.geeksforgeeks.org/the-skyline-problem-set-2/
def emptyStack(stack, item):
    if stack and stack[-1] == item:
        stack.pop()
        return emptyStack(stack, item)
    else:
        return stack

def solution(H):
    stack = []
    counter = 0
    for item in H:
        if not stack:
            stack.append(item)
        elif item > stack[-1]:
            stack.append(item)
        elif item < stack[-1]:
            stack = emptyStack(stack, stack[-1])
            counter +=1
            stack.append(item)
        else:
            pass
    counter += len(set(stack))
    return counter




    #https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/
    # https://funnelgarden.com/stonewall-codility-solution/
    # The strategy is:
    #
    # break up each array element into sub-blocks to store on a stack
    # for each subsequent array element, check if there are existing blocks on the stack that can create it
    # only add new block to the stack if impossible to reuse sub-blocks from stack

    # We need to draw it and see what actions we take when a new block is on stack vs next element
    # in the array


    pass
