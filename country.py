class India():
    def capital(self):  
        print("New delhi is the capital of India")

    def language(self):
        print("Hindi is the most widely spoken language of India")

    def type(self):
        print("India is a devloping country")

class Bangladesh():
    def capital(self):
        print("dhaka is the capital of India")

    def language(self):
        print("Bangla is the most widely spoken language of Bangladesh")

    def type(self):
        print("bangladesh is a devloping country")

objInd = India()
objbd = Bangladesh()

for country in (objInd, objbd):
    country.capital()
    country.language()
    country.type()

    print()        