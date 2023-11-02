
//BOOK LIST
//Come back and fix syntax issues
$(document).ready(function) {
    //Fucntion to get and display all books
    function fetchAllBooks() {
        $.get('/books', function(data) {
            $('booksList').empty();
            data.forEach(book => {
                $('booksList').append('<li>${book.title</li>')
            })
        })
    }
}


//CART LIST
//Come back and fix syntax issues
$(document).ready(function) {
    //Fucntion to get and display all books
    function fetchAllBooksinCart() {
        $.get('/carts/', function(data) { //figure out how you want to save books in cart
            $('cartBookList').empty();
            data.forEach(book => {
                $('cartBookList').append('<li>${book.title</li>') //put the book title price
            })
        })
    }
}


//Call function to fetch books 
fetchAllBooks();

//Event listeners for both CART AND BOOK LIST