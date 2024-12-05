class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person_dict["name"],
               person_dict["age"])
        for person_dict in people]

    for person_dict in people:
        person = Person.people[person_dict["name"]]

        if "wife" in person_dict and person_dict["wife"]:
            person.wife = Person.people.get(person_dict["wife"])
        if "husband" in person_dict and person_dict["husband"]:
            person.husband = Person.people.get(person_dict["husband"])

    return person_list


# class Person:
#     people = {}
#
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age
#         Person.people[name] = self
#
#
# def create_person_list(people: list) -> list:
#     pass
#     person_list = []
#     for person_dict in people:
#         person = Person(person_dict["name"], person_dict["age"])
#         person_list.append(person)
#
#     for person in person_list:
#         for person_dict in people:
#             if person_dict["name"] == person.name:
#                 if "wife" in person_dict:
#                     if person_dict["wife"] is not None:
#                         person.wife = Person.people[person_dict["wife"]]
#                 if "husband" in person_dict:
#                     if person_dict["husband"] is not None:
#                         person.husband = Person.people[
#                         person_dict["husband"]]
#     return person_list
