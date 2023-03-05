def recursive(k):
    if(k > 0):
        return k + recursive(k-1)
    else:
        result = 0
        return result

print("\n\nRecursion Example Result")
x = recursive(6)
print(x)