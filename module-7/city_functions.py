def catLocations(city, country, population='', language=''):
    if population and language:
        destination = f"{city}, {country} - population {population}, {language}"
    elif language:
        destination = f"{city}, {country}, {language}"
    elif population:
        destination = f"{city}, {country} - population {population}"
    else:
        destination = f"{city}, {country}"
    return destination.title()
 
    

firstCall = catLocations("Santiago", "Chile")
print(firstCall)
secondCall = catLocations("Lima","Peru", 500000)
print(secondCall)
thirdCall = catLocations("Bogota", "Colombia", 3215648, "Spanish")
print(thirdCall)