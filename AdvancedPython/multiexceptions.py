def main():
    try:
        x=1/2
        file=open("text2.txt")
    except ZeroDivisionError as e:
        print('Cos poszlo nie tak ',e)
    except IOError as e:
        print('Nie ma takiego pliku : ',e)



if __name__=="__main__":
    main()