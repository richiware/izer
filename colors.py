import sys

for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write(u"\u001b[38;5;" + code + "m " + (code + ' ' + sys.argv[1]).ljust(6))
    print(u"\u001b[0m")