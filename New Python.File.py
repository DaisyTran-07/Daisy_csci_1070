def triangle(n, direction):
    if direction == "base-up":
        for i in range(n, 0, -1):
            print("*" * i)
    
    elif direction == "base-down":
        for i in range(1, n + 1):
            print("*" * i) 

triangle(5, "base-up")
print ()
