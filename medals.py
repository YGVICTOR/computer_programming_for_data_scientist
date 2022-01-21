import json
import csv


class CountryMedals:
    def __init__(self,name,gold,silver,bronze):
        self.__name = name
        self.__gold = gold
        self.__silver = silver
        self.__bronze = bronze

    @property
    def name(self):
        return self.__name

    def to_json(self):
        attribute_result = {}
        attribute_dict = {}
        attribute_dict['gold'] = self.__gold
        attribute_dict['silver'] = self.__silver
        attribute_dict['bronze'] = self.__bronze
        attribute_dict['total'] = self.__gold + self.__silver + self.__bronze
        attribute_result[self.name] = attribute_dict
        json_attribute = json.dumps(attribute_dict)
        return json_attribute

    def get_medals(self,medal_type):
        if medal_type == 'gold':
            return self.__gold
        elif medal_type == 'silver':
            return self.__silver
        elif medal_type == 'bronze':
            return self.__bronze
        elif medal_type == 'total':
            return self.__bronze + self.__gold + self.__silver
        else:
            return None

    def print_summary(self):
        print("{country} received {total} medals in total; {gold} gold, {silver} silver, and {bronze} bronze.".format(country= self.__name,
                                                                                                                      total = self.get_medals('total'),
                                                                                                                      gold = self.get_medals('gold'),
                                                                                                                      silver = self.get_medals('silver'),
                                                                                                                      bronze = self.get_medals('bronze')))

    def __compare_helper(self,country_2,medal_type):
        medal1 = self.get_medals(medal_type)
        medal2 = country_2.get_medals(medal_type)
        if medal1 == medal2:
            print('- Both {country_1} and {country_2} received {medal_qty} {medal1_type} medal(s).'.format(
                country_1 = self.name,
                country_2 = country_2.name,
                medal_qty = medal2,
                medal1_type = medal_type
            ))
        elif medal1 > medal2:
            print('- {country_1} received {medal1} {medal_type} medal(s), {offset} more than {country_2}, which received {medal2}.'.format(
                country_1 = self.name,
                medal1 = medal1,
                medal_type = medal_type,
                offset = medal1 - medal2,
                country_2 = country_2.name,
                medal2 = medal2
            ))
        else:
            print('- {country_1} received {medal1} {medal_type} medal(s), {offset} fewer than {country_2}, which received {medal2}.'.format(
                country_1 = self.name,
                medal1 = medal1,
                medal_type = medal_type,
                offset = medal2 - medal1,
                country_2 = country_2.name,
                medal2 = medal2
            ))

    def compare(self,country_2):
        country1 = self.name
        country2 = country_2.name
        print('Medals comparison between \'{country1}\' and \'{country2}\':'.format(
            country1=country1,
            country2=country2
        ))
        self.__compare_helper(country_2,'gold')
        self.__compare_helper(country_2, 'silver')
        self.__compare_helper(country_2,'bronze')
        total1 = self.get_medals('gold') + self.get_medals('silver') + self.get_medals('bronze')
        total2 = country_2.get_medals('gold') + country_2.get_medals('silver') + country_2.get_medals('bronze')
        if total1 > total2:
            print('Overall, {country1} received {total1} medal(s), {offset} more than {country2}, which received {total2} medal(s).'.format(
                country1 = self.name,
                total1 = total1,
                offset = total1 - total2,
                country2 = country_2.name,
                total2 = total2
            ))
        elif total1 < total2:
            print(
                'Overall, {country1} received {total1} medal(s), {offset} more less {country2}, which received {total2} medal(s).'.format(
                    country1=self.name,
                    total1=total1,
                    offset=total2 - total1,
                    country2=country_2.name,
                    total2=total2
                ))
        else:
            print(
                'Overall, both {country1} and {country2} received {total1} medal(s).'.format(
                    country1=self.name,
                    total1=total1,
                    country2=country_2.name,
                ))


def get_sorted_list_of_country_names(countries):
    result = []
    for cur_value in countries.values():
        name = cur_value.name
        result.append(name)
    result.sort(key=lambda x: x.upper())
    return result


def sort_countries_by_medal_type_ascending(countries, medal_type):
    tmp = []
    for k,v in countries.items():
       tmp.append(v)
    tmp.sort(key=lambda x: x.get_medals(medal_type))
    result = [x.name for x in tmp]
    return result


def sort_countries_by_medal_type_descending(countries, medal_type):
    tmp = []
    for k,v in countries.items():
        tmp.append(v)
    tmp.sort(key=lambda x:x.get_medals(medal_type),reverse=True)
    result = [x.name for x in tmp]
    return result


def read_positive_integer():
    try:
        result = int(input('Enter the threhold (a positive integer):'))
        if result >= 0:
            return result
        else:
            print("your input is incorrect, please input a positive integer")
            return read_positive_integer()
    except:
        print("your input is incorrect, please input a positive integer")
        return read_positive_integer()


def read_country_name():
    countries = ['Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Belarus', 'Belgium', 'Bermuda', 'Botswana', 'Brazil', 'Bulgaria', 'Burkina Faso', 'Canada', 'Chinese Taipei', 'Colombia', 'Croatia', 'Cuba', 'Czech Republic', "Côte d'Ivoire", 'Denmark', 'Dominican Republic', 'Ecuador', 'Egypt', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Georgia', 'Germany', 'Ghana', 'Great Britain', 'Greece', 'Grenada', 'Hong Kong,China', 'Hungary', 'India', 'Indonesia', 'Ireland', 'Islamic Republic of Iran', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Latvia', 'Lithuania', 'Malaysia', 'Mexico', 'Mongolia', 'Morocco', 'Namibia', 'Netherlands', 'New Zealand', 'Nigeria', 'North Macedonia', 'Norway', "People's Republic of China", 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Republic of Korea', 'Republic of Moldova', 'ROC', 'Romania', 'San Marino', 'Saudi Arabia', 'Serbia', 'Slovakia', 'Slovenia', 'South Africa', 'Spain', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Thailand', 'Tunisia', 'Turkey', 'Turkmenistan', 'Uganda', 'Ukraine', 'United States of America', 'Uzbekistan', 'Venezuela']
    input_ = input('Insert a country name (\'q\' for quit): ')
    if input_.capitalize() in countries:
        return input_.capitalize()
    elif input_.upper() == 'Q':
        return
    else:
        print('The country you have just entered is incorrect, you can input one of the following countries: ')
        result = '; '.join(countries)
        print(result)
        return read_country_name()


def read_medal_type():
    potential_correct_input = ['gold','silver','bronze','total']
    inputed_type = input('Insert a model type (chose among \'gold\',\'silver\',\'bronze\', or \'total\'):')
    if inputed_type in potential_correct_input:
        return inputed_type
    else:
        print('The medal type you have just inputted is incorrect, you can input one of the following medal type:')
        for medal_type in potential_correct_input:
            print(medal_type)
        return read_medal_type()


if __name__ == '__main__':
    list_form = []
    try:
        with open('Medals.csv','r',encoding='utf-8')as medal_file:
            head = medal_file.readline().split(sep=',')
            csv_data = csv.DictReader(medal_file,fieldnames=head)
            list_form = list(csv_data)
    except IOError as ioe:
        print("IOErrot"+str(ioe))

    countries = {}
    for country in list_form:
        countries[country['Team/NOC']]=CountryMedals(country['Team/NOC'],int(country['Gold']),int(country['Silver']),int(country['Bronze']))

    quited = False
    while not quited:
        c = input('Insert a command (H for help):')
        if c.upper() == 'Q' or c.upper() == 'QUIT':
            quited = True
        elif c.upper() == 'H' or c.upper() == 'HELP':
            print('List of commands:')
            print('- (H)elp shows the list of comments;')
            print('- (L)ist shows the list of countries present in the dataset;')
            print('- (S)ummary prints out a summary of the medals won by a single country;')
            print('- (C)ompare allows for a comparison of the medals won by two countries;')
            print('- (M)ore, given a medal type, lists all the countries that received more medals than a treshold;')
            print('- (F)ewer, given a medal type, lists all the countries that received fewer medals than a treshold;')
            print('- (E)xport, save the medals table as \'.json\' file;')
            print('- (Q)uit.')
        elif c.upper() == 'L' or c.upper() == 'LIST':
            result = ', '.join(get_sorted_list_of_country_names(countries))
            summary = 'The dataset contains {} countries: '.format(len(countries))
            print(summary + result)
        elif c.upper() == 'S' or c.upper() == 'SUMMARY':
            country_name = read_country_name()
            if country_name is not None:
                print('{country_name} received {total} medals in total; {gold} gold, {silver} silver, and {bronze} bronze.'.format(
                    country_name = country_name,
                    total = countries[country_name].get_medals('total'),
                    gold = countries[country_name].get_medals('gold'),
                    silver = countries[country_name].get_medals('silver'),
                    bronze = countries[country_name].get_medals('bronze')
                ))
        elif c.upper() == 'C' or c.upper() == 'COMPARE':
            print('Compare two countries')
            country1 = read_country_name()
            print('Insert the name of the country you want to compare against \'{country1}\' '
                  .format(country1 = country1))
            country2 = read_country_name()
            countries[country1].compare(countries[country2])
        elif c.upper() == 'M' or c.upper() == 'MORE':
            print('Given a medal type, lists all the countries that received more medals than a treshold;')
            medal_type = read_medal_type()
            threshold = read_positive_integer()
            print('Countries that received more than {threshold} {model_type} medals:'.format(threshold = threshold,
                                                                                              model_type = medal_type))
            result = {}
            for k,v in countries.items():
                if v.get_medals(medal_type) > threshold:
                    result[k] = v
            country_result = sort_countries_by_medal_type_descending(result, medal_type)
            for country in country_result:
                print('- {country_name} received {medal_qty}'.format(
                    country_name = countries[country].name,
                    medal_qty = countries[country].get_medals(medal_type)
                ))
        elif c.upper() == 'F' or c.upper() == 'FEWER':
            print('Given a medal type, lists all the countries that received fewer medals than a treshold;')
            medal_type = read_medal_type()
            threshold = read_positive_integer()
            print('Countries that received fewer than {threshold} {model_type} medals:'.format(threshold=threshold,
                                                                                               model_type=medal_type))
            result = {}
            for k, v in countries.items():
                if v.get_medals(medal_type) < threshold:
                    result[k] = v
            country_result = sort_countries_by_medal_type_ascending(result, medal_type)
            for country in country_result:
                print('- {country_name} received {medal_qty}'.format(
                    country_name=countries[country].name,
                    medal_qty=countries[country].get_medals(medal_type)
                ))
        elif c.upper() == 'E' or c.upper() == 'EXPORT':
            file_name = input('Enter the file name (.json)')
            result_dict = {}
            file_path = '{file_path}.json'.format(file_path=file_name)
            for v in countries.values():
                tmp = json.loads(v.to_json())
                result_dict[v.name] = tmp
            json_data = json.dumps(result_dict,indent=4,separators=(',',':'))
            f = open(file_path,mode='a',encoding='utf-8')
            f.write(json_data)
            f.close()
            print("File: \'{file_name}\' correctly saved.".format(file_name=file_name))
        else:
            print("Command not recognised. Please try again")
