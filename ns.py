def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
#inner_function()   при выведении результата выдается ошибка, тк внутренняя функция локальна для внешней
test_function() # выводится текст из внутреней функции

