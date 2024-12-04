def solve_first():
    count_save = 0
    with open('day02.txt', 'r') as file:
        for line in file:
            report = line.split()
            try:
                for idx, number in enumerate(report):
                    if idx != len(report) - 1:
                        next_number = int(report[idx + 1])
                        if next_number == int(number):
                            raise ValueError("Invalid number")
                        if idx == 0:
                            increasing = int(number) < next_number
                    if abs(int(number) - next_number) > 3:
                        raise ValueError("Invalid number")
                    if int(number) > next_number and increasing:
                        raise ValueError("Invalid number")
                    elif int(number) < next_number and not increasing:
                        raise ValueError("Invalid number")
                count_save += 1
            except ValueError:
                continue
    print(f"Total valid reports: {count_save}")


# def solve_second():
#     count_save = 0
#     with open('day02.txt', 'r') as file:
#         for line in file:
#             report = line.split()
#             count_errors = 0
#             last_number_idx = 0
#             for idx in range(len(report) - 1):
#                 try:
#                     last_number = int(report[last_number_idx])
#                     next_number = int(report[idx + 1])
#                     if next_number == last_number:
#                         raise ValueError("Invalid number")
#
#                     if idx == 0:
#                         increasing = last_number < next_number
#                         if (last_number < next_number) != (next_number < int(report[idx + 2])):
#                             increasing = not increasing
#                             last_number_idx += 1
#                             raise ValueError("Invalid number")
#
#                     if abs(last_number - next_number) > 3:
#                         raise ValueError("Invalid number")
#
#                     if last_number > next_number and increasing:
#                         raise ValueError("Invalid number")
#                     elif last_number < next_number and not increasing:
#                         raise ValueError("Invalid number")
#                     last_number_idx = idx + 1
#                 except ValueError:
#                     count_errors += 1
#                     # if count_errors > 1:
#                     #     print(f"Invalid report: {report}")
#                     #     break
#             if count_errors == 2:
#                 print(f"Invalid report: {report}")
#
#             if count_errors <= 1:
#                 count_save += 1
#     print(f"Total valid reports: {count_save}")

def solve_second():
    count_save = 0
    with open('day02.txt', 'r') as file:
        for line in file:
            report = line.split()
            error_idx = validate_report(report)
            if error_idx == -1:
                count_save += 1
            else:
                report.remove(report[error_idx])
                if validate_report(report) == -1:
                    count_save += 1
    print(f"Total valid reports: {count_save}")

def validate_report(report):
    try:
        for idx, number in enumerate(report):
            if idx != len(report) - 1:
                next_number = int(report[idx + 1])
                if next_number == int(number):
                    raise ValueError("Invalid number")
                if idx == 0:
                    increasing = int(number) < next_number
                if abs(int(number) - next_number) > 3:
                    raise ValueError("Invalid number")
                if int(number) > next_number and increasing:
                    raise ValueError("Invalid number")
                elif int(number) < next_number and not increasing:
                    raise ValueError("Invalid number")
        return -1
    except ValueError:
        return idx


if __name__ == '__main__':
    solve_first()
    solve_second()
