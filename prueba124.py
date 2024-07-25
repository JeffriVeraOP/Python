'''Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.
Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código. Esta prueba es solo el comienzo.'''

def is_year_leap(yr):
    if yr % 4 != 0:
        return False
    elif yr % 100 != 0:
        return True
    elif yr % 400 != 0:
        return False
    else:
        return True

days_in_month_b = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_in_month_n = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days_in_month(yr, mo):
    if is_year_leap(yr) == True:
        result = days_in_month_b[mo-1]
        return result
    elif is_year_leap(yr) == False:
        result = days_in_month_n[mo-1]
        return result
    else:
        return None
 
def day_of_year(yr, mo, day):
    a = sum(days_in_month_b[:mo])
    b = days_in_month(yr, mo) - day
    if yr < 1542 or mo < 0 or mo > 12 or day < 0 or day > 31:
        return None
    elif is_year_leap(yr):
        if days_in_month(yr, mo) == 31 or 30 or 29:
            return a - b
    else:
        if mo > 1:
            return (a - b) - 1
        else:
            return a - b

print(day_of_year(2001, 2, 1))

'''Codigo mejorado por ChatGPT
def day_of_year(yr, mo, day):
    if yr < 1542 or mo < 1 or mo > 12 or day < 1 or day > 31:
        return None

    if day > days_in_month(yr, mo):
        return None

    days_in_previous_months = sum(days_in_month_b[:mo-1]) if is_year_leap(yr) else sum(days_in_month_n[:mo-1])
    return days_in_previous_months + day
'''
'''Codigo de CISCO
def day_of_year(year, month, day):
    days = 0
    for m in range(1, month):
        md = days_in_month(year, m)
        if md == None:
            return None
        days += md
    md = days_in_month(year, month)
    if day >= 1 and day <= md:
        return days + day
    else:
        return None
'''