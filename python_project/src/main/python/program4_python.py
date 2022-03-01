#4. Write a program to reverse a string without using predefined functions?
def rev_strf(str):
    rev1 = ""
    for i in str:
        rev1 = i + rev1
    print(rev1)

def rev_strw(str):
    rev = ""
    count = len(str)
    while count > 0:
        rev = rev + str[count - 1]
        count = count - 1
    print(rev)

stri = input("Enter the string to be reversed: ")
rev_strf(stri)
rev_strw(stri)

