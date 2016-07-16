def fibonacci(number):
    result = 0 
    x = 1

    position = 0
    msg = "%s" % result
    while True:
        temporal = result
        result = x
        x = temporal + x

        position = position + 1
        msg = "%s, %s" % (msg, result) 

        if result == number:
            print "%s... did anyone watch lost?" % msg
            print "The position is %s (0 is the first)" % position
            return position


def fibonacci_yield():
    result, x, position = 0, 1, 0
    temporal=0
    while True:
        yield result
        temporal, result  = result, x
        x += temporal

# Calling the functions ...

fibonacci(34)

position=0
msg=""
for value in fibonacci_yield():
    msg = "%s, %s" % (msg, value) if position>0 else "0"
    if value == 34:
       print "\n---- YIELD ---- \n%s... did anyone watch lost?" % msg
       print "The position is %s (0 is the first)" % position
       break
    position += 1


"""
OUTPUT:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34... did anyone watch lost?
The position is 9 (0 is the first)

---- YIELD ---- 
0, 1, 1, 2, 3, 5, 8, 13, 21, 34... did anyone watch lost?
The position is 9 (0 is the first)

"""
