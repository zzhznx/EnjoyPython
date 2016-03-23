import itertools
password = '9g9xxxx'
count = 0
for c in password:
    if c == 'g' or c == '9':
        count += 1
result = ''
for i in itertools.product('9g', repeat=count):
    temp = list(password)
    j = 0
    for n in range(len(password)):
        if password[n] == 'g' or password[n] == '9':
            temp[n] = i[j]
            j += 1
        else:
            temp[n] = password[n]
    result = result + "".join(temp) + ","
print(result[:-1] + ".")
