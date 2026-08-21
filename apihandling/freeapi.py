import requests #need requests module to make API calls

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response =requests.get(url) #which came store in response
    #all data in url is a string so convert is json because easy to handle it

    datas = response.json()
#if success and have data
    if datas["success"] and "data" in datas:
        user_data = datas["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]  
        coordinates =user_data ["location"]["coordinates"]["latitude"]
        return username,country,coordinates
    else:
        raise  Exception("failed to fetch user data")#error handling

def main():
    try:
        username, country, coordinates = fetch_random_user()
        print(f"Username:  {username} \nCountry: {country} \nCoordinates: {coordinates}") #f-string is a way to format strings in Python. It allows you to embed expressions inside string literals, using curly braces {}. The expressions are evaluated at runtime and then formatted using the format() protocol. In this case, we are embedding the values of username, country, and coordinates into the string that will be printed to the console.
    except Exception as e:
        print(str(e))

if __name__ == "__main__": #__name__ is a special variable in Python that represents the name of the current module. When a Python file is run directly, __name__ is set to "__main__". This allows us to check if the script is being run directly or being imported as a module in another script. If it is run directly, we call the main() function to execute our code.
    main()