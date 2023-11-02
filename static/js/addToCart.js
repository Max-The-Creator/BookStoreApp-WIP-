export const addToCart = () => {
    $('#addToCartBtn').click(function() {
        $.post('/carts/'), {book_id: book_id}, function() {
            alert("Book Added to Cart!");
            fetchCartList(); // This refereshes the cart after you add an item
            
        } //Figure out what to call this in the cart
        .fail(function(errorThrown)) {
            alert("Error: Book could not be added" + errorThrown)
        }
    })
}