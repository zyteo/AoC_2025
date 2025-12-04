# function takes in number range, output the list of numbers
def get_number_list(number_range):
    holder_list = []
    min, max = number_range.split("-")
    for i in range(int(min), int(max) + 1):
        # count length of string in i. if odd, ignore.
        if len(str(i)) % 2 != 0:
            continue
        else:
            # split number into two halves. if exactly the same, add into list
            length = len(str(i))
            first_half = str(i)[: length // 2]
            second_half = str(i)[length // 2 :]
            if first_half == second_half:
                holder_list.append(i)

    return holder_list


def main():
    invalid_list = []

    with open("./input2", "r") as f:
        # split by coma
        number_ranges = f.read().split(",")

    for number_range in number_ranges:
        # if output list is empty, no need to proceed
        output_list = get_number_list(number_range)
        if len(output_list) == 0:
            continue
        else:
            invalid_list.extend(output_list)
    print(invalid_list)

    sum = 0
    for invalid in invalid_list:
        sum += invalid
    print(f"Sum of all invalid numbers: {sum}")


if __name__ == "__main__":
    main()
