cities_to_check = ['lahore','islamabad']  
clean_city = str(input(''))
clean_city = clean_city.lower()
for check_city in cities_to_check:
    if clean_city == check_city:
        print("List of clean cities")
        break
    else:
        print("Not a clean city")
        break
