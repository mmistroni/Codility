import logging
def solution(input):
    holder = []
    try:
        for item in input:
            if item == "(":
                holder.append(item)
            else:
                holder.pop()
        return 1 if not holder else 0
    except Exception as e:
        logging.info(f'Excepiton:{str(e)}')
        return 0