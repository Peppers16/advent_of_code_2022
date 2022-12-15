
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
        self.contents = char_list
        self.compartment_1 = char_list[:split_point]
        self.compartment_2 = char_list[split_point:]

    def common_item(self):
        set_1 = set(self.compartment_1)
        set_2 = set(self.compartment_2)
        (common,) = set_1.intersection(set_2)  # the tuple unpacking is needed to get the one element out of the set
        return common


class ElfGroup:
    # sometimes I feel like object oriented programming just makes more work
    def __init__(self):
        self.elves = []

    def add_elf(self, elf):
        self.elves.append(elf)

    def is_full(self):
        return len(self.elves) >= 3

    def find_badge(self):
        set_1 = set(self.elves[0].contents)
        set_2 = set(self.elves[1].contents)
        set_3 = set(self.elves[2].contents)
        (common,) = set_1.intersection(set_2).intersection(set_3)
        return common


with open('input.txt') as input_file:

    total_priority = 0
    total_priority_p2 = 0
    elf_group = ElfGroup()

    for i, line in enumerate(input_file):
        rucksack = Rucksack(line)
        # Part 1: find item common between compartments
        priority = get_priority(rucksack.common_item())
        total_priority = total_priority + priority
        # Part 2:
        elf_group.add_elf(rucksack)
        if elf_group.is_full():
            badge = elf_group.find_badge()
            total_priority_p2 = total_priority_p2 + get_priority(badge)
            elf_group = ElfGroup()  # reset with new group


print("part 1:", total_priority)
print("part 2:", total_priority_p2)