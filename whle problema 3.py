n=0
s=0
while not((n%2!=0) and (n%3==0)):
    n=eval(input("Numarul="))
    if n%2==0:
        s+=n
print("suma=",(s))