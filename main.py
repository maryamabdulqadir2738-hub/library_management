from library_management import book, user, transactions

book.add_book("Python Basics", "John Smith")
book.search_book("Python Basics")

user.add_user("Ahmed")
user.remove_user("Ahmed")

transactions.borrow_book("Ahmed", "Python Basics")
transactions.return_book("Ahmed", "Python Basics")