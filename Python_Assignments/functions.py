def outer_def(a,b,n):
    print("outer loop")
    if(n>0):
        def inner_def():
            print("inner loop")
            return a+b

        add = inner_def()
        n -= 1
        return add + 5 + outer_def(a, b, n)   ## Recursive function, function by call itself
    else:
        return 0

    return add

value = outer_def(1,1,10)
print(value)
