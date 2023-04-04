# 1
for i in range(151):
    print(i)

# 2
for i in range(5, 1001, 5):
    print(i)

# 3
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# 4
sum = 0
for x in range(1, 500001, 2):
    sum += x
print(sum)

# 5
for x in range(2018, 0, -4):
    print(x)

# 6
low_num = 2
high_num = 9
mult = 3
for x in range(low_num, high_num + 1):
    if x % mult == 0:
        print(x)