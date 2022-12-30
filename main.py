print("1 2 3")
print("4 5 6")
print("7 8 9")
list_ = [i + 1 for i in range(9)]
symb = " "
i = 0

def check_win():
    if list_[0] == list_[1] == list_[2] or list_[3] == list_[4] == list_[5] or list_[6] == list_[7] == list_[8] or list_[0] == list_[3] == list_[6] or list_[1] == list_[4] == list_[7] or list_[2] == list_[5] == list_[8] or list_[0] == list_[4] == list_[8] or list_[2] == list_[4] == list_[6]:
        print(f"Выиграл: {symb}")
        return True
    else:
        return False

while True:
    i = i + 1

    print(i)

    if i % 2 == 1:
        symb = "X"
    else:
        symb = "Y"

    k = int(input("Введите координаты от 1 до 9: "))

    if list_[k-1] != "X" and list_[k-1] != "Y":
        list_[k - 1] = symb
    else:
        print("Координаты заняты!")

    if check_win():
        break
