FROM python:3.9

RUN apt-get update && \
    apt-get install -y libpq-dev postgresql-client python3-dev

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x execute.sh

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENTRYPOINT [ "/bin/bash" ]
CMD [ "./execute.sh" ]
