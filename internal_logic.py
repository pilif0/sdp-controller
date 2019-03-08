import json
import client as cl



def parseJson(jsonfile):
    with open('test.json') as f:
        data = json.load(f)
    move_count = data["move_count"]
    move_data = data["history"]["move_count"]

     _from = move_data["from"]
    to = move_data["to"]

    rowA, colA = _from[:1], int(_from[1:])
    cellA = (rowA,colA)

    rowB, colB = to[:1], int(to[1:])
    cellB = (rowB,colB)

    # Do take_piece
    if(move_data["capture"]["capture"]) {
        piece = move_data["capture"]["capture"]["piece"]
        cl.take_piece(cellA, cellB, piece)
    }
    # Do castling
    elif(move_data["castle"]["castle"]) {

        cl.perform_castling_at(cellA, cellB, cellC, cellD)
    }
    # Do en_passant
    elif(move_data["en_passant"]["en_passant"]) {
        piece = ["piece"]
        cellTake = move_data["en_passant"]["en_passant"]["square"]
        cl.en_passant(cellA, cellB, cellTake, piece)
    }
    # Do move_piece
    else {
        cl.move_piece(cellA, cellB)
    }

parseJson(jsonfile)