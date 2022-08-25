# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3


def cat_hat(str):
    a = 0
    b = 0
    while ("cat" in str):
        a += 1
        str = str.replace("cat", "", 1)
    while ("hat" in str):
        b += 1
        str = str.replace("hat", "", 1)
    if a == b:
        return True
    else:
        return False


def main():
    # testcases=int(input()) #testcases
    # while(testcases>0):
    str = input()
    print(cat_hat(str))
    # testcases-=1


if __name__ == '__main__':
    main()
