from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QVBoxLayout, QPushButton


def calculate():
    group = combo_group.currentText()
    duration = combo_duration.currentText()
    location = combo_location.currentText()
    wealth = combo_wealth.currentText()

    # Logik zur Berechnung der Vergütung für Vergütungsgruppe A
    if group == 'A':
        if duration == 'In den ersten drei Monaten':
            if location == 'stationäre Einrichtung':
                label_result.setText("Vergütung: 194,00 €" if wealth == 'mittellos' else "Vergütung: 200,00 €")
            else:
                label_result.setText("Vergütung: 208,00 €" if wealth == 'mittellos' else "Vergütung: 298,00 €")

        elif duration == 'Im vierten bis sechsten Monat':
            if location == 'stationäre Einrichtung':
                label_result.setText("Vergütung: 129,00 €" if wealth == 'mittellos' else "Vergütung: 158,00 €")
            else:
                label_result.setText("Vergütung: 170,00 €" if wealth == 'mittellos' else "Vergütung: 208,00 €")

        elif duration == 'Im siebten bis zwölften Monat':
            if location == 'stationäre Einrichtung':
                label_result.setText("Vergütung: 124,00 €" if wealth == 'mittellos' else "Vergütung: 140,00 €")
            else:
                label_result.setText("Vergütung: 151,00 €" if wealth == 'mittellos' else "Vergütung: 192,00 €")

        elif duration == 'Im 13. bis 24. Monat':
            if location == 'stationäre Einrichtung':
                label_result.setText("Vergütung: 87,00 €" if wealth == 'mittellos' else "Vergütung: 91,00 €")
            else:
                label_result.setText("Vergütung: 122,00 €" if wealth == 'mittellos' else "Vergütung: 158,00 €")

        elif duration == 'Ab dem 25. Monat':
            if location == 'stationäre Einrichtung':
                label_result.setText("Vergütung: 62,00 €" if wealth == 'mittellos' else "Vergütung: 78,00 €")
            else:
                label_result.setText("Vergütung: 105,00 €" if wealth == 'mittellos' else "Vergütung: 130,00 €")
    if group == 'B':
        if duration == 'In den ersten drei Monaten':
            label_result.setText(
                "Vergütung: 241,00 €" if wealth == 'mittellos' else "Vergütung: 249,00 €") if location == 'stationäre Einrichtung' else label_result.setText(
                "Vergütung: 258,00 €" if wealth == 'mittellos' else "Vergütung: 370,00 €")

        elif duration == 'Im vierten bis sechsten Monat':
            label_result.setText(
                "Vergütung: 158,00 €" if wealth == 'mittellos' else "Vergütung: 196,00 €") if location == 'stationäre Einrichtung' else label_result.setText(
                "Vergütung: 211,00 €" if wealth == 'mittellos' else "Vergütung: 258,00 €")

        elif duration == 'Im siebten bis zwölften Monat':
            label_result.setText(
                "Vergütung: 154,00 €" if wealth == 'mittellos' else "Vergütung: 174,00 €") if location == 'stationäre Einrichtung' else label_result.setText(
                "Vergütung: 188,00 €" if wealth == 'mittellos' else "Vergütung: 238,00 €")

        elif duration == 'Im 13. bis 24. Monat':
            label_result.setText(
                "Vergütung: 107,00 €" if wealth == 'mittellos' else "Vergütung: 113,00 €") if location == 'stationäre Einrichtung' else label_result.setText(
                "Vergütung: 151,00 €" if wealth == 'mittellos' else "Vergütung: 196,00 €")

        elif duration == 'Ab dem 25. Monat':
            label_result.setText(
                "Vergütung: 78,00 €" if wealth == 'mittellos' else "Vergütung: 96,00 €") if location == 'stationäre Einrichtung' else label_result.setText(
                "Vergütung: 130,00 €" if wealth == 'mittellos' else "Vergütung: 161,00 €")

    if group == 'C':
        if duration == 'In den ersten drei Monaten':
            label_result.setText(
                "Vergütung: 317,00 €" if wealth == 'mittellos' else "Vergütung: 327,00 €") if location == 'stationäre Einrichtung' else label_result.setText(
                "Vergütung: 339,00 €" if wealth == 'mittellos' else "Vergütung: 486,00 €")

        elif duration == 'Im vierten bis sechsten Monat':
            label_result.setText(
                "Vergütung: 208,00 €" if wealth == 'mittellos' else "Vergütung: 257,00 €") if location == 'stationäre Einrichtung' else label_result.setText(
                "Vergütung: 277,00 €" if wealth == 'mittellos' else "Vergütung: 339,00 €")

        elif duration == 'Im siebten bis zwölften Monat':
            label_result.setText(
                "Vergütung: 202,00 €" if wealth == 'mittellos' else "Vergütung: 229,00 €") if location == 'stationäre Einrichtung' else label_result.setText(
                "Vergütung: 246,00 €" if wealth == 'mittellos' else "Vergütung: 312,00 €")

        elif duration == 'Im 13. bis 24. Monat':
            label_result.setText(
                "Vergütung: 141,00 €" if wealth == 'mittellos' else "Vergütung: 149,00 €") if location == 'stationäre Einrichtung' else label_result.setText(
                "Vergütung: 198,00 €" if wealth == 'mittellos' else "Vergütung: 257,00 €")

        elif duration == 'Ab dem 25. Monat':
            label_result.setText(
                "Vergütung: 102,00 €" if wealth == 'mittellos' else "Vergütung: 127,00 €") if location == 'stationäre Einrichtung' else label_result.setText(
                "Vergütung: 171,00 €" if wealth == 'mittellos' else "Vergütung: 211,00 €")

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