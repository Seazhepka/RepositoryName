def find_common_participants(str1, str2, sep=","):
    group1 = set(str1.split(sep))
    group2 = set(str2.split(sep))
    intersection_ = list(group1.intersection(group2))
    intersection_.sort()
    return intersection_


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, sep="|")
print("Список общих участников:", common_participants)
