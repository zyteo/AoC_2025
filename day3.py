def get_joltage(line):
    line_length = len(line)
    greatest_first_digit = line[0]
    print(greatest_first_digit)
    greatest_first_digit_index = 0
    # stop at the second last digit
    for i in range(1, line_length - 1):
        if greatest_first_digit < line[i]:
            greatest_first_digit_index = i
            greatest_first_digit = line[i]

    greatest_second_digit = line[greatest_first_digit_index + 1]
    greatest_second_digit_index = greatest_first_digit_index + 1
    if greatest_second_digit_index == line_length - 1:
        pass
    else:
        for j in range(greatest_second_digit_index + 1, line_length):
            if greatest_second_digit < line[j]:
                greatest_second_digit_index = j
                greatest_second_digit = line[j]

    # combine to form the greatest number
    greatest_number = int(greatest_first_digit + greatest_second_digit)
    print(f"Greatest number from line {line} is {greatest_number}")
    return greatest_number


def main():
    sum = 0

    with open("./input3", "r") as f:
        # split by coma
        number_lines = f.read().splitlines()

    for line in number_lines:
        # if output list is empty, no need to proceed
        output_joltage = get_joltage(line)
        sum = sum + output_joltage

    print(f"Sum of all invalid numbers: {sum}")


if __name__ == "__main__":
    main()
