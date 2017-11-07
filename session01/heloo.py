a = int(input("Nhap a:"))
b = int(input("Nhap b:"))
c = int(input("Nhap c:"))
print ("Phuong trinh ax^2 + bx +c")
denta = b*b - 4*a*c
if a == 0:
    print("Phuong trinh co nghiem la x = ", -c/b)
else:
    if denta < 0:
        print("Phuong trinh vo nghiem")
    elif denta == 0:
        print("phuong trinh co nghiem kep x = ",-b/(2*a))
    else:
        x_1 = (-b+denta**0.5)/(2*a)
        x_2 = (-b-denta**0.5)/(2*a)
        print("phung trinh co 2 nghiem x1={0}, x2={1}".format(x_1, x_2) )
