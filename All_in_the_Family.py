# All in the Family
# https://open.kattis.com/problems/allinthefamily

tree_des_num, query_pair_num = map(int,input().split())
family_tree = dict()
for _ in range(tree_des_num):
    parent, _, *children = input().split()
    for child in children:
        family_tree[child] = parent

for _ in range(query_pair_num):
    si,sj = input().split()
    si_ancestors = [si]
    s0 = si
    while s0 in family_tree:
        s0 = family_tree[s0]
        si_ancestors.append(s0)
    si_ancestors_set = set(si_ancestors)
    common_ancestor = sj
    n = 0
    while common_ancestor not in si_ancestors_set:
        n += 1
        common_ancestor = family_tree[common_ancestor]
    m = si_ancestors.index(common_ancestor)

    if m==0:
        if n==1:
            print(f"{sj} is the child of {si}")
        else:
            print(f"{sj} is the "+"great "*(n-2)+f"grandchild of {si}")
    elif n==0:
        if m==1:
            print(f"{si} is the child of {sj}")
        else:
            print(f"{si} is the "+"great "*(m-2)+f"grandchild of {sj}")
    elif m==n and m>0:
        if n==1:
            print(f"{si} and {sj} are siblings")
        elif n>1:
            n -= 1
            nth = "th" if n in[11,12,13] else "st"if n%10==1 else "nd" if n%10==2 else "rd" if n%10==3 else "th"
            print(f"{si} and {sj} are {n}{nth} cousins")
    else:
        if m>n:
            n,m=m,n

        times = n-m
        m -= 1
        m_th = "th" if m in[11,12,13] else "st"if m%10==1 else "nd" if m%10==2 else "rd" if m%10==3 else "th"
        times_s = "s" if times>1 else ''
        print(f"{si} and {sj} are {m}{m_th} cousins, {times} time{times_s} removed")