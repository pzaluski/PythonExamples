import os

p='/dummyFile'

if os.path.exists(p):
    process_file(p)
else:
    print('No such file: {}'.format(p))