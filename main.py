#Функція, яка приймає довільну кількість словників, збирає їх в один словник та повертає його
main_dct = {}
def main_function(**kwargs):
    main_dct.update(**kwargs)
    return main_dct


main_function(brand='Volvo', model='XC90', year=2022)
main_function(sedan='Volkswagen', Coupe='Porsche')
main_function(January='spring', June='summer')
main_function(name='Vitalii', age=38, eyes_color='green')
print(main_dct)