def calc_delta(a, b, c):
    return (b * b) - (4 * a * c)


def calc_root(delta, a, b):
    if a == 0:
        raise "A 2nd degree polynom has 'a' different to 0."
    if delta < 0:
        raise "For a Real result, delta must be greather or equals to 0."

    delta_sqrt = delta ** (0.5)
    return (-b - delta_sqrt) / (2 * a), (-b + delta_sqrt) / (2 * a)
