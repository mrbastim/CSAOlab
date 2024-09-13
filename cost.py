def calculate_cost (color, detail):
    base_cost = 12000
    full_cost = choose_color(color) * choose_detail(detail) * base_cost

    return full_cost