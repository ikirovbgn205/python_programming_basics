book = input()

searched_books = 0
is_found = False

current_book = input()

while current_book != 'No More Books':

    if current_book == book:
        is_found = True
        print(f'You checked {searched_books} books and found it.')
        break

    searched_books += 1
    current_book = input()

if not is_found:
    print(f'The book you search is not here!')
    print(f'You checked {searched_books} books.')
