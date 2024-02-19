
class Library :
    def __init__(self):
        self.file = open("books.txt","+a")

    def __del__(self):
        self.file.close()
    
    def list_books(self):
        self.file.seek(0)
        bookList = self.file.read().splitlines()

        if bookList == [] :
            print('The file is empty.')
        
        else:
            print('Book List :')
            for element in bookList:
                name,author,release_date,pages = element.strip().split(',')
                print(f"Book Title : {name}, Author : {author}")

    def add_book(self):
        name = input('Please enter a title:')
        author = input('Please enter an author:')
        release_date = input('Please enter a release date:')
        pages = input('Please enter number of pages:')

        newBook = f"{name},{author},{release_date},{pages}\n"
        self.file.write(newBook)
        print('The book is added in file.')

    def remove_book(self):
        self.file.seek(0)
        name = input('Please enter a name that will remove the file : ')

        bookList = self.file.read().splitlines()
        flag = 0
        i = 0
        for element in bookList:
            if name in element:
                index = i
                flag = 1
            i += 1
        if flag == 1:
            bookList.pop(index)
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(bookList)
            print('The book was removed.')
        else :
            print ('{name} is not exist.')


lib = Library()

str = '***MENU***\n1)List Books\n2)Add Book\n3)Remove Book\nPress q for exit.'

while(True):
    print(str)
    chr = input('Please enter a action : ')
    if chr == '1' :
        lib.list_books()
    elif chr =='2' : 
        lib.add_book()
    elif chr =='3' :
        lib.remove_book()
    elif chr == 'q' or chr == 'Q' :
        break;
    else :
        print('Entered wrong character:::')
