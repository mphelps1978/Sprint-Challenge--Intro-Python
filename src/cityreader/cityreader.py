

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


import csv


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return f'{self.name}, {self.lat}, {self.lon}'


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []

# TODO Implement the functionality to read from the 'cities.csv' file
# Ensure that the lat and lon valuse are all floats
# For each city record, create a new City instance and add it to the
# `cities` list

# open csv file for reading
# read the file and get the values in a comma-separated state
# append the list using our new class. (note the csv uses lng for longitude, and we have it set up here as lon)


def cityreader(cities=[]):
    with open('cities.csv', 'r') as csvfile:
        city_doc = csv.DictReader(csvfile, delimiter=',')
        for e in city_doc:
            cities.append(City(e['city'], float(e['lat']), float(e['lng'])))
    return cities


cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    within = []

    # Go through each city and check to see if it falls within
    # the specified coordinates.

    for city in cities:
        # account for one corner
        if lat1 > lat2:
            # check coordinates of the list and append if they are within the coordinate square
            # Breakdown:
            # if list lat is less than lat1 AND
            # if list lat is greater than lat2 AND
            # if list lon is less than lon1 AND
            # if list long is greater than lon2 THEN
            # The coords are within the square, add to list

            if(city.lat <= lat1 and city.lat >= lat2 and city.lon <= lon1 and city.lon >= lon2):
                within.append(city)
        # account for opposite corner - (Breakdown is reversed)
        elif lat2 > lat1:
            if(city.lat >= lat1 and city.lat <= lat2 and city.lon >= lon1 and city.lon <= lon2):
                within.append(city)

    return within


# get user input
# normalize the input - first we'll extend the inputs into one
# then create a list of the inputs, making it a float type just in case some weird coordinates are entered
# finally, we pass the completed coordinates into the fucntion and create a new list
# and  print our results

print('Given 2 pairs of coordinates, I\'ll tell you what cities are in the radius. Enter 2 comma separated pairs\n\n')
input1 = input("Enter the first pair: ").split(',')
input2 = input("Enter the second pair: ").split(',')

input1.extend(input2)
search_location = [float(i) for i in input1]
# print(search_location)

find_cities = cityreader_stretch(
    search_location[0], search_location[1], search_location[2], search_location[3], cities)

for city in find_cities:
    print(city)
