a = int(input())
b = a%10
c = int(((a-b)/10)%10)
d = int(((a-b-c*10)/100)%10)
e = int(((a-b-c*10-d*100)/1000)%10)
mylst = [e, d, c, b]
if e == d:
    print("Bad")
elif d == c:
    print("Bad")
elif c == b:
    print("Bad")
else:
    print("Good")