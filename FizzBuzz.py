import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    testlist = test.split(' ')
    print testlist

    i = 1
    x = testlist[0]
    y = testlist[1]
    n = testlist[2]
    print "x is " + x
    print "y is " + y
    print "n is " + n

    while i <= n:
        if i % x 


test_cases.close()