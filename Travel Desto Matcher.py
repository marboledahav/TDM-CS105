def collect_user_preferences():
    print("Welcome to the Travel Destination Recommender!")

    while True:
        try:
            budget = float(input("Enter your budget for the trip: $"))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for the budget.")
    activities = input("Enter preferred activities (separated by commas): ").replace(' ', '').split(',')
    climate_preference = input("Enter climate preference (warm, cold, mild, etc.): ")
    
    preferences = {
        'budget': budget,
        'activities': activities,
        'climate_preference': climate_preference
    }
    
    return preferences



def initialize_destinations():
    destinations = [
        {
            'name': 'Paris',
            'location': 'France',
            'climate': 'mild',
            'activities': ['sightseeing', 'cultural tours', 'shopping', 'disneyland', 'concerts', 'eiffel tower'],
            'average_cost': 1500
        },
        {
            'name': 'Bali',
            'location': 'Indonesia',
            'climate': 'warm',
            'activities': ['beach', 'surfing', 'temples', 'swimming', 'hiking'],
            'average_cost': 1200
        },
        {
            'name': 'Tokyo',
            'location': 'Japan',
            'climate': 'mild',
            'activities': ['historical sites', 'shopping', 'culinary tours', 'disneyland', 'robotics', 'tokyo tower'],
            'average_cost': 1800
        },
        {
            'name': 'Cape Town',
            'location': 'South Africa',
            'climate': 'mild',
            'activities': ['wildlife safari', 'beach', 'hiking', 'museums', 'zoos', 'natural parks'],
            'average_cost': 1400
        },
        {
            'name': 'Rio de Janeiro',
            'location': 'Brazil',
            'climate': 'warm',
            'activities': ['beach', 'carnival', 'hiking', 'football', 'culinary tours'],
            'average_cost': 1300
        },
        {
            'name': 'Sydney',
            'location': 'Australia',
            'climate': 'mild',
            'activities': ['sightseeing', 'beach', 'wildlife tours', 'opera house', 'boat rides'],
            'average_cost': 1600
        },
        {
            'name': 'Amsterdam',
            'location': 'Netherlands',
            'climate': 'mild',
            'activities': ['canal cruises', 'museums', 'biking', 'legoland', 'clubbing'],
            'average_cost': 1400
        },
        {
            'name': 'Reykjavik',
            'location': 'Iceland',
            'climate': 'cold',
            'activities': ['northern lights tours', 'hot springs', 'glacier hiking'],
            'average_cost': 2000
        },
        {
            'name': 'Barcelona',
            'location': 'Spain',
            'climate': 'mild',
            'activities': ['architecture tours', 'beach', 'culinary tours', 'museums', 'football'],
            'average_cost': 1400
        },
        {
            'name': 'Bangkok',
            'location': 'Thailand',
            'climate': 'warm',
            'activities': ['culinary tours', 'temples', 'market tours', 'river cruises', 'natural parks'],
            'average_cost': 1100
        },
        {
            'name': 'Dubai',
            'location': 'United Arab Emirates',
            'climate': 'hot',
            'activities': ['desert safaris', 'shopping', 'luxury experiences', 'robotics', 'architecture tours', 'burj khalifa'],
            'average_cost': 2000
        },
        {
            'name': 'Florence',
            'location': 'Italy',
            'climate': 'mild',
            'activities': ['art', 'wine tours', 'museums', 'churches', 'gelato tasting'],
            'average_cost': 1700
        },
        {
            'name': 'Hawaii',
            'location': 'United States',
            'climate': 'warm',
            'activities': ['beach', 'volcano tours', 'hiking','fishing', 'Polynesian culture'],
            'average_cost': 1900
        },
        {
            'name': 'Marrakech',
            'location': 'Morocco',
            'climate': 'warm',
            'activities': ['desert safaris', 'souk shopping', 'camel rides', 'mosques', ],
            'average_cost': 1200
        },
        {
            'name': 'Oslo',
            'location': 'Norway',
            'climate': 'cold',
            'activities': ['fjord cruises', 'skiing', 'museums', 'opera house', 'viking culture'],
            'average_cost': 1800
        },
        {
            'name': 'Prague',
            'location': 'Czech Republic',
            'climate': 'mild',
            'activities': ['historic landmarks', 'beer tours', 'river cruises', 'zoos'],
            'average_cost': 1500
        },
        {
            'name': 'Santorini',
            'location': 'Greece',
            'climate': 'warm',
            'activities': ['sunsets', 'beach', 'wine tasting', 'kayaking', 'volcano tours'],
            'average_cost': 1600
        },
        {
            'name': 'Zurich',
            'location': 'Switzerland',
            'climate': 'mild',
            'activities': ['lake cruises', 'chocolate tasting', 'skiing', 'hiking', 'art'],
            'average_cost': 2000
        },
        {
            'name': 'Cairo',
            'location': 'Egypt',
            'climate': 'hot',
            'activities': ['pyramids visit', 'Nile cruises', 'market tours', 'desert safaris'],
            'average_cost': 1300
        },
        {
            'name': 'Edinburgh',
            'location': 'Scotland',
            'climate': 'mild',
            'activities': ['castle tours', 'whisky tastings', 'ghost tours', 'hiking', 'harry potter tours'],
            'average_cost': 1400
        },
        {
            'name': 'Kyoto',
            'location': 'Japan',
            'climate': 'mild',
            'activities': ['temples', 'traditional tea ceremonies', 'bamboo forest visits', 'culinary tours'],
            'average_cost': 1700
        },
        {
            'name': 'Las Vegas',
            'location': 'United States',
            'climate': 'hot',
            'activities': ['casinos', 'live entertainment', 'luxury experiences', 'clubbing'],
            'average_cost': 1800
        },
        {
            'name': 'Machu Picchu',
            'location': 'Peru',
            'climate': 'varied',
            'activities': ['hiking', 'historical exploration', 'scenic views'],
            'average_cost': 1600
        },
        {
            'name': 'New Zealand',
            'location': 'New Zealand',
            'climate': 'varied',
            'activities': ['sky diving', 'Maori culture', 'natural parks', 'fishing', 'snorkeling'],
            'average_cost': 1900
        },
        {
            'name': 'Seoul',
            'location': 'South Korea',
            'climate': 'mild',
            'activities': ['palace visits', 'street food tours', 'K-pop experiences'],
            'average_cost': 1500
        },
        {
            'name': 'Tahiti',
            'location': 'French Polynesia',
            'climate': 'warm',
            'activities': ['overwater bungalows', 'snorkeling', 'beach', 'fishing', 'diving', 'surfing'],
            'average_cost': 2000
        },
]
    return destinations
def calculate_score(user_preferences, destination):
    score = 0

    if destination['climate'].lower() == user_preferences['climate_preference'].lower():
        score += 2  # Adding weight to climate match

    matched_activities = sum(activity.lower() in destination['activities'] for activity in user_preferences['activities'])
    score += matched_activities  # Adding the count of matched activities
    
    if destination['average_cost'] <= user_preferences['budget']:
        score += 1  # Adding weight for budget within range
    
    return score


def find_best_destination(user_preferences, destinations):
    scores = []

    for destination in destinations:
        score = calculate_score(user_preferences, destination)
        scores.append((destination['name'], score))
    sorted_scores = sorted(scores, key = lambda x: x[1], reverse = True)
    top_destinations = sorted_scores[:3]
    return top_destinations


user_preferences = collect_user_preferences()
destinations = initialize_destinations()
best_destinations = find_best_destination(user_preferences, destinations)

print(f"The top destination according to your preferences is: {best_destinations[0][0]}")
print(f"Other destinations we recommend: {best_destinations[1][0]}, {best_destinations[2][0]}")