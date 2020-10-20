"""Try creating a list of cities that will include a series of tuples that contain both a city’s name and its ZIP code.
Loop through the list and utilize tuple assignment. Assign one variable to denote the city name and another variable to
represent the ZIP code. Display the city’s name and ZIP code to the screen."""

cities = [
    ("Ljubljana", 1000),
    ("Maribor", 8000),
    ("Koper", 5000),
    ("Slivnica", 4000),
    ("Portoroz", 2000),
    ("Celje", 7000)
]

for (city, zip_code) in cities:
    print("The city of {} has a ZIP code of {}.".format(city, str(zip_code)))