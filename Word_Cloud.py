# Word_Cloud.py


# wordcloud
# https://open.kattis.com/problems/wordcloud

# python Word_Cloud.py < Word_Cloud_in.txt
import math

def calc_size(occurence:int,c_max:int,word):
    height = 8 + math.ceil(40*(occurence-4)/(c_max-4))
    return math.ceil(9/16*len(word)*(height)),height

cloud_no = 1
while (line:=input())!='0 0':
    cloud_height = 0
    max_cloud_width, num_words = map(int,line.split())
    word_data = []
    for _ in[0]*num_words:
        word, occurence = input().split()
        word_data += [[word,int(occurence)]]
    c_max = max(data[1]for data in word_data)
    curr_width = 0
    curr_max_height = 0
    for word,occurence in word_data:
        new_word_width, new_word_height = calc_size(occurence,c_max,word)
        if curr_width!=0:
            if curr_width + 10 + new_word_width <= max_cloud_width:
                curr_max_height = max(curr_max_height,new_word_height)
                curr_width += 10 + new_word_width
            else:
                cloud_height += curr_max_height
                # print(curr_max_height)
                curr_max_height = new_word_height
                curr_width = new_word_width
        else:
            curr_max_height = new_word_height
            curr_width = new_word_width
    cloud_height += curr_max_height
    print(f'CLOUD {cloud_no}: {cloud_height}')
    cloud_no += 1


