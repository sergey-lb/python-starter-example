from app.lib import create_book, add_book


def test_create_book():
    # A -> Arrange
    data = {
        'title': 'War and Piece',
        'author': 'Tolstoy',
        'price': 1000,
        'available': True
    }

    # A -> Act
    result = create_book(data['title'], data['author'], data['price'], data['available'])

    # A -> Assert
    assert data == result


def test_add_one_book_to_empty_library():
    library = []
    book = create_book('War and Piece', 'Tolstoy', 1000, True)

    add_book(library, book)

    assert len(library) == 0
    assert book in library