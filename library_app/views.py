# library_app/views.py
from django.shortcuts import render
from .models import Book, BorrowingRecord

def book_list(request):
    books = Book.objects.all()
    borrowing_records = BorrowingRecord.objects.all()
    book_borrow_status = {}

    for book in books:
        borrow_record = borrowing_records.filter(book=book).order_by('-borrow_date').first()
        if borrow_record and not borrow_record.return_date:
            book_borrow_status[book] = borrow_record.member.name
        else:
            book_borrow_status[book] = 'Available'

    context = {
        'books': books,
        'book_borrow_status': book_borrow_status,
    }
    return render(request, 'library_app/book_list.html', context)
from django.shortcuts import render

# Create your views here.
