from datetime import datetime
import re
import json

class Client:

    def __init__(self, surname, name, patronymic, address, phone):
        self.surname = self.validate_value(surname, "surname", is_required=True, only_letters=True)
        self.name = self.validate_value(name, "name", is_required=True, only_letters=True)
        self.patronymic = self.validate_value(patronymic, "patronymic", is_required=False, only_letters=True)
        self.address = self.validate_value(address, "address", is_required=True)
        self.phone = self.validate_value(phone, "phone", is_required=True, regex=r'^\+\d{1,3}-\d{3}-\d{3}-\d{4}$')

    @staticmethod
    def validate_value(value, field_name, is_required=True, only_letters=False, regex=None):
        if is_required and not value.strip():
            raise ValueError(f"{field_name} cannot be empty.")
        if only_letters and not value.replace(' ', '').isalpha():
            raise ValueError(f"{field_name} must contain only letters.")
        if regex and not re.match(regex, value):
            raise ValueError(f"{field_name} is invalid. Expected format: {regex}")
        return value

     @classmethod
    def from_string(cls, data_string, delimiter=","):
        fields = data_string.split(delimiter)
        if len(fields) != 5:
            raise ValueError("Data string must contain exactly 5 fields separated by the delimiter.")
        return cls(*[field.strip() for field in fields])

    @classmethod
    def from_json(cls, json_string):
        try:
            data = json.loads(json_string)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON: {e}")

        required_keys = ["surname", "name", "patronymic", "address", "phone"]
        if not all(key in data for key in required_keys):
            raise ValueError(f"JSON must contain the following keys: {', '.join(required_keys)}")

        return cls(
            surname=data["surname"],
            name=data["name"],
            patronymic=data["patronymic"],
            address=data["address"],
            phone=data["phone"]
        )

 def __str__(self):
        return (
            f"Full Details:\n"
            f"surname: {self.surname}\n"
            f"name: {self.name}\n"
            f"patronymic: {self.patronymic}\n"
            f"address: {self.address}\n"
            f"phone: {self.phone}"
        )

    def __repr__(self):
        return f"Client({self.name} {self.surname})"

    def __eq__(self, other):
        if not isinstance(other, Client):
            return NotImplemented
        return (self.surname == other.surname and
                self.name == other.name and
                self.patronymic == other.patronymic and
                self.address == other.address and
                self.phone == other.phone)
        
    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        self.__surname = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def patronymic(self):
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value):
        self.__patronymic = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value
