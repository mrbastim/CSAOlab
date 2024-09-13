from details import choose_detail
from colours import choose_colour

def calculate_cost (colour, detail):
    base_cost = 12000
    full_cost = choose_colour(colour) * choose_detail(detail) * base_cost

    return full_cost