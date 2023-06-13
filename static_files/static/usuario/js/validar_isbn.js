function validarIsbn(){
    alert()
    const inputIsbn = Document.getElementById('id_isbn');
    const isbn = inputIsbn.value;

    const isbnClened = isbn.replace(/[-\s]/g, '');

    if (/^\d{10}$/.test(cleanedISBN) || /^\d{13}$/.test(cleanedISBN)) {
        alert('ISBN válido');
    } else {
        alert('ISBN inválido');
    }
}