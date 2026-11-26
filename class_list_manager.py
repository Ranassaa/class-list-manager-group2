# Class List Manager - Group2
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]

# ===== Each student adds her function BELOW this line =====
# Written by: Weam alhawas (task 1)
def count_names(names):
    count = 0
    for name in names:
        count = count + 1
    return count


def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    # Each student calls her function here, for example:
    print("Number of names:", count_names(names))


main()
