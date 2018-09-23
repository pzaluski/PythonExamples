#generator_expt ::= "(" express comp_for ")"

#(x*y for x in range(10) for y in bar(x))

print(x*y for x in range(10) for y in [1, 2])

lista = ["jeden", "dwa", "trzy"]

print(list(enumerate(lista, start=1)))


with open('text.txt') as f:
    for line in iter(f.readline,''):
        print(line.split())

def inclusive_range(start, stop, step):
    i=start
    while i<=stop:
        yield i
        i+=1


def main():
    print("generating...")
    for i in inclusive_range(0,25,1):
        print(i,end=' ')

main()