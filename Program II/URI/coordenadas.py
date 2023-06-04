a=[]

p = input()

for valor in p.split():
    a.append(float(valor))
x = a[0]
y = a[1]

if x>0 and y>0:
    print('Q1')
elif x<0 and y>0:
    print('Q2')
elif x<0 and y<0:
    print('Q3')
elif x>0 and y<0:
    print('Q4')
elif x==0 and y!=0:
    print('Eixo Y')
elif x!=0 and y==0:
    print('Eixo X')
else:
    print('Origem')
