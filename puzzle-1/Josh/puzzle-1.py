
elves = []

with open('input.txt') as input_file:
    elf_total = 0
    for line in input_file:
        if line != '\n':
            elf_total = elf_total + int(line)
        else:
            elves.append(elf_total)
            elf_total = 0

print("carrying most:", max(elves))