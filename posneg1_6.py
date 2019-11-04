def chkSign(no):
    if no>0:
        print("Positive");
    elif  no<0:
        print("Negative");
    else:
        print("Zero");        



def main():
    no=int(input("Enter a number"));
    chkSign(no);

if __name__=="__main__":
    main();