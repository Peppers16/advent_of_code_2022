
def get_priority(char):
    ascii_value = ord(char)
    if ascii_value >= 97:
        return ascii_value - 96
    elif ascii_value <= 90:
        return ascii_value - 64 + 26
    else:
        print("You messed up")


class Rucksack:
    def __init__(self, string):
        char_list = list(string.rstrip('\n'))
        split_point = int(len(char_list) / 2)
        self.compartment_1 = char_list[:split_point]
        self.compartment_2 = char_list[split_point:]

    def common_item(self):
        set_1 = set(self.compartment_1)
        set_2 = set(self.compartment_2)
        (common,) = set_1.intersection(set_2)  # the tuple unpacking is needed to get the one element out of the set
        return common


with open('input.txt') as input_file:
    total_priority = 0
    for line in input_file:
        rucksack = Rucksack(line)
        priority = get_priority(rucksack.common_item())
        total_priority = total_priority + priority

print("part 1:", total_priority)