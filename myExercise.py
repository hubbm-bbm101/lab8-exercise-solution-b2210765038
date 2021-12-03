import sys
with open(sys.argv[1], "r") as o:
    o_data = [i.split(":")for i in o.read().splitlines()]
o_data = {i[0]: i[1] for i in o_data}

for i in list(sys.argv[2].split(",")):
    try:
        assert i in o_data
    except AssertionError:
        print("Any record of \'%s\' not found!" % i)
    else:
        print("Name:", i, ", University:", o_data[i])
