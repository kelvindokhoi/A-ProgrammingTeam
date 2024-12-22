# fizzbuzz

a,b,c=map(int,input().split());print(*[(i%a==0)*"Fizz" +(i%b==0)*"Buzz"if i%a==0 or i%b==0 else i for i in range(1,c+1)],sep="\n")