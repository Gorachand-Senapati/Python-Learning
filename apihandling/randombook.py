import requests

def fetch_random_book():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    response = requests.get(url)

    datas = response.json()
    if datas["success"] and "data" in datas: 
        book_data = datas["data"]
        country = book_data["accessInfo"]["country"]
        accessViewStatus = book_data["accessInfo"]["accessViewStatus"]
        id = book_data["id"]
        return country, accessViewStatus,id
    else:
        raise Exception("Failed to fetch book data")

def main():
    try:
        country,accessViewStatus,id = fetch_random_book()
        print(f"Country: {country} \nAccess View Status: {accessViewStatus} \nID: {id}") #f-string is a way to format strings in Python. It allows you to embed expressions inside string literals, using curly braces {}. The expressions are evaluated at runtime and then formatted using the format() protocol. In this case, we are embedding the values of username, country, and coordinates into the string that will be printed to the console.
    except Exception as e:
        print(str(e))

if __name__ == "__main__": #__name__ is a special variable in Python that represents the name of the current module. When a Python file is run directly, __name__ is set to "__main__". This allows us to check if the script is being run directly or being imported as a module in another script. If it is run directly, we call the main() function to execute our code.
    main()