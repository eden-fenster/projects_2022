from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:bul_pgia_records.db:', echo=False)
Base = declarative_base()
Base.metadata.create_all(engine)


class BulPgiaDatabase(Base):
    __tablename__ = 'bul_pgia_records'

    id = Column(Integer, primary_key=True)
    generated_number = Column(Integer)
    guessed = Column(String)
    number_of_guesses = Column(Integer)

    def __repr__(self):
        return "<BulPgiaDatabase(generated_number='%s', guessed='%s', number_of_guesses='%s')>" % (
            self.generated_number, self.guessed, self.number_of_guesses)


def add_one(generated_number: int, guessed: str, number_of_guesses: int):
    Session = sessionmaker(bind=engine)
    session = Session()
    record_to_add = BulPgiaDatabase(generated_number=generated_number,
                                    guessed=guessed, number_of_guesses=number_of_guesses)
    session.add(record_to_add)
    session.commit()


def show_all():
    Session = sessionmaker(bind=engine)
    session = Session()
    Query = session.query(BulPgiaDatabase).order_by(BulPgiaDatabase.id)
    name_list: list = Query.all()
    for name in name_list:
        print(name)
