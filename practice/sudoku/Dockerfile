FROM python:3.10.6

WORKDIR sudoku_server

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt


COPY sudoku_app.py ./
COPY sudoku.py ./
COPY sudoku_class.py ./

CMD [ "python3", "./sudoku_app.py"]
