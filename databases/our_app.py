import database

# add a record to the database
# database.add_one("Laura", "Smith", "laura@smith.com")

# delete a record from the database (id needs to be a string, not an int)
# database.delete_one('6')

# add many records
stuff = [
    ('Brenda', 'Smitherton', 'brenda@smitherton.com'),
    ('Joshua', 'Raintree', 'josh@raintreecom')
    ]
# database.add_many(stuff)

# lookup email address record
database.email_lookup("john@codemy.com")

# see all records
# database.show_all()
