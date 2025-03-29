total = ['.',*map(str,range(0,10)),*'abcdefghijklmnopqrstuvwxyz',*'abcdefghijklmnopqrstuvwxyz'.upper()]
print(*[(x,ord(x))for x in total])