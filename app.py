def unit_convert(value, initial_unit, convert_to_unit):
    units = {"cm": 0.01, "m": 1}
    result = value*(units[initial_unit]/units[convert_to_unit])
    string = f"{result}{convert_to_unit}"
    print(string)
    return string