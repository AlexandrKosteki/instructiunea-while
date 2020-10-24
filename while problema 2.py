s_p=0
s_n=0
nr_p=0
nr_n=0
l=1
while l<=12:
    t=eval(input("Temperatura lunii="))
    if t>0:
        s_p+=t
        nr_p+=1
    if t<0:
        s_n+=t
        nr_n+=1
    l+=1
print("Media_poz=",(round(s_p/nr_p,2)))
print("Media_neg=",(round(s_n/nr_n,2)))