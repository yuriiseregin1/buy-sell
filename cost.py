a = '18000'
print(len(a))
if len(a) == 4:
    a = a[0] + ' ' + a[1:]
if len(a) == 5:
    print(a[0:2], a[2:])

    b = a[0:2] + ' ' + a[2:]

if len(a) == 6:
    b = a[0:3] + ' ' + a[3:]
if len(a) == 7:
    b = a[0] + ' ' + a[1:4] + ' ' + a[4:]
if len(a) == 8:
    a = a[0:2] + ' ' + a[2:5] + ' ' + a[5:]
print(b)