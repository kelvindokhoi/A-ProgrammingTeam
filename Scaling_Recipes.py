# Scaling_Recipes.py

# recipes
# https://open.kattis.com/problems/recipes

# python Scaling_Recipes.py < Scaling_Recipes_in.txt

for case in range(1,int(input())+1):
    num_ingre, num_por, num_out = map(int,input().split())
    convert_rate = num_out/num_por
    all_ingre = []
    for _ in[0]*num_ingre:
        name,weight,percentage = input().split()
        weight,percentage = float(weight),float(percentage)/100
        if percentage == 1:
            convert_rate *= weight
        all_ingre.append([name,percentage])
    print(f'Recipe # {case}')
    print(*[f'{name} {percentage*convert_rate}'for name,percentage in all_ingre],sep='\n')
    print('-'*40)