FROM python:3
RUN git clone https://github.com/Lucasgarciamdz/4-en-linea-Lucasgarciamdz.git
WORKDIR 4-en-linea-Lucasgarciamdz
RUN pip install -r requirements.txt
CMD ["python3","-m", "unittest"]