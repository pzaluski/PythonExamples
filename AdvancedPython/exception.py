try:
    file=open('text.txt')
except IOError as e:
    print("Error: {}"+format(e))
else:
    for line in file: print(line.strip())
