import hashlib

def hash_function(name):
    # Choose a suitable hashing algorithm (MD5, SHA-1, SHA-256)
    hash_value = hashlib.sha256(name.encode()).hexdigest()
    print("------", hash_value)
    return int(hash_value, 16) % 1000  # Adjust the table size as needed


def add_contact(name, phone_number):
    index = hash_function(name)
    if phonebook[index] is None:
        phonebook[index] = [(name, phone_number)]
    else:
        print(f"collision happens boom {phonebook[index]}")
        phonebook[index].append((name, phone_number))

def search_contact(name):
    index = hash_function(name)
    if phonebook[index] is not None:
        matching_contacts = []
        for contact in phonebook[index]:
            if contact[0] == name:
                matching_contacts.append(contact)
        return matching_contacts
    return None

def update_contact(name, new_name, new_phone_number):
    index = hash_function(name)
    if phonebook[index] is not None:
        for i, contact in enumerate(phonebook[index]):
            if contact[0] == name:
                phonebook[index][i] = (new_name, new_phone_number)
                return True
    return False


def delete_contact( name):
    index = hash_function(name)
    if phonebook[index] is not None:
        for i, contact in enumerate(phonebook[index]):
            if contact[0] == name:
                del phonebook[index][i]
                break

def get_all_contacts():
    for index, contacts in enumerate(phonebook):
        if contacts is not None:
            for contact in contacts:
                name, phone_number = contact
                print(f"Name: {name}, Phone Number: {phone_number}")

phonebook = [None] * 1000
add_contact("Jatin", "1234567890")
add_contact("Megha", "9876543210")
add_contact("Anusurya", "9057513312")
add_contact("Megha", "7754723092")


get_all_contacts()

phone_number = search_contact( "Megha")
print(phone_number)  # Output: 123-456-7890

# delete_contact(phonebook, "David")