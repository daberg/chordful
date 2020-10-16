from chordful.database import initdb
import chordful.chordlang

import flask
import json


def runApp(configPath):
    with open(configPath) as f:
        config = json.load(f)

    app = flask.Flask(__name__)

    # Init database; routes are closures w.r.t. the db variable
    db = initdb(config)

    def show_pieces(startfrom):
        numentries = 25

        morepieces = db.get_pieces(numentries + 1, startfrom=startfrom)

        hasprev = startfrom > 0
        hasnext = morepieces and len(morepieces) > numentries

        pieces = morepieces[0:-1] if hasnext else morepieces

        prevfrom = max(0, startfrom - numentries) if hasprev else None
        nextfrom = startfrom + numentries if hasnext else None

        return flask.render_template( 'pieces.html.jinja'
                                    , pieces=pieces
                                    , prevfrom=prevfrom
                                    , nextfrom=nextfrom
                                    )

    @app.route('/')
    def index():
        return flask.render_template('index.html.jinja')

    @app.route('/pieces/')
    def show_pieces_from_first():
        return show_pieces(0)

    @app.route('/pieces/from=<int:piece_number>')
    def show_pieces_from_id(piece_number):
        return show_pieces(piece_number)

    @app.route('/piece/<pieceid>')
    def show_piece(pieceid):
        piece = db.get_piece(pieceid)

        if not piece:
            return ("<h1>404 - resource not found</h1>", 404)

        piece["chords"] = chordful.chordlang.tohtml(piece["chords"])

        return flask.render_template('piece.html.jinja', piece=piece)

    @app.route('/postpiece', methods=['POST'])
    def save_piece():
        reqdata = flask.request.get_json()

        title = reqdata["title"]
        artist = reqdata["artist"]
        chords = reqdata["chords"]

        db.store_piece({"title" : title, "artist" : artist, "chords" : chords})

        return ("Succesfully stored piece", 200)

    app.run(host='0.0.0.0')
