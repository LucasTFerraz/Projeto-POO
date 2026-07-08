def m(p = None):
    if p is None:
        p = []
    print(p)

def n(e):
    L = []
    L.append(e)
    return L

def l(e, L = []):
    L.append(e)
    return L

m()
m([1,2,3])
m([4,5,6])
m(3)

print(n(1))
print(n(2))
print(n(3))

print(l(1))
print(l(2))
print(l(3))