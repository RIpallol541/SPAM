import os
def log_pas(link):
    link_use = os.path.abspath(link)
    data = []
    filelp = open(f"{link_use}", "r")
    dlin = filelp.readlines()
    for line in dlin:
        stor = line.strip().split(":")
        data.append(stor)
    return data