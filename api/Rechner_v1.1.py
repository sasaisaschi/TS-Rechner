from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QVBoxLayout, QPushButton

def calculate():
    group = combo_group.currentText()
    duration = combo_duration.currentText()
    location = combo_location.currentText()
    wealth = combo_wealth.currentText()

    # Define a dictionary to map the values of group, duration, location, and wealth to their corresponding Vergütung values
    vergutung_dict = {
        ('A', 'In den ersten drei Monaten', 'stationäre Einrichtung', 'mittellos'): "Vergütung: 194,00 €",
        ('A', 'In den ersten drei Monaten', 'stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 200,00 €",
        ('A', 'In den ersten drei Monaten', 'nicht stationäre Einrichtung', 'mittellos'): "Vergütung: 208,00 €",
        ('A', 'In den ersten drei Monaten', 'nicht stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 298,00 €",
        ('A', 'Im vierten bis sechsten Monat', 'stationäre Einrichtung', 'mittellos'): "Vergütung: 129,00 €",
        ('A', 'Im vierten bis sechsten Monat', 'stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 158,00 €",
        ('A', 'Im vierten bis sechsten Monat', 'nicht stationäre Einrichtung', 'mittellos'): "Vergütung: 170,00 €",
        ('A', 'Im vierten bis sechsten Monat', 'nicht stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 208,00 €",
        ('A', 'Im siebten bis zwölften Monat', 'stationäre Einrichtung', 'mittellos'): "Vergütung: 124,00 €",
        ('A', 'Im siebten bis zwölften Monat', 'stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 140,00 €",
        ('A', 'Im siebten bis zwölften Monat', 'nicht stationäre Einrichtung', 'mittellos'): "Vergütung: 151,00 €",
        ('A', 'Im siebten bis zwölften Monat', 'nicht stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 192,00 €",
        ('A', 'Im 13. bis 24. Monat', 'stationäre Einrichtung', 'mittellos'): "Vergütung: 87,00 €",
        ('A', 'Im 13. bis 24. Monat', 'stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 91,00 €",
        ('A', 'Im 13. bis 24. Monat', 'nicht stationäre Einrichtung', 'mittellos'): "Vergütung: 122,00 €",
        ('A', 'Im 13. bis 24. Monat', 'nicht stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 158,00 €",
        ('A', 'Ab dem 25. Monat', 'stationäre Einrichtung', 'mittellos'): "Vergütung: 62,00 €",
        ('A', 'Ab dem 25. Monat', 'stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 78,00 €",
        ('A', 'Ab dem 25. Monat', 'nicht stationäre Einrichtung', 'mittellos'): "Vergütung: 105,00 €",
        ('A', 'Ab dem 25. Monat', 'nicht stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 130,00 €",
        ('B', 'In den ersten drei Monaten', 'stationäre Einrichtung', 'mittellos'): "Vergütung: 241,00 €",
        ('B', 'In den ersten drei Monaten', 'stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 249,00 €",
        ('B', 'In den ersten drei Monaten', 'nicht stationäre Einrichtung', 'mittellos'): "Vergütung: 258,00 €",
        ('B', 'In den ersten drei Monaten', 'nicht stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 370,00 €",
        ('B', 'Im vierten bis sechsten Monat', 'stationäre Einrichtung', 'mittellos'): "Vergütung: 158,00 €",
        ('B', 'Im vierten bis sechsten Monat', 'stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 196,00 €",
        ('B', 'Im vierten bis sechsten Monat', 'nicht stationäre Einrichtung', 'mittellos'): "Vergütung: 211,00 €",
        ('B', 'Im vierten bis sechsten Monat', 'nicht stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 258,00 €",
        ('B', 'Im siebten bis zwölften Monat', 'stationäre Einrichtung', 'mittellos'): "Vergütung: 154,00 €",
        ('B', 'Im siebten bis zwölften Monat', 'stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 174,00 €",
        ('B', 'Im siebten bis zwölften Monat', 'nicht stationäre Einrichtung', 'mittellos'): "Vergütung: 188,00 €",
        ('B', 'Im siebten bis zwölften Monat', 'nicht stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 238,00 €",
        ('B', 'Im 13. bis 24. Monat', 'stationäre Einrichtung', 'mittellos'): "Vergütung: 107,00 €",
        ('B', 'Im 13. bis 24. Monat', 'stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 113,00 €",
        ('B', 'Im 13. bis 24. Monat', 'nicht stationäre Einrichtung', 'mittellos'): "Vergütung: 151,00 €",
        ('B', 'Im 13. bis 24. Monat', 'nicht stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 196,00 €",
        ('B', 'Ab dem 25. Monat', 'stationäre Einrichtung', 'mittellos'): "Vergütung: 78,00 €",
        ('B', 'Ab dem 25. Monat', 'stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 96,00 €",
        ('B', 'Ab dem 25. Monat', 'nicht stationäre Einrichtung', 'mittellos'): "Vergütung: 130,00 €",
        ('B', 'Ab dem 25. Monat', 'nicht stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 161,00 €",
        ('C', 'In den ersten drei Monaten', 'stationäre Einrichtung', 'mittellos'): "Vergütung: 317,00 €",
        ('C', 'In den ersten drei Monaten', 'stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 327,00 €",
        ('C', 'In den ersten drei Monaten', 'nicht stationäre Einrichtung', 'mittellos'): "Vergütung: 339,00 €",
        ('C', 'In den ersten drei Monaten', 'nicht stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 486,00 €",
        ('C', 'Im vierten bis sechsten Monat', 'stationäre Einrichtung', 'mittellos'): "Vergütung: 208,00 €",
        ('C', 'Im vierten bis sechsten Monat', 'stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 257,00 €",
        ('C', 'Im vierten bis sechsten Monat', 'nicht stationäre Einrichtung', 'mittellos'): "Vergütung: 277,00 €",
        ('C', 'Im vierten bis sechsten Monat', 'nicht stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 339,00 €",
        ('C', 'Im siebten bis zwölften Monat', 'stationäre Einrichtung', 'mittellos'): "Vergütung: 202,00 €",
        ('C', 'Im siebten bis zwölften Monat', 'stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 229,00 €",
        ('C', 'Im siebten bis zwölften Monat', 'nicht stationäre Einrichtung', 'mittellos'): "Vergütung: 246,00 €",
        ('C', 'Im siebten bis zwölften Monat', 'nicht stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 312,00 €",
        ('C', 'Im 13. bis 24. Monat', 'stationäre Einrichtung', 'mittellos'): "Vergütung: 141,00 €",
        ('C', 'Im 13. bis 24. Monat', 'stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 149,00 €",
        ('C', 'Im 13. bis 24. Monat', 'nicht stationäre Einrichtung', 'mittellos'): "Vergütung: 198,00 €",
        ('C', 'Im 13. bis 24. Monat', 'nicht stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 257,00 €",
        ('C', 'Ab dem 25. Monat', 'stationäre Einrichtung', 'mittellos'): "Vergütung: 102,00 €",
        ('C', 'Ab dem 25. Monat', 'stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 127,00 €",
        ('C', 'Ab dem 25. Monat', 'nicht stationäre Einrichtung', 'mittellos'): "Vergütung: 171,00 €",
        ('C', 'Ab dem 25. Monat', 'nicht stationäre Einrichtung', 'nicht mittellos'): "Vergütung: 211,00 €"
    }

    # Get the corresponding Vergütung value from the dictionary
    vergutung = vergutung_dict.get((group, duration, location, wealth))

    # Set the label_result text to the Vergütung value
    label_result.setText(vergutung)

app = QApplication([])

window = QWidget()
layout = QVBoxLayout()

combo_group = QComboBox()
combo_group.addItems(['A', 'B', 'C'])
layout.addWidget(QLabel('Vergütungsgruppe:'))
layout.addWidget(combo_group)

combo_duration = QComboBox()
combo_duration.addItems(
    ['In den ersten drei Monaten', 'Im vierten bis sechsten Monat', 'Im siebten bis zwölften Monat',
     'Im 13. bis 24. Monat', 'Ab dem 25. Monat'])
layout.addWidget(QLabel('Dauer der Betreuung:'))
layout.addWidget(combo_duration)

combo_location = QComboBox()
combo_location.addItems(['stationäre Einrichtung', 'andere Wohnform'])
layout.addWidget(QLabel('Gewöhnlicher Aufenthaltsort:'))
layout.addWidget(combo_location)

combo_wealth = QComboBox()
combo_wealth.addItems(['mittellos', 'nicht mittellos'])
layout.addWidget(QLabel('Vermögensstatus:'))
layout.addWidget(combo_wealth)

button_calculate = QPushButton('Berechnen')
button_calculate.clicked.connect(calculate)
layout.addWidget(button_calculate)

label_result = QLabel('Vergütung: ')
layout.addWidget(label_result)

window.setLayout(layout)
window.show()

app.exec_()