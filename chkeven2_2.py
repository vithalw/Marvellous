def chkNum(no):
    if(no%2==0):
        print("Even No")
    else:    
        print("Odd No")

def main():
    number=int(input("Enter a number: "));
    chkNum(number);

if __name__=="__main__":
    main();
    # TODO: write code...