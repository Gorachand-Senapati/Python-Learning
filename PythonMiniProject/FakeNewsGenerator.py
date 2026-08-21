import random

names=["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown", "Charlie Davis","Virat Kohli","Amitabh Bachchan","Shahrukh Khan","Salman Khan","Deepika Padukone","Priyanka Chopra","Ranveer Singh","Alia Bhatt","Katrina Kaif","Hrithik Roshan","virat kohli","sachin tendulkar","rohit sharma","ms dhoni","jasprit bumrah","ravindra jadeja","hardik pandya","ravichandran ashwin","yuzvendra chahal","shikhar dhawan","A group of Monkeys","A group of Lions","A group of Tigers","A group of Elephants","A group of Giraffes","A group of Zebras","A group of Kangaroos","A group of Penguins","A group of Dolphins","A group of Whales"]

actions = ["launches", "announces", "reveals", "introduces", "unveils", "discloses", "promises","declare a war on", "dance with"]

places = ["in New York", "in London", "in Paris", "in Tokyo", "in Sydney", "in Mumbai", "in Los Angeles","in Delhi","in Dubai","in Singapore","in Hong Kong","in Berlin","in Rome","in Madrid","in Toronto","in Chicago","in San Francisco","in Washington D.C.","in Beijing","in Shanghai","Ganga Ghat","Taj Mahal","Red Fort","Qutub Minar","Charminar","Gateway of India","India Gate","Lotus Temple","Hawa Mahal","Mysore Palace","Victoria Memorial","Golden Temple"]

while True:
    # FIXED: Only use one equals sign here!
    user_says = input("You need fake news headline: ").strip().lower()
    
    if user_says == "no":
        break
    elif user_says == "yes":
        ranName = random.choice(names)
        ranAction = random.choice(actions)
        ranPlaces = random.choice(places)
        headline = f"Breaking News: {ranName} {ranAction} {ranPlaces}"
        print("\n" + headline + "\n")
    

print("good Bye")

    