try:
    foobar
except:  #"catch all", highly discourage due to not being able to identify what went wrong 
    print("PROBLEM")
print("after the try")