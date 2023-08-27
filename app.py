from peewee import * # Importing all from peewee

# Creating a database instance
db = PostgresqlDatabase('contacts', user='cli_user', password='', host='localhost', port=5432)

# Creating a base model class
class BaseModel(Model):
    class Meta:
        database = db

# Creating a contact model
class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    phone_number = CharField()

# Connecting to the database
db.connect()

# Dropping the tables
db.drop_tables([Contact])

# Creating the tables
db.create_tables([Contact])

# Creating a contact
def add_new_contact():
    first_name = input('Enter first name: ')
    last_name = input('Enter last name: ')
    phone_number = input('Enter phone number: ')

    contact = Contact(first_name=first_name, last_name=last_name, phone_number=phone_number)
    contact.save()
    print('Contact saved successfully!')

# Getting all contacts
def get_all_contacts():
    contacts = Contact.select()# Getting all contacts
    for contact in contacts:
        print(f'{contact.first_name} {contact.last_name} - Phone: {contact.phone_number}')

# Getting a contact by first name
def get_contact_by_first_name():
    first_name = input('Enter first name: ')
    contact = Contact.get(Contact.first_name == first_name)
    print(f'{contact.first_name} {contact.last_name} - Phone: {contact.phone_number}')

# Menu
running = True
while running:
    # Printing menu
    print('Welcome to the contacts app!')
    print('1. Add new contact')
    print('2. Get all contacts')
    print('3. Get contact by first name')
    print('4. Quit')

    # Getting user choice
    choice = int(input('Enter choice: '))

    # Handling user choice
    if choice == 1:
        add_new_contact()
    elif choice == 2:
        get_all_contacts()
    elif choice == 3:
        get_contact_by_first_name()
    elif choice == 4:
        break
    else:
        print('Invalid choice!')
        running = False

