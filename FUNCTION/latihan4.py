def recursive(x):
    if(x > 0):
        result = x + recursive(x-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Result")
recursive(6)