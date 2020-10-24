n=eval(input("numarul="))
i=1
s=0
p=1
while i<=n:
    s+=i
    p*=i
    i+=1
    print("Suma=",(s))
    print("produsul=",(p))
    print("media aritmetca=",(s/n))