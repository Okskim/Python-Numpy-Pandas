import os
f = open('my_file', 'w')
f.write('Hello, ')
f.write('World!')
f.close()

f = open('my_file', 'r')
print(f.read(5))
print(f.read())
f.close()
################

f = open(r'my_file', 'w')
f.write('01234567890123456789')
f.seek(5)
f.write('Hello, World!')
f.close()
f = open(r'my_file')
print(f.read())
################


f = open(r'my_file')
lines = f.readlines()
f.close()
lines[0] = "This is a my_file2 \n" 
f = open(r'my_file2','w')
f.writelines(lines)
f.close()
##################


f = open(r'my_file')
while True:
    char = f.read(1)
    if not char:
        break
#process(char)
f.close()
####################

import pickle
t1 = [1, 2, 3]
s = pickle.dumps(t1)
t2 = pickle.loads(s)
print (t2)
###################


from struct import*
out = open("123.bin", "wb") 
format = "if5s" 
data = pack(format, 24,12.48, b'12456785')
out.write(data)
out.close()
input = open("123.bin", "rb")
data = input.read()
input.close()
format = "if5s" # one integer
value,value2,value3 = unpack(format, data) 

print (value)
print (value2)
print (value3)
print (calcsize(format))
#######################

f = open('C:test.txt', 'w')
f.write('string1 \r\n')
f.write('string2')

f.close()

f = open('C:test.txt', 'r')
print(f.read(7))
print(f.read())

f.close()

f = open('C:test.txt', 'w')
f.write('abcdef')
print(f.seek(3))

f.write('CD')

f.close()

f = open('C:test.txt', 'r')
print(f.read())

f = open('C:test.txt', 'w')
f.write('string \r\n')

f.write('string \r\n')

f.write('string \r\n')

f.close()

f = open('C:test.txt', 'r')
print(f.readline())
print(f.readlines())

f.close()

f = open('C:test.txt', 'r')
strings = f.readlines()
print(strings)
f.close()

strings[0] = 'STRING'
f = open('C:test.txt', 'w')
f.writelines(strings)

f.close()
