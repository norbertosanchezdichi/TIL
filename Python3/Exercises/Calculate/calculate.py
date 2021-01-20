def calculate(**kwargs):
    
    result = 0
    if kwargs['operation'] == 'add':
        result = kwargs['first'] + kwargs['second']    
    elif kwargs['operation'] == 'subtract':
        result = kwargs['first'] - kwargs['second']    
    elif kwargs['operation'] == 'multiply':
        result = kwargs['first'] * kwargs['second'] 
    elif kwargs['operation'] == 'divide':
        result = kwargs['first'] / kwargs['second']
        
    if not kwargs['make_float']:
        result = int(result)

    if 'message' in kwargs:
        return kwargs['message'] + ' ' + str(result)
    else:
        return 'The result is ' + str(result)

calculate(make_float=False, operation='add', message='You just added', first=2, second=4) # "You just added 6"

calculate(make_float=True, operation='divide', first=3.5, second=5) # "The result is 0.7"

# Pythonic Version
def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final