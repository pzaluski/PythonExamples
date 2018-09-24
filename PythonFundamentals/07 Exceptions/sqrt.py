import sys

def sqrt(x):

    if x < 0:
        raise ValueError("Negative argument: {}".format(x))

    guess = x
    i = 0
    while guess*guess != x and i < 20:
        guess = (guess+x/guess)/2.0
        i += 1
    return guess

def main():
    try:
        print(sqrt(5))
        print(sqrt(-12))
    except ValueError as e:
        print(e, file=sys.stderr)
    print("Program exitcode 0")

if __name__ == '__main__':
    main()