
# Funktio jolla voi luoda uuden kirjan ja lisätä sen kirjaston tietokantaan.
def add_book(title, author, year, genre, isbn, loaned):
    book = {
        "nimi" : title,
        "kirjailija" : author,
        "julkaisuvuosi" : year,
        "genre" : genre,
        "isbn" : isbn,
        "lainausstatus" : loaned # oletuksena kirja ei ole lainassa.
    }
    return book



# iteroidaan läpi kaikki databasen kirjat ja niiden arvot ja avaimet ja etsitään osuuko jokin niistä hakusanaan
def search(searchword, book_database):
    found_books = []
    for item in book_database:
        for key, value in item.items():
            # poisluetaan ne avaimet joilla ei voi hakea kirjaa
            if key == "julkaisuvuosi" or key == "genre":
                pass
            if str(searchword).lower() == str(value).lower():
                found_books.append(item)

    return found_books # palautetaan lista hakusanalla löydetyistä kirjoista.


# funktio jolla muokataan halutun kirjan tietoja. Päivittyy suoraan kirjojen tietokantaan "book_database".
def edit_book(edited_book, title, author, year, genre, isbn):
    edited_book["nimi"] = title
    edited_book["kirjailija"] = author
    edited_book["julkaisuvuosi"] = year
    edited_book["genre"] = genre
    edited_book["isbn"] = isbn
    return edited_book


# funktio joka printtaa kaikki tietokannassa olevat kirjat.
def print_book_database(book_database):
    try:
        import json
        #tulostetaan sanakirjojen eli "kirjojen" lista.
        for i in range(len(book_database)):
            print(f"|{i+1}|. {book_database[i]}")
        print("\nTarkastele yksittäisen kirjan tietoja syöttämällä krijan numero listasta.\n")
        selection = int(input("\nSyötä kirjan numero: "))

        # tarkistetaan onko syöte oikeanlainen
        if selection > len(book_database) or selection < 1:
            print("Vääränlainen syöte. Yritä uudelleen.")
            return print_book_database(book_database)
        else:
            #tulostetaan valitun kirjan tiedot json-muodossa jotta näyttää vähäh selkeämmältä
            selected_book = book_database[selection - 1]
            print(json.dumps(selected_book, indent=4))
    # syötteen errorchecking
    except ValueError:
        print("Vääränlainen syöte. Yritä uudelleen.")
        return print_book_database(book_database)

# tulostaa listan krijoista ilman mitään ylimääräsiä toimintoja
def print_book_database_2(book_database):
    for i in range(len(book_database)):
        print(f"|{i + 1}|. {book_database[i]}")


# Simmuloitu latauspalkki. Hieno graafinen ominaisuus jolla ei ole mitään käytännöllistä merkitystä.
def hyodyton_latauspalkki():
    import time
    # importataan time-moduuli jotta voidaan luoda ikkään kuin ajastin jolla simuloidaan latausta.
    for i in range(1, 101):
        # ajastin joka oottaa x määrän sekuntia ennen kun se tulostaa seuraavan palkin. (Tulostaa yhteensä 100 kertaa)
        time.sleep(0.018)
        print(f"\r[{i * '█'}{(100 - i) * ' '}] {i}%", end="")


def thirty_days_ahead():
    #importataan aikamoduuli jolla voidaan laskea päivämäärä 30 päivää eteenpäin nykyisestä ajasta
    from datetime import datetime, timedelta
    # haetaan nykyinen aika
    current_date = datetime.now()
    # lasketaan 30 päivää eteenpäin nykyisestä ajasta
    future_date = current_date + timedelta(days=30)
    # viimeiseks muotoillaan päivämäärä haluttuun muotoon
    formatted_date = future_date.strftime("%d.%m.%Y")
    return formatted_date

