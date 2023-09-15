import json

# List of books data as dictionaries
books_data = [
    {
        "title": "Door mat",
        "author": "James Brown",
        "year": 2000,
        "genre": "Fiction"
    },
    {
        "title": "Beautiful lie",
        "author": "Christina Camble",
        "year": 2015,
        "genre": "Mystery"
    },
    {
        "title": "Boss Baby",
        "author": "James Therone",
        "year": 1998,
        "genre": "Sci-Fi"
    },
    {
        "title": "Love-A four letter word",
        "author": "Austine Martin",
        "year": 2010,
        "genre": "Romance"
    },
    {
        "title": "Big Mamma",
        "author": "Luther Chris",
        "year": 2022,
        "genre": "Fantasy"
    },
    {
        "title": "House of fire",
        "author": "Clarence Drone",
        "year": 2005,
        "genre": "Thriller"
    }
]

# Write the books_data to the books.json file
with open("books.json", "w") as file:
    json.dump(books_data, file, indent=4)

print("books.json file has been created and populated with data.")
