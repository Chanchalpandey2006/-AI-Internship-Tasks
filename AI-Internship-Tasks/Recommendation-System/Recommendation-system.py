 Recommendation System
# Content-Based Movie Recommendation

movies = {
    "3 Idiots": ["Comedy", "Drama"],
    "Chhichhore": ["Comedy", "Drama"],
    "Taare Zameen Par": ["Drama", "Education"],
    "Dangal": ["Sports", "Drama"],
    "Mary Kom": ["Sports", "Biography"],
    "Bhaag Milkha Bhaag": ["Sports", "Biography"],
    "Zindagi Na Milegi Dobara": ["Comedy", "Drama"],
    "Dil Chahta Hai": ["Comedy", "Drama"],
    "Yeh Jawaani Hai Deewani": ["Romance", "Drama"],
    "Wake Up Sid": ["Comedy", "Drama"],
    "Chak De India": ["Sports", "Drama"]
}


def recommend_movies(selected_movie):
    selected_genres = movies[selected_movie]

    recommendations = []

    for movie, genres in movies.items():
        if movie == selected_movie:
            continue

        common_genres = set(selected_genres).intersection(set(genres))

        if common_genres:
            recommendations.append(movie)

    return recommendations


print("===================================")
print("      MOVIE RECOMMENDATION SYSTEM")
print("===================================")

print("\nAvailable Movies:")

for movie in movies:
    print("-", movie)

while True:

    choice = input("\nEnter movie name (or type 'exit'): ")

    if choice.lower() == "exit":
        print("\nThank you for using the Recommendation System!")
        break

    if choice in movies:

        recommendations = recommend_movies(choice)

        print("\nRecommended Movies for you:")

        for movie in recommendations:
            print("-", movie)

    else:
        print("\nMovie not found!")
        print("Please enter a movie from the available list.")