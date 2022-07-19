from snack_list_database import RandomSnackGenerator

food_list = RandomSnackGenerator('food.db')

# add many records
stuff = [
    ('Apple', 1),
    ('Banana', 0)
]
food_list.add_many(stuff)

# see all records
food_list.show_all()
