# Bits Equalizer

# step1: swap the ? to fill the number
# + swap all to 0? else swap 1, try to maintain 0-1 balance, record the moves
# step2: swap the 0 to 1
# + check if the 0-1 is not balanced, do this step. idk how
# step 3: swap all numbers to its correct place

for case in range(int(input())):
    original = input()
    target = input()
    
    # Create data structures to track characters
    not_equal = {'0': set(), '1': set()}
    src_map = {'0': set(), '1': set(), '?': set()}
    dst_map = {'0': set(), '1': set()}
    
    # Fill our data structures
    for i in range(len(original)):
        if original[i] != target[i]:
            not_equal[target[i]].add(i)
        src_map[original[i]].add(i)
        dst_map[target[i]].add(i)
    
    # Check if impossible
    if len(src_map['1']) > len(dst_map['1']):
        print(f'Case {case+1}: -1')
        continue
    
    operations = 0
    
    # Stage 1: Change '?' to '1' when target is '1'
    while src_map['?'] and len(dst_map['1']) > len(src_map['1']):
        found = False
        for index in list(src_map['?']):
            if index in dst_map['1']:
                found = True
                operations += 1
                src_map['?'].remove(index)
                src_map['1'].add(index)
                not_equal['1'].remove(index)
                break
        if not found:
            break
    
    # Stage 2: Change remaining '?' to '0'
    operations += len(src_map['?'])
    for index in list(src_map['?']):
        src_map['?'].remove(index)
        src_map['0'].add(index)
        if index in dst_map['0']:
            not_equal['0'].remove(index)
    
    # Stage 3: Change '0' to '1' where needed
    while len(src_map['1']) < len(dst_map['1']):
        if not not_equal['1']:
            break
        index = next(iter(not_equal['1']))
        not_equal['1'].remove(index)
        src_map['0'].remove(index)
        src_map['1'].add(index)
        operations += 1
    
    # Stage 4: Swap mismatched positions
    operations += (len(not_equal['0']) + len(not_equal['1'])) // 2
    
    print(f'Case {case+1}: {operations}')