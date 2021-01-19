a=int(input("Enter the value for side a: "))
b=int(input("Enter the value for side b: "))
c=int(input("Enter the value for side c: "))
s=a<b+c and b<a+c and c<a+b
if a<1 or a>10:
    print("Value of a is not in the range (1-10)")
elif b<1 or b>10:
    print("Value of b is not in the range (1-10)")
elif c<1 or c>10:
    print("Value of c is not in the range (1-10)")
elif not s==True:
    print("Not a triangle")
else:
    if a==b and b==c:
        print("Equilateral triangle")
    elif a!=b and b!=c and c!=a:
        print("Scalene triangle")
    else:
        print("Isosceles triangle")