def details_func(detail):
    details_tup = {"капот": 1, 
                "передняя дверь": 1.2, 
                "задняя дверь": 1.1, 
                "передний бампер": 1, 
                "задний бампер": 1, 
                "крыша": 1.1}
    return(details_tup[detail.lower()])

