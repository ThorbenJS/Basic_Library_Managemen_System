


import functions as func
from functions import hyodyton_latauspalkki

# Kutsutaan latauspalkkia
print("\n\n\n\n\nKäynnistetään ohjelmistoa...")

func.hyodyton_latauspalkki()
print("\nTervetuloa kirjastonhallintaohjelmistoon! Creator: Benjamin Sundell.")

# pistin copilotin lisäämään muutaman suositun kirjan valmiiksi tietokantaan(?) niin se ei ole ihan tyhjä alussa.
# Tän ohjelmiston tapauksessa tietokanta tarkoittaa vaan listaa kirjoista, jossa ns. kirja on sanakirjan muodossa.
book_database = [
    {"nimi": "To Kill a Mockingbird", "kirjailija": "Harper Lee", "julkaisuvuosi": 1960, "genre": "Fiction", "isbn": 9780061120084, "lainausstatus": False},
    {"nimi": "Go Set a Watchman", "kirjailija": "Harper Lee", "julkaisuvuosi": 2015, "genre": "Fiction", "isbn": 9780062409850, "lainausstatus": False},
    {"nimi": "The Catcher in the Rye", "kirjailija": "J.D. Salinger", "julkaisuvuosi": 1951, "genre": "Fiction", "isbn": 9780316769488, "lainausstatus": False},
    {"nimi": "Franny and Zooey", "kirjailija": "J.D. Salinger", "julkaisuvuosi": 1961, "genre": "Fiction", "isbn": 9780316769495, "lainausstatus": False},
    {"nimi": "The Hobbit", "kirjailija": "J.R.R. Tolkien", "julkaisuvuosi": 1937, "genre": "Fantasy", "isbn": 9780547928227, "lainausstatus": False},
    {"nimi": "The Lord of the Rings", "kirjailija": "J.R.R. Tolkien", "julkaisuvuosi": 1954, "genre": "Fantasy", "isbn": 9780618640157, "lainausstatus": False},
    {"nimi": "1984", "kirjailija": "George Orwell", "julkaisuvuosi": 1949, "genre": "Dystopian", "isbn": 9780451524935, "lainausstatus": False},
    {"nimi": "Animal Farm", "kirjailija": "George Orwell", "julkaisuvuosi": 1945, "genre": "Dystopian", "isbn": 9780451526342, "lainausstatus": False},
    {"nimi": "The Great Gatsby", "kirjailija": "F. Scott Fitzgerald", "julkaisuvuosi": 1925, "genre": "Fiction", "isbn": 9780743273565, "lainausstatus": False},
    {"nimi": "Tender Is the Night", "kirjailija": "F. Scott Fitzgerald", "julkaisuvuosi": 1934, "genre": "Fiction", "isbn": 9780684801544, "lainausstatus": False},
    {"nimi": "Pride and Prejudice", "kirjailija": "Jane Austen", "julkaisuvuosi": 1813, "genre": "Romance", "isbn": 9781503290563, "lainausstatus": False},
    {"nimi": "Sense and Sensibility", "kirjailija": "Jane Austen", "julkaisuvuosi": 1811, "genre": "Romance", "isbn": 9781503290556, "lainausstatus": False},
    {"nimi": "1984", "kirjailija": "George Orwell", "julkaisuvuosi": 1949, "genre": "Dystopian", "isbn": 9780451524935, "lainausstatus": False},
    {"nimi": "The Hobbit", "kirjailija": "J.R.R. Tolkien", "julkaisuvuosi": 1937, "genre": "Fantasy", "isbn": 9780547928227, "lainausstatus": False},
    {"nimi": "To Kill a Mockingbird", "kirjailija": "Harper Lee", "julkaisuvuosi": 1960, "genre": "Fiction", "isbn": 9780061120084, "lainausstatus": False}
]


# funktio jolla valitaan käyttäjämenu. Mukana errorcheckingiä jos käyttäjä syöttää jotain kelvotonta.
def choose_user():
    while True:
        try:
            print("\n\n|1| Kirjastonhoitaja")
            print("|2| Asiakas")
            print("|3| Sulje ohjelmisto")
            user = int(input("\nValitse käyttäjä tai sulje ohjelmisto: "))

            # Jos valinta ei ole 1 tai 2 tai 3 niin luodaan error ja looppi alkaa alusta virheviestin jälkeen
            if user != 1 and user != 2 and user!= 3:
                raise ValueError
            else:
                return user
        except ValueError:
            print("\nVääränlainen syöte, yritä uudelleen.")
            continue


# admin-looppi joka pyörittää ohjelmaa kirjastonhoitajan näkymässä.
def librarian_menu():

        while True:
            try:
                print("\n***************************************************")
                print("Toiminto |1|: Lisää kirja.")
                print("Toiminto |2|: Hae kirjaa.")
                print("Toiminto |3|: Muokkaa kirjan tietoja tai poista kirja.")
                print("Toiminto |4|: Avaa lista kaikista kirjoista.")
                print("Toiminto |5|: Takaisin käyttäjävalikkoon.")
                print("***************************************************")
                selection = int(input("\nValitse toiminto: "))
            # jos valinta ei ole jokin vaihtoehtoihin kuuluvista niin heitetään erroria.
                if selection != 1 and selection != 2 and selection != 3 and selection != 4 and selection != 5:
                    raise ValueError
            except ValueError:
                print("\nVääränlainen syöte, yritä uudelleen.")
                continue


            # kun halutaan lisätä kirja niin kysytään ensin käyttäjältä kaikki kirjan tiedot eli parametrit ja niillä parametreilla
        # add_book funktio luo uuden kirjan ja lisää sen kirjaston tietokantaan.
            if selection == 1:
                try:
                    title = input("Kirjan nimi: ")
                    author = input("Kirjailija: ")
                    year = int(input("Julkaisuvuosi: "))
                    genre = input("Genre: ")
                    isbn = int(input("ISBN: "))
                    loaned = False
                    book_database.append(func.add_book(title, author, year, genre, isbn, loaned))
                    func.print_book_database_2(book_database)
                except ValueError:
                    print("\n-------------------------------------")
                    print("Vääränlainen syöte, yritä uudelleen.")
                    print("-------------------------------------")
                    continue

        # kirjan hakeminen
            if selection == 2:
               searchword = input("\nHae kirjaa nimellä, kirjailijan nimellä, tai isbn-numerolla: ")
               hakutulos = func.search(searchword, book_database)
               if len(hakutulos) == 0:
                   print("\n-------------------------------------")
                   print("Hakua vastaavaa kirjaa ei löytynyt!")
                   print("-------------------------------------")
                   continue
               else:
                    print("\n-------------------------------------")
                    print(f"Seuraavat tulokset löytyivät:")
                    print("-------------------------------------")
                    # luodaan järkevämmän näkönen lista hakutuloksista käyttämällä indeksointia. Samanlainen for-looppi toistuu
                    # useemman kerran tässä ohjelmassa.
                    for i in range(len(hakutulos)):
                         print(f"|{i+1}|. {hakutulos[i]}")





        # kirjan muokkaaminen tai poistaminen
            if selection == 3:
                try:
                    searchword = input("\nHae muokattavaa kirjaa nimellä, kirjailijan nimellä, tai isbn-numerolla: ")
                    found_books = func.search(searchword, book_database)

                    if len(found_books) == 0:
                        print("\n-------------------------------------")
                        print("Hakua vastaavaa kirjaa ei löytynyt!")
                        print("-------------------------------------")
                        continue

                    else:
                        try:
                            print("\n-------------------------------------")
                            print(f"Seuraavat tulokset löytyivät:")
                            print("-------------------------------------\n")
                            for i in range(len(found_books)):
                                print(f"|{i+1}|. {found_books[i]}")
                            selected_book = int(input("\n Valitse listasta mitä kirjaa haluat muokata tai poistaa: "))
                            if selected_book > len(found_books) or selected_book < 1:
                                raise ValueError

                            delete_or_edit = int(input("Haluatko poistaa kirjan vai muokata kirjaa? (|1| = Poista, |2| = Muokkaa): "))

                            # jos käyttäjä valitsee |1|, niin poistetaan kirja tietokannasta.
                            if delete_or_edit == 1:
                                print(f"\nPOISTETAAN KIRJA: {found_books[selected_book - 1]}\n")
                                book_database.remove(found_books[selected_book - 1])
                                func.print_book_database_2(book_database)
                                print("\nKirja poistettu. Tietokanta päivitetty.")


                            # jos käyttäjä valitsee |2| eli muokkaa kirjaa niin annetaan uudet tiedot tai parametrit valitulle kirjalle eli muokataan sitö.
                            try:
                                if delete_or_edit == 2:
                                    print("\nMuokkaa kirjaa:")
                                    title = input("Kirjan nimi: ")
                                    author = input("Kirjailija: ")
                                    year = int(input("Julkaisuvuosi: "))
                                    genre = input("Genre: ")
                                    isbn = int(input("ISBN: "))
                                    edited_book = found_books[selected_book - 1]
                                    func.edit_book(edited_book, title, author, year, genre, isbn)
                                    func.print_book_database_2(book_database)
                                    print("Kirja muokattu. Tietokanta päivitetty.")

                                # errorchecking
                            except ValueError:
                                print("\n-------------------------------------")
                                print("Vääränlainen syöte, yritä uudelleen.")
                                print("-------------------------------------")
                                continue
                                #errorchecking
                            if delete_or_edit != 1 and delete_or_edit != 2:
                                print("\n-------------------------------------")
                                print("Vääränlainen syöte, yritä uudelleen.")
                                print("-------------------------------------")
                                continue
                            # errorchecking
                        except ValueError:
                            print("\n-------------------------------------")
                            print("Vääränlainen syöte, yritä uudelleen.")
                            print("-------------------------------------")
                            continue
                # jos käyttäjä valitsee listasta numeron jota ei ole niin heitetään erroria ja pistetään käyttäjä yrittämään uudelleen.
                except ValueError:
                    print("\n-------------------------------------")
                    print("Kelpaamaton valinta, yritä uudelleen.")
                    print("-------------------------------------")
                    continue
                # printtaa kaikki kirjat
            if selection == 4:
                func.print_book_database(book_database)

                # sulkee nykyisen menu loopin ja takaisin palaa käyttäjävalikkoon
            if selection == 5:
                break

# käyttäjämenu jossa on vähän rajoitetummat ominaisuudet
def customer_menu():
    while True:
        try:
            print("\n\n***************************************************")
            print("Toiminto |1|: Hae kirjaa.")
            print("Toiminto |2|: Avaa lista kaikista kirjoista.")
            print("Toiminto |3|: Lainaa kirja tai palauta kirja.")
            print("Toiminto |4|: Takaisin käyttäjävalikkoon.")
            print("***************************************************")
            selection = int(input("\nValitse toiminto: "))

            # jos valinta ei ole jokin vaihtoehtoihin kuuluvista niin heitetään erroria.
            if selection != 1 and selection != 2 and selection != 3 and selection != 4:
                raise ValueError

        except ValueError:
            print("\nVääränlainen syöte, yritä uudelleen.")
            continue

            # kun halutaan hakea kirja niin kysytään ensin käyttäjältä hakusana ja kutsutaan hakufunktiota
        if selection == 1:
            searchword: str = input("\nHae kirjaa nimellä, kirjailijan nimellä, tai isbn-numerolla: ")
            hakutulos_user = func.search(searchword, book_database)

            # tarkistetaan löytyykö kirjoja hakusanalla
            if len(hakutulos_user) == 0:
                print("\n-------------------------------------")
                print("Hakua vastaavaa kirjaa ei löytynyt!")
                print("-------------------------------------")
                continue
            else:
                print("\n-------------------------------------")
                print(f"Seuraavat tulokset löytyivät:")
                print("-------------------------------------\n")
                for i in range(len(hakutulos_user)):
                    print(f"|{i + 1}|. {hakutulos_user[i]}")

            # printtaa listan kaikista kirjoista
        if selection == 2:
            func.print_book_database(book_database)


        if selection == 3:
            searchword = input("\nHae lainattavaa kirjaa nimellä, kirjailijan nimellä, tai isbn-numerolla: ")
            found_books = func.search(searchword, book_database)
            try:
                # tarkistetaan löytyykö kirjoja hakusanalla
                if len(found_books) == 0:
                    print("\n-------------------------------------")
                    print("Hakua vastaavaa kirjaa ei löytynyt!")
                    print("-------------------------------------")
                    continue

                # jos löytyy niin tulostetaan lista kirjoista
                else:
                    print("\n-------------------------------------")
                    print(f"Seuraavat tulokset löytyivät:")
                    print("-------------------------------------")
                    for i in range(len(found_books)):
                        print(f"|{i + 1}|. {found_books[i]}")
                    selected_book = int(input("\n Valitse listasta minkä kirjan haluat lainata tai palauttaa: "))
                    # tarkistetaan onko syöte oikeanlainen
                    if selected_book > len(found_books) or selected_book < 1:
                        raise ValueError

                    # kysytään käyttäjältä haluaako lainata vai palauttaa kirjan
                    loan_or_return = int(input("Haluatko lainata kirjan vai palauttaa sen? (|1| = Lainaa, |2| = Palauta): "))

                    #tarkistetaan taas syöte ja heitetään erroria jos se ei ole oikeanlainen
                    if loan_or_return != 1 and loan_or_return != 2:
                        raise ValueError

                    # jos käyttäjä valitsee |1|, niin käyttäjä lainaa kirjan
                    if loan_or_return == 1:
                        print("\nVoit lainata kirjaa 30 päiväksi kerrallaan lainaushetkestä.")
                        print(f"\nLAINATAAN KIRJA: {found_books[selected_book - 1]}\n")

                        # tarkistetaan onko kirja jo lainassa
                        if found_books[selected_book - 1]["lainausstatus"] == True:
                            print("\nKirja on jo lainassa, et voi lainata sitä.")
                            continue
                        # jos ei ole lainassa niin muutetaan lainausstatus --> "True" ja lasketaan viimeinen palautuspäivä
                        else:
                            found_books[selected_book - 1]["lainausstatus"] = True
                            func.print_book_database_2(book_database)
                            print(f"\nValitsemasi kirja on lainattu {func.thirty_days_ahead()} asti.\n")

                    # jos käyttäjä valitsee |2| niin käyttäjä palauttaa valitun kirjan
                    if loan_or_return == 2:
                        print(f"\nPALAUTETAAN KIRJA: {found_books[selected_book - 1]}\n")
                        found_books[selected_book - 1]["lainausstatus"] = False
                        func.print_book_database_2(book_database)
                        print("\nOlet palauttanut kirjan. Tietokanta päivitetty.")

        # jos käyttäjä valitsee listasta numeron jota ei ole niin heitetään erroria ja pistetään käyttäjä yrittämään uudelleen.
            except ValueError:
                print("\n-------------------------------------")
                print("Vääränlainen valinta, yritä uudelleen.")
                print("-------------------------------------")
                continue

            # sulkee nykyisen menu loopin ja takaisin palaa käyttäjävalikkoon
        if selection == 4:
            break


# tämä on periaatteessa main looppi jonka sisällä kaikki tapahtuu. Esim. käyttäjävalikoidenkin loopit pyörivät tämän
# loopin sisällä. Ohjelma sulkeutuu kun tämä looppi katkaistaan.

while True:
    user = choose_user()
    if user == 1:
        librarian_menu()
    elif user == 2:
        customer_menu()

    # jos käyttäjän valinta on user = 3 niin looppi katkaistaan ja ohjelma sulkeutuu.
    elif user == 3:
        print("Suljetaan ohjelmistoa... Ethän sammuta tietokonetta.")
        hyodyton_latauspalkki()
        break

        # jos syötteeseen menee jotain sangen sopimatonta niin ohjelmisto rankaisee käyttäjää ja aloittaa loopin alusta.
    else:
        print("Vääränlainen syöte, yritä uudelleen.")
        continue