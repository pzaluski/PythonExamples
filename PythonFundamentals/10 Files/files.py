import sys
print(sys.getdefaultencoding())

f = open("wasteland.txt", mode='wt', encoding='utf-8')

f.write('To jest pierwsza linia')
f.write(', ktora chyba sie nie konczy\n')
f.write('dopiero tutaj')

f.close()

g = open('wasteland.txt', mode='rt', encoding='utf-8')
print(g.readlines())
g.close()

print(30*"=")
def main(filename):
    f = open(filename, mode='rt', encoding='utf-8')
    for line in f:
        sys.stdout.write(line)
    f.close()


if __name__ == '__main__':
    main(sys.argv[1])
