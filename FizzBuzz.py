import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    testlist = test.split(' ')
    print testlist

    i = 1
    x = int(testlist[0])
    y = int(testlist[1])
    n = int(testlist[2])

    print "x is ", x
    print "y is ", y
    print "n is ", n

    while i <= n:
        if i % x == 0 and i % y == 0:
            print i, "is divisible by ", x, "and", y, "FB"
        elif i % x == 0:
            print i, "is divisible by ", x, "F"
        elif i % y == 0:
            print i, "is divisible by ", y, "B"
        i += 1

test_cases.close()