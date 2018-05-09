from random import randint


def most_frequent_int( array ):
    counter = {}
    # count the occurences of each integer
    result      = 0
    max_freq    = 0
    for i in array:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
        if counter[i] > max_freq:
            max_freq = counter[i]
            result = i

    return result 


if __name__ == '__main__':
    target  = 20
    array   = []
    for i in range(200):
        if i % 2 == 0:
            array.append(target)
        else:
            array.append(randint(0, 100))

    result = most_frequent_int( array )
    
    print( target == result )
