class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if hasattr(self, "title"):
            print("Title cannot be chnaged!")
        elif (len(value) <= 5):
            print("Title is too short")
        elif (len(value) >= 50):
            print("Title is too long")
        else:
            self._title = value
    
class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass

author = Author("Carry Bradshaw")
magazine = Magazine("Vogue", "Fashion")
article_1 = Article(author, magazine, "How")

