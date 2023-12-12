from flask import Flask, render_template, request
from TravelDestoMatcher import collect_user_preferences, initialize_destinations, find_best_destination

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recommendations', methods=['POST'])
def recommendations():
    user_preferences = collect_user_preferences()
    destinations = initialize_destinations()
    best_destinations = find_best_destination(user_preferences, destinations)

    top_destination = best_destinations[0][0]
    second_destination = best_destinations[1][0]
    third_destination = best_destinations[2][0]

    return render_template(
        'recommendations.html',
        top_destination=top_destination,
        second_destination=second_destination,
        third_destination=third_destination
    )


if __name__ == '__main__':
    app.run(debug=True)
