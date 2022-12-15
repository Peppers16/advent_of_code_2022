
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

# I am not feeling hardcore enough to do a sorting algorithm from scratch
elves.sort()
print("top three:", elves[-3:])
print("which totals:", sum(elves[-3:]))