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

    def spread(self):
        return self.max_temp - self.min_temp

    def __str__(self):
        return 'day=' + str(self.day) + ', min_temp=' + str(self.min_temp) + ', max_temp=' + str(self.max_temp)


from functools import reduce


class Weather:
    def __init__(self, data):
        self.__data = data

    @staticmethod
    def with_min_spread(first, second):
        if first.spread() < second.spread():
            return first
        else:
            return second

    def min_spread(self):
        return reduce(Weather.with_min_spread, self.__data)


import re


class ObjectMapper:
    def map(self, line):
        tokens = line.strip().split()
        weather_data = WeatherData()
        weather_data.day = ObjectMapper.strip_number(tokens[0])
        weather_data.max_temp = ObjectMapper.strip_number(tokens[1])
        weather_data.min_temp = ObjectMapper.strip_number(tokens[2])
        return weather_data

    @staticmethod
    def strip_number(token):
        return int(re.search('(\d+)', token).group(0))


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


loader = CsvLoader(ObjectMapper())
data = loader.load('weather.dat')
# data = [WeatherData(1, 3, 21), WeatherData(1, 8, 15), WeatherData(1, 20, 30)]
weather = Weather(data).min_spread()

print(weather)