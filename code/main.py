import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import figures
import drawing as d
plt.figure(figsize=(30, 20))


def print_statistics(figure_name, indexes, col, prices, flag, c):
    print(f'Стастистика по фигуре {figure_name}:')
    print(f'Всего найдено: {col}, что составляет {round(col / c, 3)} \
        от общего числа фигур')
    res = []
    # pennants
    if flag == 1:
        for index in indexes:
            res.append([1 if prices[index] > prices[index - 1] and \
                prices[index + value] > prices[index + 5] else 0
                        for value in range(6, 11)])
    #flags
    if flag == 2:
        for index in indexes:
            res.append([1 if prices[index] < prices[index - 1] and \
                prices[index + value] > prices[index + 5] or
                             prices[index] > prices[index - 1] and \
                                 prices[index + 6] < prices[index + value] else 0
                        for value in range(6, 11)])
    #rectangles
    if flag == 3:
        for index in indexes:
            res.append([1 if prices[index] > prices[index - 1] and \
                prices[index + 7] < prices[index + value] or
                             prices[index] < prices[index - 1] and \
                                 prices[index + 7] > prices[index + value] else 0
                        for value in range(8, 13)])
    #rhombuses
    if flag == 4:
        for index in indexes:
            res.append([1 if prices[index] > prices[index - 1] and \
                prices[index + 8] > prices[index + value] or
                             prices[index] < prices[index - 1] and \
                                 prices[index + 8] < prices[index + value] else 0
                        for value in range(9, 14)])
    #head_and_shoulders
    else:
        for index in indexes:
            res.append([1 if prices[index] > prices[index - 1] and \
                 prices[index + 4] < prices[index + value] or
                             prices[index] < prices[index - 1] and \
                                 prices[index + 4] > prices[index + value] \
                                      else 0
                        for value in range(5, 10)])

    for subres in res:
        print(subres)


def get_extrema(date, prices):
    indexes = []
    for i in range(1, len(prices) - 1):
        if prices[i] > prices[i - 1] and prices[i] > prices[i + 1] or \
                prices[i] < prices[i - 1] and prices[i] < prices[i + 1]:
           indexes.append(i)

    return [date[index] for index in indexes], \
        [prices[index] for index in indexes]


data = yf.Ticker("AAPL").history(period='max')
prices = np.array(data['High'])
data.reset_index(inplace=True)
date = np.array(data['Date'], dtype='datetime64[D]')

delta_y = (max(prices) - min(prices)) / 10
date_extrema, prices_extrema = get_extrema(date, prices)
# plt.plot(date_extrema, prices_extrema, color='red')
plt.plot(date, prices)
count_pennants, res_pennants = figures.get_pennants(prices_extrema)
d.draw_pennants_rising_flags(plt, res_pennants, prices_extrema, \
    date_extrema, delta_y)

count_descending_flags, res_descending_flags = figures.get_descending_flags(\
    prices_extrema)
d.draw_descending_flags(plt, res_descending_flags, prices_extrema, \
    date_extrema, delta_y)

count_rising_flags, res_rising_flags = figures.get_rising_flags(prices_extrema)
d.draw_pennants_rising_flags(plt, res_rising_flags, prices_extrema, \
    date_extrema, delta_y)

count_rectangles, res_rectangles = figures.get_rectangles(prices_extrema)
d.draw_rectangles(plt, res_rectangles, prices_extrema, date_extrema, delta_y)

count_descending_rhombuses, res_descending_rhombuses = figures.get_descending_rhombuses(\
    prices_extrema)
d.draw_rhombuses(plt, res_descending_rhombuses, prices_extrema, \
    date_extrema, delta_y)

count_rising_rhombuses, res_rising_rhombuses = figures.get_rising_rhombuses(\
    prices_extrema)
d.draw_rhombuses(plt, res_rising_rhombuses, prices_extrema, \
    date_extrema, delta_y)

count_double_tops, res_double_tops = figures.get_double_tops(prices_extrema)
d.draw_double_tops(plt, res_double_tops, prices_extrema, date_extrema, delta_y)

count_triple_bottoms, res_triple_bottoms = figures.get_triple_bottoms(prices_extrema)
d.draw_triple_bottoms(plt, res_triple_bottoms, prices_extrema, \
    date_extrema, delta_y)

count_head_and_shoulders, res_head_and_shoulders = figures.get_head_and_shoulders(\
    prices_extrema)
d.draw_head_and_shoulders(plt, res_head_and_shoulders, prices_extrema, \
    date_extrema, delta_y)

count_reversed_head_and_shoulders, res_reversed_head_and_shoulders = \
    figures.get_reversed_head_and_shoulders(prices_extrema)
d.draw_head_and_shoulders(plt, res_reversed_head_and_shoulders, \
    prices_extrema, date_extrema, delta_y)

count_falling_wedges, res_falling_wedges = figures.get_falling_wedges(prices_extrema)
d.draw_wedges(plt, res_falling_wedges, prices_extrema, \
    date_extrema, True, delta_y)

count_rising_wedges, res_rising_wedges = figures.get_rising_wedges(prices_extrema)
d.draw_wedges(plt, res_rising_wedges, prices_extrema, \
    date_extrema, False, delta_y)

plt.show()
c = count_pennants + count_descending_flags + count_rectangles + \
    count_descending_rhombuses + count_rising_rhombuses \
      + count_double_tops + count_head_and_shoulders + \
          count_reversed_head_and_shoulders + count_falling_wedges \
      + count_rising_wedges

print(f'Общее количество найденных фигур: {c}')

# print_statistics('вымпел', res_pennants, count_pennants, prices_extrema, 1, c)
# pennants, \
# descending_flags, \
# rising_flags, \
# rectangles, \
# descending_rhombuses, \
# rising_rhombuses, \
# head_and_shoulders, \
# reversed_head_and_shoulders, \


# double_tops, \
# triple_bottoms, \
# falling_wedges, \
# rising_wedges, \

# rising_triangles, \
# falling_triangles
