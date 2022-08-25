PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names:
    name = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letters:
    letter = letters.read()
    for n in name:
        stripped_name = n.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt",
                  mode="w") as complete_letter:
            complete_letter.write(new_letter)
