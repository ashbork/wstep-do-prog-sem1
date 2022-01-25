
def format_bytes(number: int) -> str:
    if not isinstance(number, int):
        raise TypeError(f"expected integer")
    if number > (1024 ** 9):
        raise ValueError(
            f"can't handle more than 1023 yobibytes (got {number})")
    units = ("bytes", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB")
    results = []
    for unit in units:
        if not number:
            break
        remainder = number % 1024
        if remainder:
            results.append(f'{remainder} {unit} + ')
        number = number // 1024
        print(remainder, number, unit)
    return "".join(reversed(results)).strip("+ ")


print(format_bytes(1208925819614629174706176123))
