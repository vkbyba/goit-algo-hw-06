from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name):
        super().__init__(name)

class Phone(Field):
    def __init__(self, phone_number):
        super().__init__(phone_number)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        if not (len(phone_number) == 10 and phone_number.isdigit()):
            print(f"Invalid phone number: {phone_number}")
            return
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        self.phones = [phone for phone in self.phones if phone.value != phone_number]

    def edit_phone(self, old_number, new_number):
        if not (len(new_number) == 10 and new_number.isdigit()):
            print(f"Invalid new phone number: {new_number}")
            return
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number
                return
        print(f"Old phone number {old_number} not found.")    

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(phone.value for phone in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
    

book = AddressBook()

john_record = Record("John")
john_record.add_phone('123456789A')
john_record.add_phone("5555555555")


book.add_record(john_record)

print(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)



john = book.find("John")
john_record.edit_phone("1234567890", "1112223333")


found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}") 
book.delete("Jane")
