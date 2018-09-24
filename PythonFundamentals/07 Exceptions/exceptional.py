
import sys


def convert(s):
    '''Converts to string'''
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion failed: {}".format(str(e)), file=sys.stderr)
        return -1


print(convert("-23"))
print(convert("supa dfadk"))
print(convert([4, 5, 6]))
