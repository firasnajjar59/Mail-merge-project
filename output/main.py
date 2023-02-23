list_names=[]
starter_letter=""
with open("./input/Names/names.txt") as names:
    data=names.read()
    list_names=list(data.split("\n"))
with open("./input/Letters/starting_letter.txt") as start_letter:
    data=start_letter.read()
    starter_letter=data

for letter in list_names:
    new_letter=starter_letter.replace("[name]",letter)
    with open(f"./output/ReadyToSend/Ready_to_send_{letter}.txt",mode="w") as file:
        file.write(new_letter)