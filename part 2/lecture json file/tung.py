data = [
    [
            "Dhurandar 2",
            "Inside Out 2",
            "Super Mario Galaxy",
            "Transformers One",
            "Sonic 3"
    ],
    [
            "Beauty and the Beast",
            "IF",
            "Garfield",
            "Harry Potter",
            "K-Pop Demon Hunters"
        ],
    [
            "Honey, I Shrunk the Kids",
            "Love Insurance Company",
            "Mitchells vs The Machines",
            "Pushpa",
            "Super Mario"
        ],
     [
            "Harry Potter",
            "Iron Man",
            "Spider-Man",
            "Kalki",
            "Minions"
        ],
    [
            "Harry Potter",
            "IF",
            "LIK",
            "Pushpa",
            "Super Mario"
        ],
        [
            "Harry Potter",
            "Spider-Man",
            "LIK",
            "Minions",
            "Super Mario"
        ]
]

"super mario" in "super mario galaxy"
"super mario galaxy" in "super mario"
def get_possible_fav_movies(movie_name):
    result = [] 
    for person in data:
        flag = False # asuming it is not the possible fav movie list 
        for movie in person:
            if movie in movie_name or movie_name in movie:
                flag = True 
                break 
        if flag == True:
            result.append(person)
    return result 

def get_fav_movies_frequency(fav_movies,mv):
    frequency = dict({})
    for person in fav_movies:
        for movie in person:
            if movie in mv:
                continue
            if frequency.get(movie) == None:
                frequency[movie] = 0
            frequency[movie] += 1 
    return frequency

def print_recommendations(recommendations):
    print("Recommendations: ")
    for recommendation in recomendations[:5]:
        print(recommendation)
        if recomendations==0:
            print("No reccommendatiions for this film")

movie_name = input("Enter your fav movie: ")
possible_fav_movies = get_possible_fav_movies(movie_name)
frequency = get_fav_movies_frequency(possible_fav_movies,movie_name)
recomendations = sorted(frequency,key=lambda x:frequency[x] ,reverse=True)
print_recommendations(recomendations)
def disapproved_movies():
    recomendations = sorted(frequency,key=lambda x:frequency[x] ,reverse=False)
    print_recommendations(recomendations)
disapproved_movies()