def find_common_participants(list1, list2, delimiter=','):

    set1 = set(list1.split(delimiter))
    set2 = set(list2.split(delimiter))
    intersection_set = set1.intersection(set2)
    return sorted(intersection_set)

participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", common_participants)

