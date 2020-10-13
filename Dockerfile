FROM python:3-alpine

WORKDIR /srv/chordful

COPY . .

RUN pip install -r requirements.txt . && \
    addgroup -S chordful && \
    adduser -S -g chordful chordful && \
    chown -R chordful:chordful /srv/chordful && \
    chmod -R 700 /srv/chordful

USER chordful:chordful

CMD python3 -m chordful
