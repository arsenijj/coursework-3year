import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import figures
import drawing as d
plt.figure(figsize=(30, 20))


def print_statistics(figure_name, indexes, col, prices, flag, c):
    print(f'Стастистика по фигуре {figure_name}:')
    print(f'Всего найдено: {len(indexes)}, что составляет \
        {round(len(indexes) / c, 3)} от общего числа фигур')
    delta = 0
    # вымпел, восходящий / нисходящий флаг
    if flag == 1 or flag == 2 or flag == 3:
        delta = 6
    # прямоугольник
    elif flag == 4:
        delta = 8
    # восходящий / нисходящий ромб
    elif flag == 5 or flag == 6:
        delta = 9
    # голова и плечи
    elif flag == 7:
        delta = 5
    res = 0

    for index in indexes:
        
        if flag == 1 or flag == 2 or flag == 3 or flag == 4:
            if prices[index] > prices[index - 1] and \
                prices[index + delta] > prices[index + delta - 1]:
                res += 1
            if prices[index] < prices[index - 1] and \
                prices[index + delta] < prices[index + delta - 1]:
                res += 1
        
        if flag == 5 or flag == 6 or flag == 7:
            if prices[index] < prices[index - 1] and \
                prices[index + delta] > prices[index + delta - 1]:
                res += 1
            if prices[index] > prices[index - 1] and \
                prices[index + delta] < prices[index + delta - 1]:
                res += 1
    
    print('Прошло: ', res)
    if len(indexes):
        print('Удача:', res / len(indexes))


def get_extrema(date, prices):
    indexes = []
    for i in range(1, len(prices) - 1):
        if prices[i] > prices[i - 1] and prices[i] > prices[i + 1] or \
                prices[i] < prices[i - 1] and \
                    prices[i] < prices[i + 1]:
           indexes.append(i)

    return [date[index] for index in indexes], \
        [prices[index] for index in indexes]


data = yf.Ticker("EOS").history(period='5y')
prices = np.array(data['High'])
data.reset_index(inplace=True)
date = np.array(data['Date'], dtype='datetime64[D]')

delta_y = (max(prices) - min(prices)) / 10
date_extrema, prices_extrema = get_extrema(date, prices)
plt.plot(date_extrema, prices_extrema, color='red', linestyle='--')
plt.plot(date, prices)

print(len(prices_extrema))
count_pennants, res_pennants = figures.get_pennants(prices_extrema)
d.draw_pennants_rising_flags(plt, res_pennants, \
    prices_extrema, date_extrema, delta_y)

count_descending_flags, res_descending_flags = \
figures.get_descending_flags(prices_extrema)
d.draw_descending_flags(plt, res_descending_flags, \
    prices_extrema, date_extrema, delta_y)

count_rising_flags, res_rising_flags = \
    figures.get_rising_flags(prices_extrema)
d.draw_pennants_rising_flags(plt, res_rising_flags, \
    prices_extrema, date_extrema, delta_y)

count_rectangles, res_rectangles = \
    figures.get_rectangles(prices_extrema)
d.draw_rectangles(plt, res_rectangles, \
    prices_extrema, date_extrema, delta_y)

count_descending_rhombuses, res_descending_rhombuses = \
    figures.get_descending_rhombuses(prices_extrema)
d.draw_rhombuses(plt, res_descending_rhombuses, \
    prices_extrema, date_extrema, delta_y)

count_rising_rhombuses, res_rising_rhombuses = \
    figures.get_rising_rhombuses(prices_extrema)
d.draw_rhombuses(plt, res_rising_rhombuses, \
    prices_extrema, date_extrema, delta_y)

count_double_tops, res_double_tops = \
    figures.get_double_tops(prices_extrema)
d.draw_double_tops(plt, res_double_tops, \
    prices_extrema, date_extrema, delta_y)

count_triple_bottoms, res_triple_bottoms = \
    figures.get_triple_bottoms(prices_extrema)
d.draw_triple_bottoms(plt, res_triple_bottoms, \
    prices_extrema, date_extrema, delta_y)

count_head_and_shoulders, res_head_and_shoulders = \
    figures.get_head_and_shoulders(prices_extrema)
d.draw_head_and_shoulders(plt, res_head_and_shoulders, \
    prices_extrema, date_extrema, delta_y)

count_reversed_head_and_shoulders, res_reversed_head_and_shoulders = \
    figures.get_reversed_head_and_shoulders(prices_extrema)
d.draw_head_and_shoulders(plt, res_reversed_head_and_shoulders, \
    prices_extrema, date_extrema, delta_y)

count_falling_wedges, res_falling_wedges = \
    figures.get_falling_wedges(prices_extrema)
d.draw_wedges(plt, res_falling_wedges, prices_extrema, \
    date_extrema, True, delta_y)

count_rising_wedges, res_rising_wedges = \
    figures.get_rising_wedges(prices_extrema)
d.draw_wedges(plt, res_rising_wedges, prices_extrema, \
    date_extrema, False, delta_y)

c = count_pennants + count_descending_flags + count_rising_flags + \
    count_rectangles + count_descending_rhombuses + \
count_rising_rhombuses + count_double_tops + count_triple_bottoms + \
    count_head_and_shoulders + count_reversed_head_and_shoulders + \
count_falling_wedges + count_rising_wedges

plt.show()

print(f'Общее количество найденных фигур: {c}')

print_statistics('вымпел', res_pennants, count_pennants, \
    prices_extrema, 1, c)
print_statistics('нисходящий флаг', res_descending_flags, \
    count_descending_flags, prices_extrema, 2, c)
print_statistics('восходящий флаг', res_rising_flags, \
    count_rising_flags, prices_extrema, 3, c)
print_statistics('прямоугольник', res_rectangles, \
    count_rectangles, prices_extrema, 4, c)
print_statistics('восходящий ромб', res_rising_rhombuses, \
    count_rising_rhombuses, prices_extrema, 5, c)
print_statistics('нисходящий ромб', res_descending_rhombuses,\
    count_descending_rhombuses, prices_extrema, 6, c)
print_statistics('голова и плечи', res_head_and_shoulders, \
    count_head_and_shoulders, prices_extrema, 7, c)
print_statistics('перевернутые голова и плечи', \
    res_reversed_head_and_shoulders, \
        count_reversed_head_and_shoulders, prices_extrema, 7, c)

print(f'pennants {count_pennants}')
print(f'descending_flags {count_descending_flags}')
print(f'rising_flags {count_rising_flags}')
print(f'rectangles {count_rectangles}')
print(f'descending_rhombuses {count_descending_rhombuses}')
print(f'rising_rhombuses {count_rising_rhombuses}')
print(f'head_and_shoulders {count_head_and_shoulders}')
print(f'reversed_head_and_shoulders \
    {count_reversed_head_and_shoulders}')
