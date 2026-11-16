class Person:
    # counts instances created
    count = 0
    old_name = "Trial"
    def __init__(self, name):
        self.name = name
        Person.count += 1

    # @classmethod
    # def change_name(self, new_name):
    #     self.old_name = new_name
    #     return f"The name of {self.old_name} was changed to {new_name}"

    @classmethod
    def get_instance_count(cls):
        return f"There are {cls.count} instances"

    


guy1 = Person("Bob")
guy2 = Person("Sansum")
print(Person.get_instance_count())
# print(Person.change_name("Speaker"))
