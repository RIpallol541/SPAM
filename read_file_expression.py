import os
def read_expression(link):
    link_use = os.path.abspath(link)
    data = []
    fileExpression = open(f"{link_use}", "r", encoding="utf-8")
    len = 0
    dlin = fileExpression.readlines()
    for line in dlin:
        data.append(line.strip())
        len += 1
    return data, len

