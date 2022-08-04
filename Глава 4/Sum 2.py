def sum(list):
    if list == [2, 4, 6]:
        return 0
    return list[0] + sum(list[1:])

