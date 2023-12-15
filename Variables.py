#!/usr/bin/env python3

cadena = "mi cadena"
print(cadena)
# mi cadena

ip_address = "192.168.1.42"
print(ip_address)
# 192.168.1.42
print(type(ip_address))
# <class 'str'>

port = 80

print(port)
# 80
print(type(port))
# <class 'int'>

number = 4.5
print(number)
# 4.5
print(type(number))
# <class 'float'>

number = float(4)
print(number)
# 4.0
print(type(number))

number = int(4.0)
print(number)
# 4
print(type(number))
# <class 'int'>






# LISTAS

my_ports = []
my_ports.append(22)
my_ports.append(80)
my_ports.append(443)
my_ports.append(8080)

my_ports.extend([84, 90])

my_ports += [86, 87]

my_ports = my_ports + [88, 89]

my_ports = sorted(my_ports)

del my_ports[0]


my_ports2 = [22, 80, 443]

print("\nListas")
print(my_ports[0])
print(my_ports[1])
print(my_ports[2])

#print("\nBucle con type")
#for port in my_ports:
#    print("Puerto: " + str(port))

print("\nBucke con print f")
for port in my_ports:
    print(f"Puerto: {port}")

print(f"\n[+] Total de la lista {len(my_ports)} elementos ")


>>> mi_lista = [1, 2, 3, 4, 5]
>>> mi_lista
[1, 2, 3, 4, 5]
>>> print(mi_lista)
[1, 2, 3, 4, 5]
>>> mi_lista[:2]
[1, 2]
>>> mi_lista[:3]
[1, 2, 3]
>>> mi_lista[:4]
[1, 2, 3, 4]
>>> mi_lista[4]
5
>>> mi_lista[0]
1
>>> mi_lista[0:3]
[1, 2, 3]
>>> mi_lista[2:4]
[3, 4]
>>> 
#
>> mi_lista
[1, 2, 3, 4, 5]
>>> mi_lista[:2]
[1, 2]
>>> mi_lista[2:]
[3, 4, 5]
>>> mi_lista[1]
2
>>> mi_lista[-1]
5
>>> mi_lista[-2]
4
>>> mi_lista[-2:]
[4, 5]
>>> mi_lista[-4:]
[2, 3, 4, 5]
>>> mi_lista[:-2]
[1, 2, 3]
>>> 

>>> mi_lista
[1, 2, 3, 4, 5]
>>> mi_lista.insert(2, 9)
>>> mi_lista
[1, 2, 9, 3, 4, 5]
>>> mi_lista.insert(2, "Hola")
>>> mi_lista
[1, 2, 'Hola', 9, 3, 4, 5]
>>> mi_lista.pop()
5
>>> mi_lista
[1, 2, 'Hola', 9, 3, 4]
>>> mi_lista.pop()
4
>>> mi_lista.pop()
3
>>> mi_lista.pop()
9
>>> mi_lista.pop()
'Hola'
>>> mi_lista
[1, 2]
>>> 

>>> mi_lista = [5, 3, 7, 2, 1, 6, 1]
>>> mi_lista.index(7)
2
>>> mi_lista[2]
7
>>> mi_lista += [7]
>>> mi_lista
[5, 3, 7, 2, 1, 6, 1, 7]
>>> mi_lista.index(7)
2
>>> enumerate(mi_lista)
<enumerate object at 0x7f109aa5e660>

>>> for x, y in enumerate(mi_lista):
...     print(x)
... 
0
1
2
3
4
5
6
7
>>> for x, y in enumerate(mi_lista):
...     print(y)
... 
5
3
7
2
1
6
1
7
>>> for x, y in enumerate(mi_lista):
...     print(f"{x}: {y}")
... 
0: 5
1: 3
2: 7
3: 2
4: 1
5: 6
6: 1
7: 7
>>>


>>> mi_lista
[5, 3, 7, 2, 1, 6, 1, 7]
>>> indices = [x for x, y in enumerate(mi_lista) if y == 6]
>>> indices
[5]
>>> mi_lista[5]
6
>>> 
>>> mi_lista.count(7)
2
>>> sorted(mi_lista)
[1, 1, 2, 3, 5, 6, 7, 7]
>>> mi_lista = sorted(mi_lista)
>>> mi_lista
[1, 1, 2, 3, 5, 6, 7, 7]
>>> set(mi_lista)
{1, 2, 3, 5, 6, 7}
>>> type(set(mi_lista))
<class 'set'>
>>> 

>>> mi_lista
[1, 1, 2, 3, 5, 6, 7, 7]
>>> set(mi_lista)
{1, 2, 3, 5, 6, 7}
>>> list(set(mi_lista))
[1, 2, 3, 5, 6, 7]
>>> mi_lista = list(set(mi_lista))
>>> mi_lista
[1, 2, 3, 5, 6, 7]
>>

>>> mi_lista = [12, 8, 34, 65, 132, 2, 7, 8]
>>> print(f"[+] El numero mas alto es {max(mi_lista)}")
[+] El numero mas alto es 132
>>> print(f"[+] El numero mas bajo es {min(mi_lista)}")
[+] El numero mas bajo es 2
>

>>> sum(mi_lista)
268
>>> len(mi_lista)
8
>>> sum(mi_lista) / len(mi_lista)
33.5
>>> mi_lista.pop()
8
>>> len(mi_lista)
7
>>> sum(mi_lista) / len(mi_lista)
37.142857142857146
>>> 
>>> round(sum(mi_lista) / len(mi_lista), 2)
37.14
