FROM python:3
RUN git clone https://github.com/AugustoKark/4enLineaAK.git
WORKDIR /4enLineaAK
RUN pip install -r requirements.txt
CMD ["python3","-m", "unittest"]