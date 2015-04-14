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

    def goal_difference(self):
        return abs(self.goals_for - self.goals_against)

    def __str__(self):
        return 'team=' + str(self.team) + ', goals_for=' + str(self.goals_for) + ', goals_against=' + str(self.goals_against)


from functools import reduce


class Soccer:
    def __init__(self, data):
        self.__data = data

    @staticmethod
    def with_min_goal_difference(first, second):
        if first.goal_difference() < second.goal_difference():
            return first
        else:
            return second

    def min_goal_difference(self):
        return reduce(Soccer.with_min_goal_difference, self.__data)


import re


class ObjectMapper:
    def map(self, line):
        tokens = line.strip().split()
        team_data = TeamData()
        print(tokens[0], tokens[6], tokens[8])
        team_data.team = tokens[1]
        team_data.goals_for = ObjectMapper.strip_number(tokens[6])
        team_data.goals_against = ObjectMapper.strip_number(tokens[8])
        return team_data

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
data = loader.load('football.dat')
# data = [WeatherData(1, 3, 21), WeatherData(1, 8, 15), WeatherData(1, 20, 30)]
team_data = Soccer(data).min_goal_difference()

print(team_data)
