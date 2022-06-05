def make_bolting(indexes, delta):
    res = []
    if indexes:
        res.append(indexes[0])
    if len(indexes) > 1:
        for i in range(1, len(indexes) - 1):
            if indexes[i] - indexes[i + 1] <= delta and \
                indexes[i] - res[-1] <= delta:
                continue
            else:
                res.append(indexes[i])
    return res


def get_pennants(prices):
    res = []
    col = 0
    for i in range(0, len(prices) - 6):
        if prices[i] > prices[i + 2] > prices[i + 4] > \
            prices[i + 5] > prices[i + 3] > prices[i + 1]:
            res.append(i)
            col += 1
    return col, make_bolting(res, 6)


def get_descending_flags(prices):
    res = []
    col = 0
    eps = 1.25
    for i in range(0, len(prices) - 6):
        if prices[i] > prices[i + 2] > prices[i + 4] > \
            prices[i + 5] > prices[i + 3] > prices[i + 1] and \
                abs(prices[i] - prices[i + 4] - \
                    prices[i + 1] + prices[i + 5]) < eps:
            res.append(i)
            col += 1
    return col, make_bolting(res, 6)


def get_rising_flags(prices):
    res = []
    col = 0
    eps = 0.5
    for i in range(0, len(prices) - 6):
        if prices[i] < prices[i + 2] < prices[i + 4] < prices[i + 5] \
            and prices[i + 1] < prices[i + 3] < prices[i + 5] \
                and abs(prices[i] - prices[i + 4] - \
                    prices[i + 1] + prices[i + 5]) < eps:
            res.append(i)
            col += 1
    return col, make_bolting(res, 6)


def get_rectangles(prices):
    res = []
    col = 0
    eps = 0.15
    for i in range(len(prices) - 8):
        if abs(prices[i] - prices[i + 2]) < eps and \
            abs(prices[i + 2] - prices[i + 4]) < eps and \
                abs(prices[i + 4] - prices[i + 6]) < eps and \
                    abs(prices[i + 1] - prices[i + 3]) < eps and \
                abs(prices[i + 3] - prices[i + 5]) < eps and \
                    abs(prices[i + 5] - prices[i + 7]) < eps and \
                prices[i + 7] > prices[i + 6]:
            res.append(i)
            col += 1
    return col, make_bolting(res, 8)


def get_descending_rhombuses(prices):
    res = []
    col = 0
    eps = 0.40
    for i in range(len(prices) - 9):
        if prices[i + 2] < prices[i] < prices[i + 1] and \
            prices[i + 6] < prices[i + 8] < prices[i + 7] and \
                abs(prices[i + 3] - prices[i + 5]) < eps and \
                    abs(prices[i + 2] - prices[i + 6]) < eps and \
                prices[i + 4] < prices[i + 2] and \
                    abs(prices[i + 1] - prices[i + 7]) < eps and \
                abs(prices[i] - prices[i + 8]) < eps and \
                    prices[i + 3] > prices[i + 8]:
            res.append(i)
            col += 1
    return col, make_bolting(res, 9)


def get_rising_rhombuses(prices):
    res = []
    col = 0
    eps = 0.15
    for i in range(len(prices) - 9):
        if prices[i + 2] > prices[i] > prices[i + 1] and \
            prices[i + 6] > prices[i + 8] > prices[i + 7] and \
                abs(prices[i + 3] - prices[i + 5]) < eps and \
                    abs(prices[i + 2] - prices[i + 6]) < eps and \
                prices[i + 4] > prices[i + 2] and \
                    abs(prices[i + 1] - prices[i + 7]) < eps and \
                abs(prices[i] - prices[i + 8]) < eps and \
                    prices[i + 3] < prices[i + 8]:
            res.append(i)
            col += 1
    return col, make_bolting(res, 9)


def get_double_tops(prices):
    res = []
    col = 0
    eps = 0.1
    for i in range(1, len(prices) - 3):
        if prices[i - 1] < prices[i + 1] < prices[i] and \
            abs(prices[i] - prices[i + 2]) < eps:
            res.append(i)
            col += 1
    return col, make_bolting(res, 3)


def get_triple_bottoms(prices):
    res = []
    col = 0
    eps = 0.1
    for i in range(1, len(prices) - 5):
        if abs(prices[i] - prices[i + 2]) < eps and \
            abs(prices[i + 2] - prices[i + 4]) < eps and \
                abs(prices[i + 1] - prices[i + 3]) < eps and \
                    prices[i] < prices[i + 1] and \
                        prices[i] < prices[i - 1]:
            res.append(i)
            col += 1
    return col, make_bolting(res, 5)


def get_reversed_head_and_shoulders(prices):
    res = []
    col = 0
    eps = 0.1
    for i in range(1, len(prices) - 5):
        if prices[i] < prices[i - 1] and \
            abs(prices[i + 1] - prices[i + 3]) < eps and \
                abs(prices[i] - prices[i + 4]) < eps and \
                    prices[i + 1] > prices[i] > prices[i + 2]:
            res.append(i)
            col += 1
    return col, make_bolting(res, 5)


def get_head_and_shoulders(prices):
    res = []
    col = 0
    eps = 0.1
    for i in range(1, len(prices) - 5):
        if prices[i] > prices[i - 1] and \
            abs(prices[i + 1] - prices[i + 3]) < eps and \
                abs(prices[i] - prices[i + 4]) < eps and \
                    prices[i + 1] < prices[i] < prices[i + 2]:
            res.append(i)
            col += 1
    return col, make_bolting(res, 5)


def get_falling_wedges(prices):
    res = []
    col = 0
    for i in range(len(prices) - 6):
        if prices[i] > prices[i + 2] > prices[i + 4] > \
            prices[i + 5] and prices[i + 1] > \
                prices[i + 3] > prices[i + 5]:
            res.append(i)
            col += 1
    return col, make_bolting(res, 6)


def get_rising_wedges(prices):
    res = []
    col = 0
    for i in range(len(prices) - 7):
        if prices[i] < prices[i + 2] < prices[i + 4] < \
            prices[i + 6] and prices[i + 1] < \
                prices[i + 3] < prices[i + 5] < \
                    prices[i + 6]:
            res.append(i)
            col += 1
    return col, make_bolting(res, 7)


def get_rising_triangles(prices):
    res = []
    col = 0
    eps = 0.25
    for i in range(len(prices) - 7):
        if abs(prices[i + 1] - prices[i + 3]) < eps and \
            abs(prices[i + 3] - prices[i + 5]) < eps and \
                prices[i] < prices[i + 2] < prices[i + 4] < \
                    prices[i + 6] < prices[i + 5]:
            res.append(i)
            col += 1
        return col, make_bolting(res, 7)


def get_falling_triangles(prices):
    res = []
    col = 0
    eps = 0.25
    for i in range(len(prices) - 8):
        if abs(prices[i] - prices[i + 2]) < eps and \
            abs(prices[i + 2] - prices[i + 4]) < eps and \
                abs(prices[i + 4] - prices[i + 6]) < eps and \
                    prices[i + 6] < prices[i + 7] < prices[i + 5] < \
                prices[i + 3] < prices[i + 1]:
            res.append(i)
            col += 1
        return col, make_bolting(res, 8)
