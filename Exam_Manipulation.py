# Exam Manipulation
# https://open.kattis.com/problems/exammanipulation

from itertools import product

num, length = map(int,input().split())

student_answer = [input() for _ in ' '*num]

def calc_score(student,correct):
    count = 0
    for a,b in zip(student,correct):
        if a==b:
            count += 1
    return count

def find_min_student1(student_answer,num,length):
    # best_option = None
    maximin = 0
    for possible_solution in product('TF',repeat=length):
        possible_maximin = min(calc_score(student,possible_solution) for student in student_answer)
        if possible_maximin > maximin:
            maximin = possible_maximin
    return maximin




print(find_min_student1(student_answer,num,length))