def rec(num):
    if num == 1:
        return 1
    return num * rec(num-1)
    
print(rec(5))