# function
def get_month(language, number):
    lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if language == "ru":
        return lng_ru[number-1]
    if language == "en":
        return lng_en[number-1]
    pass

# input
lan = input()
num = int(input())

# call a function
print(get_month(lan, num))