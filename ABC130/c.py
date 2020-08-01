w,h,x,y = (int(i) for i in input().split())

if y==(h/w)*x and y==-(h/w)*x+h:
    print("{} {}".format(w*h/2,1))
else:
    print("{} {}".format(w*h/2,0))

