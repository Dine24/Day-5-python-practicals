st=input("enter a string=")
s=st.split()[::-1]
l=[]
for i in s:
    l.append(i)
print(" ".join(l))
