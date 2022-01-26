
def format_bytes(number: int) -> str:
    if not isinstance(number, int):
        raise TypeError(f"expected integer (got {type(number)})")
    if number > (1024 ** 9):
        raise ValueError(
            f"can't handle more than 1023 yobibytes (got {number})")
    if number < 0:
        raise ValueError(f"expected positive integer (got {number})")
    units = ("bytes", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB")
    results = []
    # for each unit, until our number isn't zero
    for unit in units:
        if number == 0:
            break
        remainder = number % 1024
        if remainder != 0:
            results.append(f'{remainder} {unit}, ')
        number = number // 1024
    return "".join(reversed(results)).strip(", ")


print(format_bytes(1025))
