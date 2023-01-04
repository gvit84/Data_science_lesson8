#Функція, яка приймає довільну кількість словників, збирає їх в один словник та повертає його
main_dct = {}
def main_function(**kwargs):
    main_dct.update(**kwargs)
    return main_dct


main_function(brand='Kia', model='Sportage', year=2018)
main_function(sedan='Volkswagen', Coupe='Porsche')
main_function(January='spring', June='summer')
main_function(name='Vitalii', age=38, eyes_color='green')
print(main_dct)


#Функція, яка приймає номер місяця та повертає рядок з назвою пори року, до якої цей місяць відноситься
def year_seasons(a):
    dct = {1: "winter", 2: "winter", 3: "spring", 4: "spring", 5:"spring", 6: "summer",
           7: "summer", 8: "summer", 9: "autumn", 10: "autumn", 11: "autumn", 12: "winter"}
    return dct[a]

print(year_seasons(4))