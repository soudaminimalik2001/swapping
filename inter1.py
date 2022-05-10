# a={"one":1,"two":2,"three":3}
# for i in a:
#     print(a[i])
f=open("question4.txt","r")
var=f.read()
f1=open("delhi.txt","w")
f2=open("shimla.txt","w")
f3=open("others.txt","a")
list=var.split("\n")
i=0
while i<len(list):
    if "delhi"in list[i]:
        f1.write(list[i])
        f1.write("\n")
    elif"shimla" in list[i]:
        f2.write(list[i])
        f2.write("\n")
    else:
        f3.write(list[i])
        f3.write("\n")
    i+=1
f1.close()
f2.close()
f3.close()
f.close()