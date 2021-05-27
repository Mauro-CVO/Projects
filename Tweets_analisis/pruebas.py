
words = ['hola','adios','perro','gato']
file = ['(01)','(02)','(03)']

for fs in file:
f = open('pruebas.txt','a',encoding='utf-8')
for word in words:
    f.write(word + '\n')

f.close