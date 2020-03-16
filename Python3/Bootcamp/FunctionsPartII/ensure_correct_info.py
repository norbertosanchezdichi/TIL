def ensure_correct_info(*args):
    if 'Norberto' in args and 'Sanchez-Dichi' in args:
        return 'Welcome back Norberto!'
    return 'Not sure who you are...'
    
ensure_correct_info(25, True, "Norberto", "Sanchez-Dichi", "hi")