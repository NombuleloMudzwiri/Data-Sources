import xml.etree.ElementTree as ET

def count_favourites(movie_elements):
    count_fav = 0
    count_not_fav = 0

    for movie in movie_elements:
        is_favorite = movie.findtext("favorite")
        if is_favorite and is_favorite.lower() == "true":
            count_fav += 1
        else:
            count_not_fav += 1

    return count_fav, count_not_fav

def main():
    # Read in the movie.xml file
    tree = ET.parse("movie.xml")
    root = tree.getroot()

    # List all the child tags of the movie element
    movie_elements = root.findall("movie")
    
    if not movie_elements:
        print("No <movie> elements found in the XML file.")
        return

    print("Child tags of the movie element:")
    for child in movie_elements[0]:
        print(f"  - {child.tag}")

    # Use the itertext() function to print out the movie descriptions
    print("\nMovie Descriptions:")
    for movie in movie_elements:
        description = movie.findtext("description")
        if description:
            print(f"  - {description}")

    # Find the number of movies that are favourites and the number of movies that are not.
    count_fav, count_not_fav = count_favourites(movie_elements)
    print(f"\nNumber of movies that are your favourites: {count_fav}")
    print(f"Number of movies that are not your favourites: {count_not_fav}")

if __name__ == "__main__":
    main()
