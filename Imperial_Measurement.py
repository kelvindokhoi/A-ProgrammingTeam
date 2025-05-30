# Imperial_Measurement.py


# measurement
# https://open.kattis.com/problems/measurement

# python Imperial_Measurement.py < Imperial_Measurement_in.txt

c={'thou':0.001,'th':0.001,'inch':1,'in':1,'foot':12,'ft':12,'yard':36,'yd':36,'chain':792,'ch':792,'furlong':7920,'fur':7920,'mile':63360,'mi':63360,'league':190080,'lea':190080}
n,a,_,b=map(str,input().split())
print(int(n)*c[a]/c[b])


# golfed:
# c=dict(zip('th in ch fu mi le fo ya ft yd'.split(),[.001,1,792,7920,63360,190080]+[12,36]*2));n,a,_,b=input().split();print(int(n)*c[a[:2]]/c[b[:2]])