def evenNos(no):
    no1=int(0);
    for i in range(0,no,1):
        print(no1,end=" ");
        no1=no1+2;

def main():
    no=int(input("Enter a number: "));
    evenNos(no);
   

if __name__=="__main__":
    main();