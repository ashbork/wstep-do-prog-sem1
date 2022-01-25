import math
from typing import Iterable


def normalize(floats: Iterable[float]) -> list[float]:
    sqrsum = sum([x**2 for x in floats])
    result = []
    for num in floats:
        num /= (math.sqrt(sqrsum))
        result.append(num)
    return result


print(normalize((2.2, 5.6, 4.3, 3.0, 0.5)))
