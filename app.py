from flask import Flask, render_template, request
from TravelDestoMatcher import collect_user_preferences, initialize_destinations, find_best_destination

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['POST'])
def recommendations():
    if request.method == 'POST':
        user_preferences = {
            'budget': float(request.form['budget']),
            'activities': request.form['activities'].split(','),
            'climate_preference': request.form['climate_preference']
        }
        
        destinations = initialize_destinations()
        best_destinations = find_best_destination(user_preferences, destinations)
        
        return render_template('recommendations.html', best_destinations=best_destinations)

if __name__ == '__main__':
    app.run(debug=True)
