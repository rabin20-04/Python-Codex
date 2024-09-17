a = 0
b = 1


while a < 10:
    print(a)
    a, b = b, a + b


print("next way ")

a = 0
b = 1
c = 0
print(a)
while c < 10:
    c = a + b
    a = b
    b = c
    print(c)