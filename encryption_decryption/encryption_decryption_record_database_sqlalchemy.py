from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///encryption_decryption_records.db', echo=False)
Base = declarative_base()


class EncryptionDecryptionDatabase(Base):
    __tablename__ = 'encryption_decryption_records'

    id = Column(Integer, primary_key=True)
    original_text = Column(String)
    translated_text = Column(String)

    def __repr__(self):
        return "<EncryptionDecryptionDatabase(original_text='%s', translated_text='%s')>" % (
            self.original_text, self.translated_text)


Base.metadata.create_all(engine)


def add_one(original_text: str, translated_text: str):
    Session = sessionmaker(bind=engine)
    session = Session()
    record_to_add = EncryptionDecryptionDatabase(original_text=original_text,
                                                 translated_text=translated_text)
    session.add(record_to_add)
    session.commit()


def show_all():
    Session = sessionmaker(bind=engine)
    session = Session()
    Query = session.query(EncryptionDecryptionDatabase).order_by(EncryptionDecryptionDatabase.id)
    record_list = Query.all()
    for record in record_list:
        print(record)
