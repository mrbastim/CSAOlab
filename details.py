def choose_detail(detail):
    details_tup = {"hood": 1, 
                "front door": 1.2, 
                "back door": 1.1, 
                "front  bumper": 1, 
                "back bumper": 1, 
                "roof": 1.1}
    return(details_tup[detail.lower()])

