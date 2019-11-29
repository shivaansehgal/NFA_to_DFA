import json

with open('input.json') as f:
    d=json.load(f)

n=int(d['states'])
l=d['letters']
tf=d['t_func']
f=d['final']

dfa=[]
fina=[]

inp = [[[]] * len(l) for i in range(n)]

for e in tf:
    inp[int(e[0])][l.index(e[1])]=e[2]

"""
for i in range(0,n):
    for j in range(0,len(l)):
        print(inp[i][j],end=' ')
    print()
"""

out = [[[]] * len(l) for i in range(2**n)]

for i in range(0,2**n):
    t=i
    kiska=[]
    j=0
    while t>0:
        if t%2==1:
            kiska.append(j)
        t = int(t/2)
        j = j+1
    for finalstate in f:
        if(finalstate in kiska):
            fina.append(i)
    for alfa in l:
        union=[]
        for state in kiska:
            union= list(set(union)|set(inp[state][l.index(alfa)]))
        fin=0
        for num in union:
            fin=fin+(2**num)
        out[i][l.index(alfa)]=fin
        dfa.append([i,alfa,fin])
       # print(union,end=" ")
    #print()


"""
for i in range(0,2**n):
    for j in range(0,len(l)):
        print(out[i][j],end=' ')
    print()

for i in range(0,n):
    for j in range(0,len(l)):
        print(inp[i][j],end=' ')
    print()
"""

final = []
for ele in fina:
    if ele not in final:
        final.append(ele)

y={ 
        "states": 2**n ,
        "letters":l,
        "t_func":dfa,
        "start":2**int(d['start']),
        "final":final
        }

with open("output.json", "w") as write_file:
        json.dump(y, write_file)




