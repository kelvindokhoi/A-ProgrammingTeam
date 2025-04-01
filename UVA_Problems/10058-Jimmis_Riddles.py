# 10058 - Jimmi's Riddles

# python UVA_Problems/10058-Jimmis_Riddles.py < UVA_Problems/10058-Jimmis_Riddles_in.txt
# python 10058-Jimmis_Riddles.py < 10058-Jimmis_Riddles_in.txt
# python UVA_Problems/10058-Jimmis_Riddles.py < UVA_Problems/10058-Jimmis_Riddles_in.txt > UVA_Problems/10058-Jimmis_Riddles_out.txt

# python A.FORTESTONLY.py < UVA_Problems/10058-Jimmis_Riddles_in.txt > UVA_Problems/10058-Jimmis_Riddles_out.txt  

# def debug_wrapper(func):
#     def wrapper(*args, **kwargs):
#         print(f"Entering {func.__name__} with args: {args}, kwargs: {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Exiting {func.__name__} with result: {result}")
#         return result
#     return wrapper

def debug_wrapper(func):
    def wrapper(*args, **kwargs):
        # print(f"Entering {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        # print(f"Exiting {func.__name__} with result: {result}")
        return result
    return wrapper



@debug_wrapper
def statement(string):
    n = len(string)
    i = 0
    if string==[]:
        return 0
    next_index = action(string,i,n)
    if next_index==-2 or next_index==n:
        return 1
    elif next_index==-1 :
        return 0
    elif next_index>i:
        if next_index<n-1 and string[next_index]==',':
            return statement(string[next_index+1:])
        else:
            return 0
    return 0

@debug_wrapper
def action(string,i,n):
    if i==n-1:
        return -1
    next_index = active_list(string,i,n)
    if next_index==-2:
        return -1
    elif next_index==n-1:
        return -1
    if next_index>i:
        i = next_index
    else:return -1

    next_index = verb(string,i,n)
    if next_index==-2:
        return -1
    elif next_index==-1:
        return -1
    if next_index>i:
        i = next_index
    else:return -1

    next_index = active_list(string,i,n)
    if next_index==-2:
        return -1
    elif next_index==-1:
        return -1
    if next_index>i:
        i = next_index
    else:return -1
    return i

@debug_wrapper
def active_list(string,i,n):
    if i>n-1:
        return -2
    next_index = actor(string,i,n)
    if next_index==-2:
        return -2
    elif next_index==-1:
        return -1
    if next_index>i:
        i = next_index
    else:return -1
    while i<n and string[i]=='and':
        i+=1
        if i>=n:
            return -1
        next_index = actor(string,i,n)
        if next_index==-2:
            return -2
        elif next_index==-1:
            return -1
        i = next_index
    return i

@debug_wrapper
def actor(string,i,n):
    nouns = ['tom','jerry','goofy','mickey','jimmy','dog','cat','mouse']
    next_word = string[i]
    if next_word in nouns:
        return i+1
    elif next_word in ['a','the']:
        if i<n-1 and string[i+1] in nouns:
            return i+2
        else:
            return -1
    else:
        return -1

@debug_wrapper
def verb(string,i,n):
    verbs = ['hate','love','know','like','hates','loves','knows','likes']
    if string[i] not in verbs:
        return -1
    return i+1

# i=0
while True:
    try:
        # i+=1
        # print(f"Case {i}")
        print(["NO I WON'T","YES I WILL"][statement(input().replace(',',' , ').split())])
    except EOFError:
        break