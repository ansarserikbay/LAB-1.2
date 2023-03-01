R=int(input("R=")) #Shenberdin radiusy
P=3.14
l=0
s=0
d=0
Engiz=input("Tandau: ")
if Engiz=="L":
    l=2*P*R #Uzyndyk formulasy
    print("Shenberdin uzyndygy L: ", l)
elif Engiz=="S":
    s=2*P*R*R #Audan formulasy
    print("Shenberdin audany S: ", s)
elif Engiz=="D":
    d=2*R #Diametr formulasy
    print("Shenberdin diametr D: ", d)
else:
    print("Shartka sai kelmidi!!!")