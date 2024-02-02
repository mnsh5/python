names = ["mary", "Richard", "Noah", "KATE"]
processed_names = []

for name in names:
    processed_names.append(name.title())

names = ["mary", "Richard", "Noah", "KATE"]
processed_names = [name.title() for name in names]

names = ("mary", "Richard", "Noah", "KATE")
ages = (36, 21, 40, 28)

people = []

for name, age in zip(names, ages):
    person_data = (name.title(), age)
    people.append(person_data)

names = ("mary", "Richard", "Noah", "KATE")
ages = (36, 21, 40, 28)

people = [(name.title(), age) for name, age in zip(names, ages)]
