row1 = ["😀", "😀", "😀"]
row2 = ["😂", "😂", "😂"]
row3 = ["😹", "😹", "😹"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
"""split variable position """
horizontal = int(position[0])
vertical = int(position[1])
#get selected row
#selected_row = map[vertical - 1]
#selected_row[horizontal - 1] = "X"
map[vertical - 1][horizontal - 1] = "X"


#specify conditions int the list


print(f"{row1}\n{row2}\n{row3}")
