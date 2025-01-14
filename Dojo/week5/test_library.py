import pytest
from bibliotheque import Library

@pytest.fixture
def library_fixture():
    b = Library()
    b.add_book("Batman is back", "John Weak")
    b.add_book("Batman is testing", "Iam Back")
    print(b)
    return b

def test_add_book(library_fixture):
    print("Testing add_book method ...")
    library_fixture.add_book("Batman is dead", "Joker")
    book = library_fixture.search_book("batman is dead")
    assert book is not None
    assert book["title"] == "Batman is dead"
    assert book["author"] == "Joker"
    assert not book["borrowed"]

def test_search_book(library_fixture):
    print("Testing search_book method ...")
    book = library_fixture.search_book("batman is back")
    assert book is not None
    assert book["title"] == "Batman is back"
    assert book["author"] == "John Weak"
    assert not book["borrowed"]
    

def test_borrow_book(library_fixture):
    print("Testing borrow_book method ...")
    library_fixture.borrow_book("batman is back")
    book = library_fixture.search_book("batman is back")
    assert book["borrowed"]
    
    with pytest.raises(ValueError):
        library_fixture.borrow_book("batman is back")
        
    with pytest.raises(ValueError):
        library_fixture.borrow_book("Book doesn't exists")
    

def test_return_book(library_fixture):
    print("Testing return_book method ...")
    library_fixture.borrow_book("Batman is testing")
    library_fixture.return_book("Batman is testing")
    book = library_fixture.search_book("Batman is testing")
    assert not book["borrowed"]

    with pytest.raises(ValueError):
        library_fixture.return_book("Batman is testing")

    with pytest.raises(ValueError):
        library_fixture.return_book("Non-existent Book")
    print("return_book test passed.")

