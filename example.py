import sys
try:
    n = sys.argv[1]
except:
    print 'SYNTAX: %s N'%sys.argv[0]
    sys.exit()
print n
