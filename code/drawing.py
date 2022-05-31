def draw_pennants_rising_flags(plt, indexes, prices, date, delta):
    for index in indexes:
        x_upper_line = [date[index], date[index + 4]]
        y_upper_line = [prices[index], prices[index + 4]]
        plt.plot(x_upper_line, y_upper_line)
        x_lower_line = [date[index + 1], date[index + 5]]
        y_lower_line = [prices[index + 1], prices[index + 5]]
        plt.plot(x_lower_line, y_lower_line, color='red')
        if prices[index - 1] < prices[index]:
            x_rising_line = [date[index + 5], date[index + 8]]
            y_rising_line = [prices[index + 5], prices[index + 5] + delta]
            plt.plot(x_rising_line, y_rising_line, color='red')


def draw_descending_flags(plt, indexes, prices, date, delta):
    for index in indexes:
        x_upper_line = [date[index], date[index + 4]]
        y_upper_line = [prices[index], prices[index + 4]]
        plt.plot(x_upper_line, y_upper_line)
        x_lower_line = [date[index + 1], date[index + 5]]
        y_lower_line = [prices[index + 1], prices[index + 5]]
        plt.plot(x_lower_line, y_lower_line, color='red')
        if prices[index - 1] > prices[index]:
            x_rising_line = [date[index + 5], date[index + 8]]
            y_rising_line = [prices[index + 5], prices[index + 5] + delta]
            plt.plot(x_rising_line, y_rising_line, color='red')


def draw_rectangles(plt, indexes, prices, date, delta):
    for index in indexes:
        x_upper_line = [date[index + 1], date[index + 7]]
        y_upper_line = [prices[index + 1], prices[index + 7]]
        plt.plot(x_upper_line, y_upper_line, color='red')
        x_lower_line = [date[index], date[index + 6]]
        y_lower_line = [prices[index], prices[index + 6]]
        plt.plot(x_lower_line, y_lower_line, color='red')
        x_line = [date[index + 7], date[index + 10]]
        y_line_2nd_arg = prices[index + 7] - delta if \
             prices[index] < prices[index - 1] else \
                  prices[index + 7] + delta
        y_line = [prices[index + 7], y_line_2nd_arg]
        plt.plot(x_line, y_line, color='red')


def draw_rhombuses(plt, indexes, prices, date, delta):
    for index in indexes:
        y_middle_value = (prices[index + 4] + prices[index + 3]) / 2

        x_1st_line = [date[index - 1], date[index + 4]]
        y_1st_line = [y_middle_value, prices[index + 4]]
        plt.plot(x_1st_line, y_1st_line, color='red')

        x_2nd_line = [date[index + 4], date[index + 9]]
        y_2nd_line = [prices[index + 4], y_middle_value]
        plt.plot(x_2nd_line, y_2nd_line, color='red')

        x_3rd_line = [date[index + 9], date[index + 4]]
        y_3rd_line = [y_middle_value, prices[index + 4]]
        plt.plot(x_3rd_line, y_3rd_line, color='red')

        x_4th_line = [date[index + 4], date[index - 1]]
        y_4th_line = [prices[index + 4], y_middle_value]
        plt.plot(x_4th_line, y_4th_line, color='red')

        y_value_line = prices[index + 8] + delta if \
            prices[index] < prices[index - 1] else \
                prices[index + 8] - delta
        y_values_line = [prices[index + 8], y_value_line]
        x_values_line = [date[index + 9], date[index + 13]]
        plt.plot(x_values_line, y_values_line, color='red')


def draw_double_tops(plt, indexes, prices, date, delta):
    for index in indexes:
        x_upper_line = [date[index - 2], date[index + 4]]
        y_upper_line = [prices[index], prices[index]]
        plt.plot(x_upper_line, y_upper_line)
        x_lower_line = [date[index - 2], date[index + 4]]
        y_lower_line = [prices[index + 1], prices[index + 1]]
        plt.plot(x_lower_line, y_lower_line, color='red')
        if prices[index] > prices[index - 1]:
            y_line = [prices[index + 2], prices[index + 2] - delta]
            x_line = [date[index + 2], date[index + 5]]
            plt.plot(x_line, y_line)


def draw_triple_bottoms(plt, indexes, prices, date, delta):
    for index in indexes:
        x_upper_line = [date[index + 1], date[index + 3]]
        y_upper_line = [prices[index + 1], prices[index + 1]]
        plt.plot(x_upper_line, y_upper_line)
        x_lower_line = [date[index], date[index + 4]]
        y_lower_line = [prices[index], prices[index + 4]]
        plt.plot(x_lower_line, y_lower_line, color='red')
        if prices[index] < prices[index - 1]:
            x_line = [date[index + 4], date[index + 7]]
            y_line = [prices[index + 4], prices[index + 4] + delta]
            plt.plot(x_line, y_line)


def draw_head_and_shoulders(plt, indexes, prices, date, delta):
    for index in indexes:
        x_line = [date[index - 1], date[index + 5]]
        y_line = [prices[index + 1], prices[index + 1]]
        plt.plot(x_line, y_line, color='red')
        x_line = [date[index + 4], date[index + 7]]
        y_value = prices[index + 4] - delta if \
            prices[index] > prices[index - 1] else prices[index + 4] + delta
        y_line = [prices[index + 7], y_value]
        plt.plot(x_line, y_line)


def draw_wedges(plt, indexes, prices, date, flag, delta_y):
    # Флаг нужен для отрисовки нисходящих / восходящих
    delta = 4 if flag else 6
    for index in indexes:
        x_upper_line = [date[index], date[index + delta]]
        y_upper_line = [prices[index + 1], prices[index + delta]]
        plt.plot(x_upper_line, y_upper_line)
        x_lower_line = [date[index + 1], date[index + 5]]
        y_lower_line = [prices[index + 1], prices[index + 5]]
        plt.plot(x_lower_line, y_lower_line, color='red')
        x_line = [date[index + delta], date[index + delta + 3]]
        y_line_1st = prices[index + delta] + delta_y if delta == 5 else \
             prices[index + delta] - delta_y
        y_line_2nd = prices[index + delta]
        y_line = [y_line_2nd, y_line_1st]
        plt.plot(x_line, y_line)
