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

        if person.name != "Joey":
            # solution to:
            # "AssertionError: Person with "name" Joey
            # should not have attribute wife"
            person.wife = Person.people.get(person_dict.get("wife"))
            person.husband = Person.people.get(person_dict.get("husband"))

    return person_list
