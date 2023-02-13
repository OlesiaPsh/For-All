def rev_str(str):
    new_str = ''
    if len(str) == 0:
        return ""
    return str[-1] + rev_str(str[:-1])
print(rev_str('qweerty'))