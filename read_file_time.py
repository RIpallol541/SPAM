def read_time():
    data = []
    filetime = open("time.txt", "r")
    dlin = filetime.readlines()
    for line in dlin:
        data.append(line.strip())
    return data