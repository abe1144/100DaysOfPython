# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".


with open("./input/letters/starting_letter.txt") as f:
    letter = f.read()

print(letter)

with open("./input/names/invited_names.txt") as f:
    names = f.read()

name_list = names.split("\n")

for name in name_list:
    new_letter = letter.replace("[name]", name)
    with open("./output/readytosend/letter_for_{}".format(name), mode="w") as f:
        f.write(new_letter)
