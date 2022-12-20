from random import randint

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [{
                "id": self._generateId(),
                "first_name": "John",
                "last_name": self.last_name,
                "age": 7,
                "lucky_numbers": [7, 13, 22] },

            {
                "id": self._generateId(),
                "first_name": "Janet",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": [10, 14, 3] },

            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": self.last_name,
                "age": 12,
                "lucky_numbers": [1] }]

    
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        self._members.append(member)
        return None

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
        pass

    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member

    
    def get_all_members(self):
        return self._members