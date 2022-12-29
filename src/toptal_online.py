
start_tag = "<app>"
end_tag = "</app>"


def countMissingTag(input_str, stack, missing):
    if not input_str:
        return len(stack)
    if input_str.find(start_tag) == 0:
        new_idx = input_str.find("<app>") + 4
        stack.append(start_tag)
        substr = input_str[new_idx+1:]
        return countMissingTag(substr, stack, missing)
    else:
        if stack and stack[-1] == start_tag:
            stack.pop()
        else:
            stack.append(end_tag)
        idx = input_str.find("</app>") + 5
        substr = input_str[idx + 1:]
        return countMissingTag(substr, stack, missing)










