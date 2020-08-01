FROM python:3
EXPOSE 8090

RUN apt-get clean && apt-get -y update

WORKDIR /taller

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]
