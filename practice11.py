import functools


def sum(*arg: int):
    """
    임의의 개수의 인수를 받아서 그 합을 계산합니다.
    :param arg: 정수
    :return: 입력받은 값들의 합
    """
    return functools.reduce(lambda acc, x: acc+x, arg)


print(sum(10, 13, 14, 20))
