
class book:
    def __init__ (self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
book1 = book("1948", "Harper Lee")
print(book1)  # Output: '1948' by Harper Lee