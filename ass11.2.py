class Publication:
    def __init__(self, publication_name):
        self.publication_name=publication_name

    def print_information(self):
        print(f"The publication name is {self.publication_name}")

class Book(Publication):
    def __init__(self, publication_name,author,page_count):
        self.author=author
        self.page_count=page_count
        super().__init__(publication_name)

    def print_information(self):
        super().print_information()
        print(f"author:{self.author}  page count:{self.page_count} pages")

class Magazine(Publication):
    def __init__(self, publication_name,cheif, page_count):
        self.cheif=cheif
        self.page_count = page_count
        super().__init__(publication_name)

    def print_information(self):
        super().print_information()
        print(f"cheif:{self.cheif}  page count:{self.page_count} pages")

magazine1=Magazine("Donald Duck","Aki Hyyppä",None)
Magazine.print_information(magazine1)
book1=Book("Compartment No.6","Rosa Liksom",192 )
Book.print_information(book1)