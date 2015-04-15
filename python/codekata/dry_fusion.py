class TeamData:
    def __init__(self, team="", goals_for=0, goals_against=0):
        self.team = team
        self.goals_for = goals_for
        self.goals_against = goals_against

    @property
    def team(self):
        return self.__team

    @team.setter
    def team(self, team):
        self.__team = team

    @property
    def goals_for(self):
        return self.__goals_for

    @goals_for.setter
    def goals_for(self, goals_for):
        self.__goals_for = goals_for

    @property
    def goals_against(self):
        return self.__goals_against

    @goals_against.setter
    def goals_against(self, goals_against):
        self.__goals_against = goals_against

    def difference(self):
        return abs(self.goals_for - self.goals_against)

    def __str__(self):
        return 'team=' + str(self.team) + ', goals_for=' + str(self.goals_for) + ', goals_against=' + str(self.goals_against)

class WeatherData:
    def __init__(self, day=0, min_temp=0, max_temp=0):
        self.day = day
        self.min_temp = min_temp
        self.max_temp = max_temp

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        self.__day = day

    @property
    def min_temp(self):
        return self.__min_temp

    @min_temp.setter
    def min_temp(self, min_temp):
        self.__min_temp = min_temp

    @property
    def max_temp(self):
        return self.__max_temp

    @max_temp.setter
    def max_temp(self, max_temp):
        self.__max_temp = max_temp

    def difference(self):
        return self.max_temp - self.min_temp

    def __str__(self):
        return 'day=' + str(self.day) + ', min_temp=' + str(self.min_temp) + ', max_temp=' + str(self.max_temp)



from functools import reduce


class ItemSearcher:
    def __init__(self, data):
        self.__data = data

    @staticmethod
    def with_min_difference(first, second):
        if first.difference() < second.difference():
            return first
        else:
            return second

    def min_difference(self):
        return reduce(ItemSearcher.with_min_difference, self.__data)


import re


def strip_number(token):
    return int(re.search('(\d+)', token).group(0))

class SoccerDataMapper:
    def map(self, line):
        tokens = line.strip().split()
        team_data = TeamData()
        print(tokens[0], tokens[6], tokens[8])
        team_data.team = tokens[1]
        team_data.goals_for = strip_number(tokens[6])
        team_data.goals_against = strip_number(tokens[8])
        return team_data

class WeatherDataMapper:
    def map(self, line):
        tokens = line.strip().split()
        weather_data = WeatherData()
        weather_data.day = strip_number(tokens[0])
        weather_data.max_temp = strip_number(tokens[1])
        weather_data.min_temp = strip_number(tokens[2])
        return weather_data


class CsvLoader:
    def __init__(self, mapper):
        self.__mapper = mapper

    def load(self, filename):
        result = []
        with open(filename, 'r') as file:
            # apply mapping to each line
            for line in file:
                if re.search('^\s*\d+', line):
                    result.append(self.__mapper.map(line))
        return result


loader = CsvLoader(SoccerDataMapper())
data = loader.load('football.dat')
# data = [WeatherData(1, 3, 21), WeatherData(1, 8, 15), WeatherData(1, 20, 30)]
team_data = ItemSearcher(data).min_difference()

print(team_data)

loader = CsvLoader(WeatherDataMapper())
data = loader.load('weather.dat')
# data = [WeatherData(1, 3, 21), WeatherData(1, 8, 15), WeatherData(1, 20, 30)]
weather_data = ItemSearcher(data).min_difference()

print(weather_data)