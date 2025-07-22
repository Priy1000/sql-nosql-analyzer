CREATE TABLE books (
  book_id INT PRIMARY KEY,
  title VARCHAR(100),
  author VARCHAR(100),
  genre VARCHAR(50),
  year INT
);

INSERT INTO books (book_id, title, author, genre, year) VALUES
(1, 'Samsara', 'Saksham Garg', 'Fantasy Fiction', 2022),
(2, 'Ikigai', 'Hector Gracia', 'Self Help', 2016),
(3, 'Harry Potter', 'J.K. Rowling', 'Fantasy', 1997),
(4, 'One Indian Girl', 'Chetan Bhagat', 'Fiction', 2016);
