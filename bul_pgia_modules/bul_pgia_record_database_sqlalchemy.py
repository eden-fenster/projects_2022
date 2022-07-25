from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///bul_pgia_records.db', echo=False)
Base = declarative_base()


class BulPgiaDatabaseRecord(Base):
    __tablename__ = 'bul_pgia_records'

    id = Column(Integer, primary_key=True)
    generated_number = Column(Integer)
    guessed = Column(String)
    number_of_guesses = Column(Integer)

    def __repr__(self):
        return "<BulPgiaDatabase(generated_number='%s', guessed='%s', number_of_guesses='%s')>" % (
            self.generated_number, self.guessed, self.number_of_guesses)


class BulPgiaDatabase:
    def __init__(self, data_base_file_name: str = 'sqlite:///bul_pgia_records.db'):
        self._engine = create_engine(data_base_file_name, echo=False)
        Base.metadata.create_all(self._engine)
        Session = sessionmaker(bind=self._engine)
        self._session = Session()

    def add_one(self, generated_number: int, guessed: str, number_of_guesses: int):
        record_to_add = BulPgiaDatabaseRecord(generated_number=generated_number,
                                              guessed=guessed, number_of_guesses=number_of_guesses)
        self._session.add(record_to_add)
        self._session.commit()

    def show_all(self):
        Query = self._session.query(BulPgiaDatabaseRecord).order_by(BulPgiaDatabaseRecord.id)
        record_list = Query.all()
        for record in record_list:
            print(record)
