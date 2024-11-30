def vlr_fibonacci(num):
    if num<=1:
        return num
    return vlr_fibonacci(num-1) + vlr_fibonacci(num-2)

print (vlr_fibonacci(10))