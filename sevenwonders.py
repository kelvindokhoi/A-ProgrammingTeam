# sevenwonders

s=input();m=[s.count(x)for x in'TCG'];print(sum(x*x for x in m)+7*min(m))

# a=[*input()];t,c,g=[sum([i==x for i in a])for x in["T","C","G"]];print(t*t+c*c+g*g+min(t,c,g)*7)