import openpyxl as op


wbk = op.Workbook()


sheet = wbk.active
sheet.title = "Favorite People"

def main():

    people = []
    year_now = 2026


    for nick in range(1, 4):

        print(f"Person {nick}")

        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        birth_year = int(input("Enter birth year: "))


        age = year_now - birth_year

        people.append([nick, first_name, last_name, birth_year, age])

        print()


    header = ["ID", "First Name", "Last Name", "Birth Year", "Age"]
    sheet.append(header)

   
    for person in people:
        sheet.append(person)

    filename = "favorite_people.xlsx"
    wbk.save(filename)

    print("Favorite people saved successfully!")

    print("\n===== FAVORITE PEOPLE LIST =====")

    print(tuple(header))

    for person in people:
        print(tuple(person))

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()