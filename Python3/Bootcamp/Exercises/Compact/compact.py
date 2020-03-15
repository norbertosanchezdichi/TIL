def compact(list):
    return [value for value in list if value != False and value != None and len(str(value)) != 0]
    
print(compact([0,1,2,"",[], False, {}, None, "All done"]))