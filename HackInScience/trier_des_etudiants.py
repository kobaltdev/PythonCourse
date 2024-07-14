def sort_by_mark(students):
    students.sort(reverse = True)
    return students


def sort_by_name(students):
    students.sort(key = lambda x:x[1])
    return students



students = [(85, "Susan"), (6, "Joshua"), (37, "Jeanette")]
my_class = [(25, "Shannon"), (50, "Alan"), (75, "Ada")]

print(sort_by_mark(students))
print(sort_by_name(students))

print(sort_by_mark(my_class))
print(sort_by_name(my_class))

