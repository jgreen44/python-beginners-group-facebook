import csv
import os.path
import sys


class CheckLifeExpectancy:
    max_life_expectancy = -sys.maxsize - 1  # set to lowest int value
    max_life_country = None
    min_life_expectancy = sys.maxsize  # set to highest int value
    min_life_country = None

    def __init__(self, data):
        self.data = data
        # Get the max value for life expectancy
        max_value = max(self.data['life_expectancy'])

        # Get the min value for life expectancy
        min_value = min(self.data['life_expectancy'])

        # Get the index position for max value for life expectancy
        self.max_index = self.data['life_expectancy'].index(max_value)

        # Get the index position for the min value for life expectancy
        self.min_index = self.data['life_expectancy'].index(min_value)

        # Get the average life expectancy from all countries
        # To print two decimals, use format() {:. 2f}
        self.avg_life_expectancy = round(sum(self.data['life_expectancy']) / len(self.data['life_expectancy']), 2)

    def main(self):
        choice_year = input("Enter the year of interest: ")
        while choice_year.isnumeric() is False:
            print("A year must be a number only. Try again...\n")
            choice_year = input("Enter the year of interest: ")

        choice_year = int(choice_year)

        # loop dict to obtain min/max life expectancy/country from given year

        for i in self.data['life_expectancy']:
            index = self.data['life_expectancy'].index(i)
            if self.data['year'][index] == choice_year:
                # Get max life expectancy for given year
                if self.max_life_expectancy < self.data['life_expectancy'][index]:
                    self.max_life_expectancy = self.data['life_expectancy'][index]
                    # Get the country for the max life expectancy for given year
                    self.max_life_country = self.data['country'][index]

                # Get min life expectancy for given year
                if self.min_life_expectancy > self.data['life_expectancy'][index]:
                    self.min_life_expectancy = self.data['life_expectancy'][index]
                    self.min_life_country = self.data['country'][index]
        return choice_year

    def output(self, user_year_choice):

        print(f" The overall max life expectancy is: "
              f"{max(self.data['life_expectancy'])} from "
              f"{self.data['country'][self.max_index]} in "
              f"{self.data['year'][self.max_index]}")
        print(f" The overall min life expectancy is: "
              f"{self.data['life_expectancy'][self.min_index]} from "
              f"{self.data['country'][self.min_index]} in "
              f"{self.data['year'][self.min_index]}")
        print(f"The average life expectancy across all countries was {self.avg_life_expectancy}\n")

        print(f"For the year {user_year_choice}:\n")
        print(f"The max life expectancy was in "
              f"{self.max_life_country} with "
              f"{self.max_life_expectancy}")
        print(f"The min life expectancy was in "
              f"{self.min_life_country} with "
              f"{self.min_life_expectancy}")


if __name__ == '__main__':

    user_data = {
        'year': [],
        'country': [],
        'life_expectancy': []
    }

    csv_path = r'life-expectancy/life-expectancy.csv'

    if not os.path.isfile(csv_path):
        print("life-expectancy.csv file not found. Exiting program.")
        exit(-1)

    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader, None)
        for row in csv_reader:
            user_data['year'].append(int(row[2]))
            user_data['country'].append(row[0])
            user_data['life_expectancy'].append(float(row[3]))

    life_expectancy = CheckLifeExpectancy(user_data)
    choice_year = life_expectancy.main()
    life_expectancy.output(choice_year)