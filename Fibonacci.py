#Produce the fibonnaci sequence up until 1_000_000 using a generator with yield

def fibonnaci (amount):
    a, b = 0, 1
    while ( a <= amount):
        yield a
        a, b = b, a + b
    
for n in fibonnaci (1_000_000):
    print(n)