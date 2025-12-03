# Starts at 50, left is decrease and right is increase
# dial is from 0 to 99. Everytime stops at 0 after full rotation, add to counter


# function takes in current number and input, returns final number and counter
def dial_counter(current, input):
    counter = 0
    # split input from first character. if L is decrease, if R is increase
    direction = input[0]
    steps = int(input[1:])
    steps = steps % 100
    if direction == "L":
        if current > steps:
            current = current - steps
        elif current == steps:
            current = 0
            counter = counter + 1
        else:
            current = 100 - (steps - current)
    elif direction == "R":
        if current + steps < 100:
            current = current + steps
        elif current + steps == 100:
            current = 0
            counter = counter + 1
        else:
            current = (current + steps) - 100

    return current, counter


# test out one random input R31
def main():
    current = 50
    total_counter = 0
    inputs = ["R31"]
    for input in inputs:
        current, counter = dial_counter(current, input)
        total_counter += counter
    print(f"Final position: {current}, Total full rotations: {total_counter}")

if __name__ == "__main__":
    main()