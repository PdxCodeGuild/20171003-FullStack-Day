"""
Lab 10: convert the given distance and units to the target units
we have four types of units: meters (m), miles (mi), feet (ft), and kilometers (km)
we could handle each case individually
    e.g. if from_units == 'm' and to_units == 'miles'
instead, we'll just convert to meters, then convert to the target units
"""

# 1) get the distance from the user
# 2) convert that distance to a float
# 3) get the units for that distance from the user
# 4) get the units that the user wants to convert to
# 4) convert the distance to meters
# 5) convert the distance from meters to the target


# 1 mile is 1609.34 meters
# 1 foot is 0.3048 meters
# 1 kilometer is 1000 meters
# 1 meter is 1 meter
# 1 yard is 0.9144 meters
# 1 inch is 0.0254 meters


# convert the given distance from the given units to meters
def to_meters(distance, units):
    if units == 'm':  # meters
        return distance
    elif units == 'mi': # miles
        return distance * 1609.34
    elif units == 'ft': # feet
        return distance * 0.3048
    elif units == 'km': # kilometers
        return distance * 1000
    elif units == 'yd': # yards
        return distance * 0.9144
    elif units == 'in': # inches
        return distance * 0.0254


# convert the given distance (in meters) to the target units
def from_meters(distance, units):
    if units == 'm': # meters
        return distance
    elif units == 'mi': # miles
        return distance / 1609.34
    elif units == 'ft': # feet
        return distance / 0.3048
    elif units == 'km': # kilometers
        return distance / 1000
    elif units == 'yd': # yards
        return distance / 0.9144
    elif units == 'in': # inches
        return distance / 0.0254


def standardize_units(units):
    if units in ['m', 'meter', 'meters']:
        return 'm'
    elif units in ['mi', 'mile', 'miles']:
        return 'mi'
    elif units in ['ft', 'feet']:
        return 'ft'
    elif units in ['km', 'kilometer', 'kilometers']:
        return 'km'
    elif units in ['yd', 'yard', 'yards']:
        return 'yd'
    elif units in ['in', 'inch', 'inches']:
        return 'in'

def main():
    print('Welcome to the Distance Converter 5001™')
    distance_in = float(input('what is the distance? '))
    units_in = input('what are the units you\'re converting from? ')
    units_out = input('what are the units you\'re converting to? ')

    units_in = standardize_units(units_in)
    units_out = standardize_units(units_out)


    distance_in_m = to_meters(distance_in, units_in)
    distance_out = from_meters(distance_in_m, units_out)

    output = f'{distance_in} {units_in} is {distance_out} {units_out}'

    # output = str(distance_in) + ' ' + units_in + ' is '
    # output += str(distance_out) + ' ' + units_out
    print(output)


main()
