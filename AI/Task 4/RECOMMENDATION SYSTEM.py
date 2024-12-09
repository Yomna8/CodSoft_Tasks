import random

items_data = {
    'item_id': [
        # Movies
        101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120,
        # Anime
        201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220,
        # Music
        301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320,
        # Series
        401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420
    ],
    'title': [
        # Movies
        'The Matrix', 'The Godfather', 'Inception', 'Avengers', 'Titanic', 'Interstellar', 'Dune', 'Blade Runner 2049',
        'Mad Max: Fury Road', 'Gravity', 'The Dark Knight', 'Avatar', 'The Shawshank Redemption',
        'The Silence of the Lambs',
        'Forrest Gump', 'Inglourious Basterds', 'The Lion King', 'Pulp Fiction', 'Jaws', 'The Terminator',
        # Anime
        'Demon Slayer', 'Attack on Titan', 'My Hero Academia', 'Naruto', 'Death Note', 'One Punch Man', 'Bleach',
        'Dragon Ball Z', 'Hunter x Hunter', 'Tokyo Ghoul', 'Fullmetal Alchemist', 'One Piece', 'Sword Art Online',
        'JoJo\'s Bizarre Adventure', 'Cowboy Bebop', 'Bleach', 'Tokyo Revengers', 'Re:Zero', 'Fairy Tail',
        'Neon Genesis Evangelion',
        # Music
        'Bohemian Rhapsody', 'Shape of You', 'Blinding Lights', 'Imagine', 'Smells Like Teen Spirit',
        'Rolling in the Deep',
        'Bad Guy', 'Let It Be', 'Uptown Funk', 'Believer', 'Hurt', 'Lose Yourself', 'No Woman No Cry', 'Thunderstruck',
        'Stairway to Heaven', 'Take On Me', 'Sweet Child O\' Mine', 'Wonderwall', 'Beat It', 'Back in Black',
        'Take Five', 'Summertime',
        'Hallelujah', 'Lose Yourself', 'Electric Feel', 'Sicko Mode', 'Starboy', 'Get Lucky', 'Lose Control',
        'Billie Jean', 'Boogie Wonderland',
        # Series
        'Stranger Things', 'Breaking Bad', 'The Office', 'Money Heist', 'Narcos', 'The Witcher', 'The Mandalorian',
        'Loki', 'The Boys', 'Game of Thrones', 'The Crown', 'Peaky Blinders', 'Black Mirror', 'The Umbrella Academy',
        'Fargo', 'Chernobyl', 'The Haunting of Hill House', 'The Walking Dead', 'Mindhunter', 'Better Call Saul'
    ],
    'category': [
        # Categories
        'Movie', 'Movie', 'Movie', 'Movie', 'Movie', 'Movie', 'Movie', 'Movie', 'Movie', 'Movie', 'Movie', 'Movie',
        'Movie',
        'Movie', 'Movie', 'Movie', 'Movie', 'Movie', 'Movie', 'Movie',
        'Anime', 'Anime', 'Anime', 'Anime', 'Anime', 'Anime', 'Anime', 'Anime', 'Anime', 'Anime', 'Anime', 'Anime',
        'Anime', 'Anime', 'Anime', 'Anime', 'Anime', 'Anime', 'Anime', 'Anime',
        'Music', 'Music', 'Music', 'Music', 'Music', 'Music', 'Music', 'Music', 'Music', 'Music',
        'Music', 'Music', 'Music', 'Music', 'Music', 'Music', 'Music', 'Music', 'Music',
        'Series', 'Series', 'Series', 'Series', 'Series', 'Series', 'Series', 'Series', 'Series', 'Series',
        'Series', 'Series', 'Series', 'Series', 'Series', 'Series', 'Series', 'Series', 'Series', 'Series'
    ],
    'description': [
        # Descriptions for Movies, Anime, Music, and Series
        'A computer hacker learns about the true nature of reality and his role in it.',
        'The aging patriarch of an organized crime dynasty transfers control to his son.',
        'A thief with the ability to enter dreams takes on a dangerous mission.',
        'Superheroes team up to save the Earth from a catastrophic threat.',
        'A romance aboard the ill-fated Titanic.',
        'Explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.',
        'A noble family becomes embroiled in a conflict over a desert planet.',
        'A retired blade runner uncovers a secret that could plunge the world into chaos.',
        'In a post-apocalyptic world, a woman rebels against a tyrant to save lives.',
        'Astronauts struggle to survive after an accident in space leaves them stranded.',
        'Batman faces a chaotic adversary in the Joker.',
        'A paraplegic man explores the planet Pandora in a futuristic world.',
        'Two imprisoned men form a lasting bond as they share a dream of freedom.',
        'A psychiatrist battles the darkness of a cannibalistic serial killer.',
        'A man unexpectedly finds a life-changing friendship while fighting his way through life.',
        'Soldiers on a mission uncover hidden Nazi conspiracies during WWII.',
        'A lion cub learns the circle of life after the death of his father.',
        'Two hitmen cross paths with a briefcase, changing their fates forever.',
        'A killer shark terrorizes a beach town in a bid to feast on the summer crowds.',
        'A cyborg assassin has a mission to terminate humanity’s last hope.',
        'A young boy becomes a demon slayer after his family is killed by demons.',
        'Humans fight against giant creatures known as Titans to survive.',
        'A boy born without superpowers enrolls in a hero academy to become a symbol of peace.',
        'A high school student discovers a notebook that allows him to kill anyone by writing their name.',
        'A hero who can defeat anyone with one punch seeks a worthy opponent.',
        'A teenager gains soul reaper powers and protects humans from evil spirits.',
        'Saiyans and other powerful warriors fight for survival and honor.',
        'A young boy embarks on a journey to become a Hunter and find his missing father.',
        'A college student becomes part ghoul after a deadly encounter and struggles with his identity.',
        'A young alchemist searches for the Philosopher\'s Stone to undo a terrible mistake.',
        'A pirate sails the seas in search of the ultimate treasure, One Piece.',
        'Players get stuck in a virtual MMORPG where the stakes are life and death.',
        'A bizarre adventure through the generations unfolds for the Joestar family.',
        'A bounty hunter seeks redemption and forms unexpected bonds on the way.',
        'A delinquent travels through time to change the fate of his friends.',
        'A student is reincarnated in a world of magic and monster slaying.',
        'An epic adventure in a world where magic is real and dangerous.',
        'An artificial intelligence guides a young protagonist in a futuristic dystopian world.',
        'An iconic rock ballad that tells a story of life and loss by Queen.',
        'A heartfelt ballad by Ed Sheeran celebrating romance.',
        'An energetic pop song by The Weeknd about love and longing.',
        'An anthemic message for peace by John Lennon.',
        'A grunge rock classic by Nirvana, often regarded as an anthem of a generation.',
        'A powerful soul ballad about heartbreak by Adele.',
        'A catchy and dark pop anthem by Billie Eilish.',
        'A classic tune by The Beatles, offering hope and encouragement.',
        'A funky collaboration by Bruno Mars and Mark Ronson that became a global hit.',
        'A motivational anthem by Imagine Dragons about overcoming struggles.',
        'A smooth jazz classic by Dave Brubeck that has become an iconic piece.',
        'A soulful jazz ballad by George Gershwin that embodies timeless elegance.',
        'A classical masterpiece by Beethoven, celebrated for its deep emotion.',
        'An electronic dance track by Daft Punk known for its groovy beats.',
        'A catchy hip-hop anthem by Kendrick Lamar, rich in rhythm and rhyme.',
        'An electronic pop song by Daft Punk featuring The Weeknd.',
        'A popular dance song by Daft Punk, energetic and captivating.',
        'A disco anthem that brings vibrant energy to the dance floor.',
        'An emotive ballad by Leonard Cohen, often regarded as one of the greatest songs.',
        'A powerful rap song by Eminem from the film 8 Mile.',
        'A futuristic track by MGMT with a dreamy, electronic vibe.',
        'A rap anthem by Travis Scott that redefined modern hip-hop.',
        'A playful disco track by Daft Punk, featuring upbeat beats and catchy lyrics.',
        'A classic rock anthem by Michael Jackson.',
        'A classic funk song by Earth, Wind & Fire that brings joy and rhythm.',
        'A pop classic by The Beatles about freedom and peace.',
        'A timeless love song by The Beatles.'
    ],
    'genre': [
        # Genres: Movie, Anime, Music, Series
        'Sci-Fi', 'Crime', 'Sci-Fi', 'Action', 'Romance', 'Sci-Fi', 'Sci-Fi', 'Sci-Fi', 'Action', 'Drama', 'Action',
        'Adventure', 'Drama', 'Horror',
        'Drama', 'War', 'Animation', 'Drama', 'Drama', 'Thriller', 'Action', 'Action', 'Action', 'Comedy', 'Action',
        'Thriller', 'Drama', 'Adventure',
        'Action', 'Animation', 'Animation', 'Action', 'Action', 'Sci-Fi', 'Comedy', 'Action', 'Action', 'Sci-Fi',
        'Animation', 'Action', 'Action', 'Drama',
        'Action', 'Sci-Fi', 'Action', 'Action', 'Horror', 'Romance', 'Sci-Fi', 'Animation', 'Pop', 'Pop', 'Pop', 'Pop',
        'Rock', 'Pop', 'Pop', 'Pop', 'Rock',
        'Pop', 'Pop', 'Rock', 'Jazz', 'Pop', 'Jazz', 'Classical', 'Pop', 'Rap', 'Pop', 'Disco', 'Rap', 'Pop', 'Rap',
        'Disco', 'Pop', 'Pop', 'Pop', 'Rock',
        'Pop', 'Disco'
    ]
}


def get_category_choice():
    print("Select a category:")
    print("1. Movies")
    print("2. Anime")
    print("3. Music")
    print("4. Series")
    category_choice = input("Enter the number of your choice: ")
    try:
        category_choice = int(category_choice)
        if category_choice < 1 or category_choice > 4:
            raise ValueError("Invalid choice.")
    except ValueError as e:
        print(f"Error: {e}")
        return get_category_choice()
    return category_choice


def get_genre_choice(category_choice):
    print("\nSelect a genre:")
    genres = set()
    for i, cat in enumerate(items_data['category']):
        if category_choice == 1 and cat == 'Movie':
            genres.add(items_data['genre'][i])
        elif category_choice == 2 and cat == 'Anime':
            genres.add(items_data['genre'][i])
        elif category_choice == 3 and cat == 'Music':
            genres.add(items_data['genre'][i])
        elif category_choice == 4 and cat == 'Series':
            genres.add(items_data['genre'][i])

    genre_list = list(genres)
    for idx, genre in enumerate(genre_list, 1):
        print(f"{idx}. {genre}")

    genre_choice = input("Enter the number of your choice: ")
    try:
        genre_choice = int(genre_choice)
        if genre_choice < 1 or genre_choice > len(genre_list):
            raise ValueError("Invalid choice.")
    except ValueError as e:
        print(f"Error: {e}")
        return get_genre_choice(category_choice)
    return genre_list[genre_choice - 1]


def get_random_recommendation(category_choice, genre_choice):
    recommendations = []
    for i, cat in enumerate(items_data['category']):
        if category_choice == 1 and cat == 'Movie' and items_data['genre'][i] == genre_choice:
            recommendations.append(i)
        elif category_choice == 2 and cat == 'Anime' and items_data['genre'][i] == genre_choice:
            recommendations.append(i)
        elif category_choice == 3 and cat == 'Music' and items_data['genre'][i] == genre_choice:
            recommendations.append(i)
        elif category_choice == 4 and cat == 'Series' and items_data['genre'][i] == genre_choice:
            recommendations.append(i)

    random_index = random.choice(recommendations)
    return items_data['title'][random_index], items_data['description'][random_index]


def main():
    while True:
        category_choice = get_category_choice()
        genre_choice = get_genre_choice(category_choice)
        recommendation_title, recommendation_description = get_random_recommendation(category_choice, genre_choice)

        print(f"\nRecommended {genre_choice}: {recommendation_title}")
        print(f"Description: {recommendation_description}")

        try_again = input("\nWould you like to try again? (y/n): ").strip().lower()
        if try_again != 'y':
            print("Thank you for using the recommendation system!")
            break


if __name__ == "__main__":
    main()
