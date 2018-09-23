class inclusive_range:
    def __init__(self,*args):
        numargs=len(args)
        if numargs<1: raise TypeError('requires at leat 1 param')
        elif numargs ==1:
            self.stop=args
            self.step=1
            self.start=0
        elif numargs==2:
            (self.start,self.stop)=args
            self.step=1
        elif numargs==3:
            (self.start,self.stop,self.step)=args
        elif numargs>3:
            raise TypeError('to much params')
    def __iter__(self):
        i = self.start
        while i<=self.stop:
            yield i
            i+=self.step


def main():
    o = inclusive_range(5,25,2)
    for i in o: print(i,end=' ')

main()