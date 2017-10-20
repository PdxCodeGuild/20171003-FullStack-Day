"""
Lab 23: Contact List
Manage a list of contacts with a CSV file and a CRUDL REPL
"""


# load the contacts from the given CSV
def load(path):
    contacts = []
    header = None
    with open(path, 'r') as file:
        text = file.read()  # read all the text as one giant string
        lines = text.split('\n')  # split the text into multiple lines
        header = lines[0].split(',')  # the first line is the header
        for i in range(1, len(lines)):  # skip over the header, every line after represents a contact
            contact_values = lines[i].split(',')  # attribute values of the contact
            contact = {}  # start with an empty dictionary
            for j in range(len(header)):
                contact[header[j]] = contact_values[j]  # header[j] is the attribute name ('name', 'favorite fruit', etc)
            contacts.append(contact)

    return header, contacts


# save the list of contacts to a csv file
def save(path, header, contacts):
    output = ','.join(header)+'\n'
    for i in range(len(contacts)):
        for j in range(len(header)):
            output += contacts[i][header[j]]  # add the contact's attributes
            if j < len(header)-1:  # avoid adding an extra comma at the end
                output += ','
        if i < len(contacts)-1:  # avoid adding an extra newline at the end
            output += '\n'

    with open(path, 'w') as file:
        file.write(output)


def print_contact(contact):
    for key in contact:
        print(key + ': ' + contact[key])


def find_contact(name, contacts):
    for contact in contacts:
        if contact['name'] == name:
            return contact
    return None


def main():
    path = 'contacts.csv'
    header, contacts = load(path)

    while True:
        command = input('what operation would you like to perform? ')
        if command == 'help' or command == 'commands':
            print('create: create a contact')
            print('retrieve: retrieve a contact')
            print('update: update a contact')
            print('delete: delete a contact')
            print('help/commands: show this text')
            print('done: exit the program')
        elif command == 'done':
            break
        elif command == 'create':
            contact = {}
            for attribute_name in header:
                attribute_value = input('what is the contact\'s ' + attribute_name)
                contact[attribute_name] = attribute_value
            contacts.append(contact)
        elif command == 'retrieve':
            contact_name = input('what is the name of the contact you\'d like to retrieve? ')
            contact = find_contact(contact_name, contacts)
            if contact is None:
                print('contact not found')
            else:
                print_contact(contact)
        elif command == 'update':
            contact_name = input('what is the name of the contact you\'d like to update? ')
            contact = find_contact(contact_name, contacts)
            if contact is None:
                print('contact not found')
            else:
                attribute_name = input('what attribute would you like to set? ')
                attribute_value = input('what is that attribute\'s value? ')
                contact[attribute_name] = attribute_value
        elif command == 'delete':
            contact_name = input('what is the name of the contact you\'d like to delete? ')
            contact = find_contact(contact_name, contacts)
            contacts.remove(contact)
        elif command == 'list':
            for contact in contacts:
                print_contact(contact)
                print()
        else:
            print('command not recognized')

    save(path, header, contacts)

main()