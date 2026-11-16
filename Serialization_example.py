import json

def process_json(data: dict, filename: str) -> dict:
    # Serializing and Saving into a file
    with open(filename, 'w') as file:
        json.dump(data, file)


    # Deserialization
    with open(filename, 'r') as file:
        return json.load(file)

result  = process_json({
    "name":"Userr",
    "age":"67"
}, "test.json")
print(result)


""""
Different Case to test
"""
class GFG_User:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

user = GFG_User("User","One")

# Serializing the data
print(user)
json_data = json.dumps(user.__dict__)
print("Serialized data")
print(json_data)

# Deserialized data
print("Deserialized data")
data_dict = json.loads(json_data)
deserialized_user = GFG_User(**data_dict)
print(deserialized_user)