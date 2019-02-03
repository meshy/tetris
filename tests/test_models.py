from tetris.models import pieces, Piece


def test_next_piece():
    first_piece = Piece('I', 0)
    second_piece = first_piece.next_piece()
    assert second_piece.get_matrix() == pieces['I'][1]

def test_matrix():
    piece = Piece('I', 0)
    assert piece.get_matrix() == pieces['I'][0]

def test_wrapping():
    first_piece = Piece('I', 3)
    second_piece = first_piece.next_piece()
    assert second_piece.get_matrix() == pieces['I'][0]
