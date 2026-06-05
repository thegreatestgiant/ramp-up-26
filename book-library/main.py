import schemas
from fastapi import FastAPI, HTTPException

app = FastAPI()

fakeDb = []
idNum = 0


@app.post("/books/")
def addBook(item: schemas.Book):
    global idNum
    book = {
        "id": idNum,
        "title": item.title,
        "author": item.author,
        "year": item.year,
    }
    fakeDb.append(book)
    idNum += 1
    return book


@app.get("/books")
def getBooks():
    return fakeDb


@app.get("/books/{id}")
def getBook(id: int):
    for book in fakeDb:
        if book["id"] is id:
            return book
    raise HTTPException(404, "Book not Found")


@app.put("/books/{id}")
def updateBook(id: int, item: schemas.Book):
    for idx, book in enumerate(fakeDb):
        if book["id"] is id:
            updatedBook = {
                "id": id,
                "title": item.title,
                "author": item.author,
                "year": item.year,
            }
            fakeDb[idx] = updatedBook
            return fakeDb[idx]
    raise HTTPException(404, "Book not Found")


@app.delete("/books/{id}")
def deleteBook(id: int):
    for book in fakeDb:
        if book["id"] == id:
            fakeDb.remove(book)
            return {"Removed the book"}
    raise HTTPException(404, "book not there to delete")
