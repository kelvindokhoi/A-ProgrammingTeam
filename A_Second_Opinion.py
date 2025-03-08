# A Second Opinion

a=int(input())
hour=(a//3600)
min = (a-hour*3600)//60
sec = (a-hour*3600-min*60)
print(f"{hour} : {min} : {sec}")