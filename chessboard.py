from flask import Flask, request, jsonify
import queen, Knight, Rook, Bishop, King,Pawn

app = Flask(__name__)


def slug_check(data_slug, value_slug):
    if "Queen" == data_slug:
        return queen.all_possible_queen_moves(value_slug)
    elif "Bishop" == data_slug:
        return Bishop.all_possible_bishop_moves(value_slug)
    elif "Rook" == data_slug:
        return Rook.all_possible_rook_moves(value_slug)
    elif "Knight" == data_slug:
        return Knight.all_possible_knight_moves(value_slug)
    elif "King" == data_slug:
        return King.get_valid_king_moves(value_slug)
    elif "Pawn" == data_slug:
        return Pawn.get_valid_pawn_moves(value_slug)
    else:
        return jsonify({"Invalid Data": "Invalid Slug"})


@app.route('/chess/<string:slug>', methods=['POST'])
def chess_board(slug):
    if request.method != 'POST':
        return jsonify({'Error': 'Method not Allowed'}), 405
    valid_data = {}
    slug = slug.capitalize()
    valid_move = dict()
    data = request.get_json()
    if slug in data["postions"]:
        valid_data = set(slug_check(slug, data["postions"][slug]))
        del data["postions"][slug]
    else:
        return jsonify({"Invalid Data": "PLease send valid Json Combo"})
    for slug_key, value_slug in dict(data["postions"]).items():
        data_set = set(slug_check(slug_key, value_slug))
        valid_data.difference_update(data_set)
    valid_move['valid_moves'] = list(valid_data)
    if len(valid_move['valid_moves']) > 0:
        return jsonify(valid_move)
    else:
        return jsonify({"valid_moves": "No valid moves"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

