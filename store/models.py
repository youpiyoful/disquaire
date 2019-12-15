from django.db import models

# Create your models here.
ARTISTS = {
    'francis-cabrel': {'name': 'Francis Cabrel'},
    'lej': {'name': 'Elijay'},
    'Rosana': {'name': 'Rosana'}
}

ALBUMS = [
    {'name': 'Sarbacane', 'artists': [ARTISTS['francis-cabrel']]},
    {'name': 'La Dalle', 'artists': [ARTISTS['lej']]},
    {'name': 'Luna Nueva', 'artists': [ARTISTS['Rosana']]}
]