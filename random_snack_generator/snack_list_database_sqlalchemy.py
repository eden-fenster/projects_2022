from typing import List, Tuple

from sqlalchemy import create_engine, Column, Integer, String, func
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class FoodDatabaseRecord(Base):
    __tablename__ = 'food'

    id = Column(Integer, primary_key=True)
    food_name = Column(String)
    is_in_house = Column(String)

    def __repr__(self):
        return "<FoodDatabase(food_name='%s', is_in_house='%s')>" % (
            self.food_name, self.is_in_house)


class FoodDatabase:
    def __init__(self, data_base_file_name: str = 'sqlite:///food.db'):
        self._engine = create_engine(data_base_file_name, echo=False)
        Base.metadata.create_all(self._engine)
        Session = sessionmaker(bind=self._engine)
        self._session = Session()

    def add_one(self, food_name: str, is_in_house: str):
        record_to_add = FoodDatabaseRecord(food_name=food_name,
                                           is_in_house=is_in_house)
        self._session.add(record_to_add)
        self._session.commit()

    def add_many(self, list_of_food: List[Tuple[str, str]]):
        self._session.add_all(list_of_food)
        self._session.commit()

    def delete_one(self, delete: str):
        food_to_delete = self._session.query(FoodDatabaseRecord).filter(FoodDatabaseRecord.food_name == delete).first()
        self._session.delete(food_to_delete)
        self._session.commit()

    def delete_many(self, delete: str):
        food_to_delete = self._session.query(FoodDatabaseRecord).filter(FoodDatabaseRecord.food_name == delete).all()
        foods = food_to_delete
        for food in foods:
            self._session.delete(food)
            self._session.commit()

    def food_lookup_by_availability(self, is_in_house: str):
        foods_to_query = self._session.query(FoodDatabaseRecord).filter(FoodDatabaseRecord.is_in_house == is_in_house)
        foods = foods_to_query.all()
        for food in foods:
            print(food)

    def food_lookup_by_name(self, name: str):
        foods_to_query = self._session.query(FoodDatabaseRecord).filter(FoodDatabaseRecord.food_name.like(f'%{name}%'))
        foods = foods_to_query.all()
        for food in foods:
            print(food)

    def choose_random(self):
        Query = self._session.query(FoodDatabaseRecord).order_by(func.random()).first()
        random_snack = Query
        print(random_snack)

    def change_availability(self, food_to_change: str, the_opposite: str):
        snack_to_change = \
            self._session.query(FoodDatabaseRecord).filter(FoodDatabaseRecord.food_name == food_to_change).first()
        snack_to_change.is_in_house = the_opposite
        self._session.commit()

    def show_all(self):
        Query = self._session.query(FoodDatabaseRecord).order_by(FoodDatabaseRecord.id)
        record_list = Query.all()
        for record in record_list:
            print(record)
