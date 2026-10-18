# Parsing Hex
# python parsinghex.py < parsinghex_in.txt
# https://open.kattis.com/contests/hgr7mz/problems/parsinghex

import re


def findhex(string):
    hex_pattern = r"(0[xX][0-9a-fA-F]*)"
    results = re.findall(hex_pattern,string)
    if len(results)!=0:
        for i in range(len(results)):
            if len(results[i])>=10:
                results[i] = results[i][:10]
        return results

all_inp = []
while True:
    try:
        inp = input()
        all_inp.append(inp)
    except:
        break

for inp in all_inp:
    hex_nums = findhex(inp)
    if hex_nums:
        for hex_num in hex_nums:
            print(hex_num,int(hex_num,base=16))