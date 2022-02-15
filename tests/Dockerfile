FROM postgres:14-alpine

RUN apk --no-cache add build-base jpeg-dev python3 python3-dev py3-pip zlib-dev

WORKDIR /usr/src/app/api

COPY ./api/requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install requests==2.27.1

COPY ./api .
RUN chmod +x execute.sh

WORKDIR /usr/src/app

COPY ./tests .
RUN chmod +x execute.sh

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

ENTRYPOINT [ "/bin/bash" ]
CMD [ "./execute.sh" ]
