def choose_colour(colour):
    colours = {'white': 1,
            'blue': 1,
            'yellow': 1.1,
            'red': 1,
            'pearl': 1.2,
            'metallic grey': 1.3 
    }

    return colours.get(colour.lower())

