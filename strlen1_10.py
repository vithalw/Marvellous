def strlen(name):
    count=int(0);
    for i in name:
        count=count+1;
    return count;    


def main():
   name=str(input("Enter a name: "));
   length=strlen(name);
   print("length is: ",length)


if __name__=="__main__":
    main();