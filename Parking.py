# Parking.py

# parking
# https://open.kattis.com/problems/parking

# python Parking.py < Parking_in.txt

A,B,C = map(int,input().split())
price = [0,A,B,C]
time_table = [0]*100
def update(time:list,start,end):
    for i in range(start-1,end-1):
        time[i] += 1
update(time_table,*map(int,input().split()))
update(time_table,*map(int,input().split()))
update(time_table,*map(int,input().split()))
payment = sum(indiv*price[indiv] for indiv in time_table)
print(payment)


# golfed:
# t,I=[0]*100,input;C=[0]+[*map(int,I().split())];exec('for i in range(*map(int,I().split())):t[i-1]+=1\n'*3);print(sum(t[i]*C[t[i]]for i in range(100)))
