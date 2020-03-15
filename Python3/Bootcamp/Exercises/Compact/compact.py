def compact(list):
    return [value for value in list if value == True]
    
print(compact([0,1,2,"",[], False, {}, None, "All done"]))