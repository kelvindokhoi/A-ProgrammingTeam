# eligibility
# Eligibility


for i in [0]*int(input()):
 a,b,c,d=input().split()
 print(a,["eligible","ineligible","coach petitions"][0 if int(b[:4])>2009 or int(c[:4])>1990 else 1 if int(d)/5>8 else 2])

# for i in [0]*int(input()):w=int;a,b,c,d=input().split();print(a,[y:="eligible","in"+y,"coach petitions"][0 if w(b[:4])>2009 or w(c[:4])>1990 else 1 if w(d)>40 else 2])