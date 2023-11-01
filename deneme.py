



"""
"""
"""
"""
yüklesklik=5
def draw_triangle(n):
    for i in range(n):
        for j in range(n-i-1):
            print("*",end="")
        for j in range(n-i+1):
            print("*",end="")
        print()
draw_triangle(yüklesklik)


