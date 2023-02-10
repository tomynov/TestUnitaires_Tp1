import unittest
import sys
sys.path.append("C:\\Users\\Tom\\Desktop\\YnovParis\\Ynov2022\\TestUnitaires\\app")
from Exercice2 import Book, Client, Library

class TestBookMethods(unittest.TestCase):
    def test_check_out(self):
        # Test check_out method for a book
        book = Book("To Kill a Mockingbird", "Harper Lee")
        book.check_out()
        self.assertTrue(book.is_checked_out)

    def test_check_in(self):
        # Test check_in method for a book
        book = Book("To Kill a Mockingbird", "Harper Lee")
        book.check_out()
        book.check_in()
        self.assertFalse(book.is_checked_out)

class TestLibraryMethods(unittest.TestCase):
    def controlTest(self):
        self.library = Library()
        self.book1 = Book("To Kill a Mockingbird", "Harper Lee")
        self.book2 = Book("Pride and Prejudice", "Jane Austen")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_add_book(self):
        # Test add_book method for the library
        self.assertEqual(len(self.library.books), 2)

    def test_check_out_book(self):
        # Test check_out_book method for the library
        self.library.check_out_book("To Kill a Mockingbird")
        self.assertTrue(self.book1.is_checked_out)
        self.library.check_out_book("Pride and Prejudice")
        self.assertTrue(self.book2.is_checked_out)

    def test_check_in_book(self):
        # Test check_in_book method for the library
        self.library.check_out_book("To Kill a Mockingbird")
        self.library.check_in_book("To Kill a Mockingbird")
        self.assertFalse(self.book1.is_checked_out)
        self.library.check_out_book("Pride and Prejudice")
        self.library.check_in_book("Pride and Prejudice")
        self.assertFalse(self.book2.is_checked_out)

class TestClientMethods(unittest.TestCase):
    def controlTest(self):
        self.library = Library()
        self.book1 = Book("To Kill a Mockingbird", "Harper Lee")
        self.book2 = Book("Pride and Prejudice", "Jane Austen")
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.client = Client("John Doe")

    def test_check_out_book(self):
        # Test check_out_book method for a client
        self.client.check_out_book(self.library, "To Kill a Mockingbird")
        self.assertTrue(self.book1.is_checked_out)
        self.assertEqual(len(self.client.checked_out_books), 1)
        self.client.check_out_book(self.library, "Pride and Prejudice")
        self.client.check_in_book(self.library, "Pride and Prejudice")
        self.assertFalse(self.book2.is_checked_out)
        self.assertEqual(len(self.client.checked_out_books), 0)

    def test_check_in_book(self):
        # Test check_in_book method for a client
        self.client.check_out_book(self.library, "To Kill a Mockingbird")
        self.client.check_in_book(self.library, "To Kill a Mockingbird")
        self.assertFalse(self.book1.is_checked_out)
        self.assertEqual(len(self.client.checked_out_books), 0)

if __name__ == '__main__':
    unittest.main()