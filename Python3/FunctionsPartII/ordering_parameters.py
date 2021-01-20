def display_info(a, b, *args, student = "Norberto", **kwargs):
    return [a, b, args, student, kwargs]
    
print(display_info(1, 2, 3, last_name="Sanchez-Dichi", job="software engineer"))