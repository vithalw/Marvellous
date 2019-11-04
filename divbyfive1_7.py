def chkDivisibility(no):
    if (no%5==0):
        return 1;
    else:
        return 0;       



def main():
    no=int(input("Enter a number: "));
    res=chkDivisibility(no);
    if(res==1):
        print("Divisible");
    else:
        print("Not Divisible");    


if __name__=="__main__":
    main();