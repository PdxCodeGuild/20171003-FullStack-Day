
# Lab: Contact List


Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together, and go over how to load that file. Headers might consist of `name`, `favorite fruit`, `favorite color`. Open the CSV, convert the lines of text into a **list of dictionaries**, one dictionary for each user. The text in the header represents the **keys**, the text in the other lines represent the **values**.

```python
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)
```

Once you've processed the file, your list of contacts will look something like this...
```python
contacts = [
    {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
    {'name':'sam', 'favorite fruit':'pineapple' ...}
]
```

## Version 2

Implement a CRUD REPL

- **C**reate a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
- **R**etrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
- **U**pdate a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
- **D**elete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.

## Version 3

When REPL loop finishes, write the updated contact info to the CSV file to be saved.

## Version 4 (optional)

Add a `phone number` column to the CSV, with each contact's phone number. We'll use the Twilio API to send SMS messages from the terminal.

Add an additional command to the REPL `send sms`, ask for the contact's name, and the message you'd like to send them.




```python
# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "XXXX"
auth_token = "XXXX"
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(to="<whatever you like>",
                                             from_="+19718033720",
                                             body="Hello there!")
```

    