from collections import UserDict


class Field:
    def __init__(self, value):
        """
        конструктор класу Record
        """
        self.value = value

    def __str__(self):
        """
        Магичний метод для відображення об'єкту класа Field
        """
        return str(self.value)


class Name(Field):
    # реалізація класу
		pass


class Phone(Field):
    """
    Клас Phone:
    Реалізовано валідацію номера телефону (має бути перевірка на 10 цифр).
    Наслідує клас Field. Значення зберігaється в полі value .
    """
    def __setattr__(self, value, new_val):
        """
        магичний метот, який перевіряє значення на корректність
        Якщо значення корректне, воно присвоюється атрибуту, якщо ні - викидається виключення ValueError
        """
        if type(new_val) != str or len(new_val) != 10 or not new_val.isdigit():
            raise ValueError('Введіть корректний номер телефона. Повинно бути 10 цифр')
        object.__setattr__(self, value, new_val)

                
class Record:
    """
    Клас Record:
    Реалізовано зберігання об'єкта Name в атрибуті name.
    Реалізовано зберігання списку об'єктів Phone в атрибуті phones.
    """
    def __init__(self, name):
        """
        конструктор класу Record
        """
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        """
        Магичний метод для відображення об'єкту класа Record
        """
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self, phone: str) -> None:
        """
        метод для додавання - add_phone .
        На вхід подається рядок, який містить номер телефона.
        """
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        """
        метод для видалення - remove_phone. 
        На вхід подається рядок, який містить номер телефона.
        """
        phone_obj = self.find_phone(phone)
        if phone_obj is not None: self.phones.remove(phone_obj)

   

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """
        метод для редагування - edit_phone. 
        На вхід подається два аргумента - рядки, які містять старий номер телефона та новий. 
        У разі некоректності вхідних даних метод має завершуватись помилкою ValueError.
        """
        if self.find_phone(old_phone) is not None:
            self.remove_phone(old_phone)
            self.add_phone(new_phone)
        else:
            raise ValueError ("Номера, який ви хочете відредагувати не існує")

    def find_phone(self, phone: str)-> Phone|None:
        """
        find_phone - метод пошуку номеру телефона
        На вхід подається рядок, який містить номер телефона. Метод має повертати або об’єкт Phone, або None .
        """
        phone = Phone(phone)
        for ph_obj in self.phones:
            if phone.value == ph_obj.value:
                return ph_obj



class AddressBook(UserDict):
    """
    Клас AddressBook:
    Має наслідуватись від класу UserDict .
    """
    # реалізація класу
    def __str__(self):
        """метод для красивого відображення класу"""
        return '\n'.join([str(v) for v in self.data.values()])
        
    def add_record(self, record: Record)-> None:
        """метод для запису нових даних до контакту"""
        self.data[record.name.value] = record
        
    def find(self, name: str) -> Record|None:
        """метод для пошуку запису у контакті за ім'ям. 
        Отримує строковий аргумент name. Повертає об'єкт Record або None"""
        return self.data.get(name, None)
    
    def delete(self, name: str) -> None:
        """метод для пошуку запису у контакті за ім'ям. 
        Отримує строковий аргумент name."""
        self.data.pop(name, None)


if __name__ == '__main__':
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543260")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
        
    print(book)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112444333")
    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
    john.remove_phone("1112444333")

    print(john)  # Виведення: Contact name: John, phones: 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
    print(book)