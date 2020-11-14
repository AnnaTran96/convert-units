def unit_convert(value, initial_unit, convert_to_unit):
    units = {"cm": 0.01, "m": 1}
    result = value*(units[initial_unit]/units[convert_to_unit])
    string = f"{result}{convert_to_unit}"
    print(string)
    return string

def run_script(TEST=False):
    while True:
        try:
            user_input = input("Enter the string to convert [x unit1 in unit2]\nType 'exit' if you wish to quit the app:\n")
            if user_input == 'exit':
                break
            user_input = user_input.split()
            outcome = unit_convert(int(user_input[0]), user_input[1], user_input[3])
            if TEST:
                return outcome
            else:
                continue
        except ValueError as e:
            print(f"ValueError: {e}\nFor example, type the following: 5 cm in m\n")
        except KeyError as e:
            print(f"KeyError: invalid key {e}.\nPlease enter correct unit [cm / m]\n")
        except KeyboardInterrupt as e:
            print(f"KeyboardInterrupt: {e}")
        except IndexError as e:
            print(f"IndexError: {e}")


if __name__ == "__main__":
    run_script(False)
