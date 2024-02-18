class Library:
    def __init__(self,list_of_books):
        self.book = list_of_books

    def displayAvailablebooks(self):
        print("The Books present iin this library are: ")
        for book in self.book:
            print("\t *",book)

    def borrowBook(self,bookname):
        if bookname in self.book:
            print(f"You have been issued {bookname}. please keep it safe and return it within 30 days")
            self.book.remove(bookname)
            return True

        else:
            print("Sorry Book is issued already! plaease wait the book will return.")
            return False

    def returnBook(self,bookname):
        self.book.append(bookname)
        print("Thanks for returning this book, Hope you enjoyed!")

class Student:
    def requestBook(self):
        self.book=input("Enter the book name you want to borrow: ")
        return self.book

    def returntBook(self):
        self.book=input("Enter the book name you want to return: ")
        return self.book

if __name__ == '__main__':
    centralLibrary=Library(["Algorith","Python","DSA"])
    Student=Student()
    while(True):
        Welcoome='''
        =======Wlcome to the library!========
        please choose option
        1.List all books
        2.Request a book
        3.Return a book
        4.Exit
        '''
        print(Welcoome)
        a=int(input("Enter a choice: "))
        if a==1:
            centralLibrary.displayAvailablebooks()
        elif a==2:
            centralLibrary.borrowBook(Student.requestBook())
        elif a==3:
            centralLibrary.returnBook(Student.returntBook())
        elif a==4:
            print("Thanks for choosing central library")
            exit()
        else:
            print("invaild choice")


