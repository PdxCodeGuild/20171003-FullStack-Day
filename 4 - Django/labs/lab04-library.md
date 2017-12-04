
# Lab 4: Library

Let's create an application for representing a library. You should have two models (below) and a page for users to check out and check in books. You can enter the book and author information using the admin panel.

- Book: a model representing a book, with a title, publish date, and an author (foreign key)
- Author: a model representing an author of a book, one author can have multiple books


## Version 2

Add another model to keep track of who checked out a book and when. When a user checks a book back in, record that too. Add a text input on the 'checkout' page to record the name of who checked out the book. Have a page to show all the checkouts and returns.

The new model can have the following fields:

- book: the book that the user checked out or checked in
- user: a text field containing the name of the user that checked out or checked in the book
- checkout: a boolean indicating whether the book was checked out or checked in
- timestamp: a datetime that records when the book was checked out or in
