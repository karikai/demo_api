FROM python

COPY . /app

RUN pip install Flask && pip install pymongo

WORKDIR /app

CMD python3 /app/api.py
# CMD python3 api.py