def pattern(no):
    for i in range(0,no,1):
        print("*",end=" ");

def main():
    no=int(input("Enter a number: "));
    pattern(no);
   

if __name__=="__main__":
    main();