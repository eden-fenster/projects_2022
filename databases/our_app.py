from database import Database

# add a record to the database
# database.add_one("Laura", "Smith", "laura@smith.com")

database_to_add = Database('customer.db')

# add a dictionary to the database
user1 = {"first_name": 'James', "last_name": 'Elder', "email_address": 'james@elder.com'}
# database_to_add.add_dict(user1)

# delete a record from the database (id needs to be a string, not an int)
# database_to_add.delete_one('6')

# add many records
stuff = [
    ('Brenda', 'Smitherton', 'brenda@smitherton.com'),
    ('Joshua', 'Raintree', 'josh@raintreecom')
    ]
# database_to_add.add_many(stuff)

# lookup email address record
# database_to_add.email_lookup("john@codemy.com")

# see all records
database_to_add.show_all()
