def count_str(list):
    str_count = 0
    for i in range(len(list)):
        first_letter = list[i][0].upper()
        last_letter = list[i][-1].upper()
        if first_letter == last_letter:
            str_count += 1
    return str_count

print(count_str(["Alisha", "bob", "mama", "oromo", "Ayana"]))