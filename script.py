# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille',
         'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September',
          'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977,
         1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160,
                       175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], [
    'Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M',
           'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11,
          2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# write your update damages function here:


def updated_damages():
    """Update types in damages variable to be easier to work with

    Returns:
        list: New list of damage values
    """

    new = []

    for item in damages:
        if item == "Damages not recorded":
            new.append(item)
        else:
            if item[-1] == "M":
                new.append(float(item.rstrip("M")) * 1_000_000)
            elif item[-1] == "B":
                new.append(float(item.rstrip("B")) * 1_000_000_000)
            else:
                new.append("NA")

    return new

# write your construct hurricane dictionary function here:


def construct_hurricane_data():
    """Make a dictionary of hurricane data based on supplied data
    from Codecademy

    Returns:
        dict: dict of {name: {...}}
    """
    dat = {}
    for i in range(len(names)):
        dat[names[i]] = {
            "Name": names[i],
            "Month": months[i],
            "Year": years[i],
            "Max Sustained Wind": max_sustained_winds[i],
            "Areas Affected": areas_affected[i],
            "Damages": updated_damages()[i]
        }
    return dat

# write your construct hurricane by year dictionary function here:


def by_year(dat):
    """Take hurrcane data and organize it by year

    Args:
        dat (dict): Original dict of hurricane data,
        usually returned by the construct hurricane data
        function

    Returns:
        dict: New dict of {year: { ... }}
    """
    dat = {}
    for i in range(len(names)):
        dat[years[i]] = {
            "Name": names[i],
            "Month": months[i],
            "Year": years[i],
            "Max Sustained Wind": max_sustained_winds[i],
            "Areas Affected": areas_affected[i],
            "Damages": updated_damages()[i]
        }
    return dat

# write your count affected areas function here:


def count_areas_affected():
    """Count the number of occurences for areas in
    areas_affected

    Returns:
        dict: dict of {area: count}
    """
    flat_areas = []
    for areas in areas_affected:
        for area in areas:
            flat_areas.append(area)

    return {area: flat_areas.count(area) for area in flat_areas}


# write your find most affected area function here:

def most_affected(dat):
    """Find the most affected area

    Args:
        dat (dict): Dictionary of areas affected,
        usually returned by count_areas_affected()

    Returns:
        tuple: Tuple of (area, occurrences)
    """

    areas = [k for k in dat.keys()]
    vals = [v for v in dat.values()]

    occurrences = max(vals)
    area = areas[vals.index(occurrences)]

    return area, occurrences

# write your greatest number of deaths function here:


def most_deaths():
    """Find the hurricane with the highest kill count

    Returns:
        tuple: Tuple of (num_deaths, hurricane_name)
    """
    num = max(deaths)
    return num, names[deaths.index(num)]

# write your catgeorize by mortality function here:


def _get_mortality(count):
    if count >= 0 and count < 100:
        return 0
    elif count >= 100 and count < 500:
        return 1
    elif count >= 500 and count < 1000:
        return 2
    elif count >= 1000 and count < 10000:
        return 3
    else:
        return 4


def score_mortality():
    """Organize hurricane names by mortality scale

    Returns:
        dict: dict of {rating: [hurricane1, hurricane2, ...]}
    """
    names_to_deaths = {name: count for name, count in zip(names, deaths)}
    scores = {}
    for i in range(4):
        scores[i] = [name for name in names_to_deaths if
                     _get_mortality(names_to_deaths[name]) == i]

    return scores

# write your greatest damage function here:


def greatest_damage():

    ammts = [n for n in updated_damages() if n != "Damages not recorded"]
    num = max(ammts)
    return names[updated_damages().index(num)], num

# write your catgeorize by damage function here:


def _get_damages_score(count):
    try:
        if count >= 0 and count < 100_000_000:
            return 0
        elif count >= 100_000_000 and count < 1_000_000_000:
            return 1
        elif count >= 1_000_000_000 and count < 10_000_000_000:
            return 2
        elif count >= 10_000_000_000 and count < 100_000_000_000:
            return 3
        else:
            return 4
    except TypeError:
        return None


def score_damages():
    """Organize the hurricanes by damages

    Returns:
        dict: dict of {score: [hurricane1, hurricane2, ...]}
    """
    names_to_damages = {name: damages for name, damages, in zip(names,
                                                                updated_damages())}

    scores = {}
    for i in range(4):
        scores[i] = [name for name in names_to_damages if
                     _get_damages_score(names_to_damages[name]) == i]

    return scores
