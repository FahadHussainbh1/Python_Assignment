class Book :
    title = "The Book"
    auther = "Fahad Hussain"
    pages = 300


    def Describe(self,title,auther,pages):
        self.title = title
        self.auther = auther
        self.pages = pages
        print("The title of book", title,"written by",auther,"and total pages is",pages)


about =Book()
about.Describe("The Book","Fahad",300)
print()
about.Describe("Second Book","Hussain",400)
print()
about.Describe("Third Book","ali",500)