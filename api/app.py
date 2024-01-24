from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        group = request.form.get('group')
        duration = request.form.get('duration')
        location = request.form.get('location')
        wealth = request.form.get('wealth')
        # Hier kommt die Logik zur Berechnung der Vergütung
        result = calculate_compensation(group, duration, location, wealth)
    else:
        group = duration = location = wealth = result = None

    return render_template('index.html', result=result, selected={'group': group, 'duration': duration, 'location': location, 'wealth': wealth})

def calculate_compensation(group, duration, location, wealth):
    # Logik zur Berechnung der Vergütung
    if group == 'A':
        if duration == 'In den ersten drei Monaten':
            if location == 'stationäre Einrichtung':
                return "Vergütung: 194,00 €" if wealth == 'mittellos' else "Vergütung: 200,00 €"
            else:
                return "Vergütung: 208,00 €" if wealth == 'mittellos' else "Vergütung: 298,00 €"
        elif duration == 'Im vierten bis sechsten Monat':
            if location == 'stationäre Einrichtung':
                return "Vergütung: 129,00 €" if wealth == 'mittellos' else "Vergütung: 158,00 €"
            else:
                return "Vergütung: 170,00 €" if wealth == 'mittellos' else "Vergütung: 208,00 €"
        elif duration == 'Im siebten bis zwölften Monat':
            if location == 'stationäre Einrichtung':
                return "Vergütung: 124,00 €" if wealth == 'mittellos' else "Vergütung: 140,00 €"
            else:
                return "Vergütung: 151,00 €" if wealth == 'mittellos' else "Vergütung: 192,00 €"
        elif duration == 'Im 13. bis 24. Monat':
            if location == 'stationäre Einrichtung':
                return "Vergütung: 87,00 €" if wealth == 'mittellos' else "Vergütung: 91,00 €"
            else:
                return "Vergütung: 122,00 €" if wealth == 'mittellos' else "Vergütung: 158,00 €"
        elif duration == 'Ab dem 25. Monat':
            if location == 'stationäre Einrichtung':
                return "Vergütung: 62,00 €" if wealth == 'mittellos' else "Vergütung: 78,00 €"
            else:
                return "Vergütung: 105,00 €" if wealth == 'mittellos' else "Vergütung: 130,00 €"
    # Fügen Sie hier Bedingungen für weitere Gruppen hinzu, falls erforderlich

    elif group == 'B':
        if duration == 'In den ersten drei Monaten':
            if location == 'stationäre Einrichtung':
                return "Vergütung: 241,00 €" if wealth == 'mittellos' else "Vergütung: 249,00 €"
            else:
                return "Vergütung: 258,00 €" if wealth == 'mittellos' else "Vergütung: 370,00 €"
        elif duration == 'Im vierten bis sechsten Monat':
            if location == 'stationäre Einrichtung':
                return "Vergütung: 158,00 €" if wealth == 'mittellos' else "Vergütung: 196,00 €"
            else:
                return "Vergütung: 211,00 €" if wealth == 'mittellos' else "Vergütung: 258,00 €"
        elif duration == 'Im siebten bis zwölften Monat':
            if location == 'stationäre Einrichtung':
                return "Vergütung: 154,00 €" if wealth == 'mittellos' else "Vergütung: 174,00 €"
            else:
                return "Vergütung: 188,00 €" if wealth == 'mittellos' else "Vergütung: 238,00 €"
        elif duration == 'Im 13. bis 24. Monat':
            if location == 'stationäre Einrichtung':
                return "Vergütung: 107,00 €" if wealth == 'mittellos' else "Vergütung: 113,00 €"
            else:
                return "Vergütung: 151,00 €" if wealth == 'mittellos' else "Vergütung: 196,00 €"
        elif duration == 'Ab dem 25. Monat':
            if location == 'stationäre Einrichtung':
                return "Vergütung: 78,00 €" if wealth == 'mittellos' else "Vergütung: 96,00 €"
            else:
                return "Vergütung: 130,00 €" if wealth == 'mittellos' else "Vergütung: 161,00 €"

    elif group == 'C':
        if duration == 'In den ersten drei Monaten':
            if location == 'stationäre Einrichtung':
                return "Vergütung: 317,00 €" if wealth == 'mittellos' else "Vergütung: 327,00 €"
            else:
                return "Vergütung: 339,00 €" if wealth == 'mittellos' else "Vergütung: 486,00 €"
        elif duration == 'Im vierten bis sechsten Monat':
            if location == 'stationäre Einrichtung':
                return "Vergütung: 208,00 €" if wealth == 'mittellos' else "Vergütung: 257,00 €"
            else:
                return "Vergütung: 277,00 €" if wealth == 'mittellos' else "Vergütung: 339,00 €"
        elif duration == 'Im siebten bis zwölften Monat':
            if location == 'stationäre Einrichtung':
                return "Vergütung: 202,00 €" if wealth == 'mittellos' else "Vergütung: 229,00 €"
            else:
                return "Vergütung: 246,00 €" if wealth == 'mittellos' else "Vergütung: 312,00 €"
        elif duration == 'Im 13. bis 24. Monat':
            if location == 'stationäre Einrichtung':
                return "Vergütung: 141,00 €" if wealth == 'mittellos' else "Vergütung: 149,00 €"
            else:
                return "Vergütung: 198,00 €" if wealth == 'mittellos' else "Vergütung: 257,00 €"
        elif duration == 'Ab dem 25. Monat':
            if location == 'stationäre Einrichtung':
                return "Vergütung: 102,00 €" if wealth == 'mittellos' else "Vergütung: 127,00 €"
            else:
                return "Vergütung: 171,00 €" if wealth == 'mittellos' else "Vergütung: 211,00 €"

        return "Keine gültige Auswahl"


if __name__ == '__main__':
    app.run(debug=True)
