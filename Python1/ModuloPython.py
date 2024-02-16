from converter import euro_dollar, dollar_euro
from temperatura import celsius_fahrenheit, fahrenheit_celsius

print(euro_dollar(100))
print(dollar_euro(100))


# DESAFIO
# CRIA DUAS FUNÇÕES QUE FAÇAM A CONVERSÃO DE GRAUS CELSIUS PARA FAHRENHEIT E VICE-VERSA
# COLOCAR ESSAS DUAS FUNÇÕES NUM MÓDULO EXTERNO COM NOME temperatura
# IMPORTAR O MODULO E EXPERIMENTAR CONVERTER 32º PARA FAHRENHEIT

print(celsius_fahrenheit(32))
print(round(fahrenheit_celsius(75) ,2))
