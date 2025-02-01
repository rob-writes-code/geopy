from geopy.geocoders import Nominatim
import random

def get_location_and_country():
    #get longitude and latitude
    longitude = random.randint(-180, 180)
    latitude = random.randint(-90, 90)
    
    # Create a geocoder instance for finding country from monster long&lat
    geolocator = Nominatim(user_agent="my_geocoder")
    
    # Reverse geocode to get the location information
    location = geolocator.reverse((latitude, longitude), language='en')

    # Extract the country from the location information, with a random lat and long it might not have a country
    country = "Sea"
    try:
        country = location.raw['address']['country']
    except:
        country = 'Sea'
    return [str(country), str(longitude), str(latitude)]

output = get_location_and_country()
print(output)