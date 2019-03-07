


def fizbuzz(num: int):
    """
    Will return fizz if divisible by 3, buzz if divisible by 5
    and fizzbuzz if divisible by both
    :param num:
    :return:
    """
    # for x in fizzbuzz(num):
    if num%3 == 0 and num%5 ==0 : return "fizzbuzz"
    if num%3 == 0: return "fizz"
    if num%5 == 0: return "buzz"
    return ""



