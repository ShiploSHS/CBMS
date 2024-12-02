class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}, Address: {self.address}"

    def to_dict(self):
        return {
            'name': self.name,
            'phone_number': self.phone_number,
            'email': self.email,
            'address': self.address
        }
