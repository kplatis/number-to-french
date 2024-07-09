from number_to_french import NumberToFrench


def test_number_to_word():

    result = NumberToFrench(0).__double_digit_to_word(4)
    assert result == "quatre"
    result = NumberToFrench(0).__double_digit_to_word(17)
    assert result == "dix-sept"
    result = NumberToFrench(0).__double_digit_to_word(30)
    assert result == "trente"
    result = NumberToFrench(0).__double_digit_to_word(51)
    assert result == "cinquante-et-un"
    result = NumberToFrench(0).__double_digit_to_word(63)
    assert result == "soixante-trois"
    result = NumberToFrench(0).__double_digit_to_word(73)
    assert result == "soixante-treize"
    result = NumberToFrench(0).__double_digit_to_word(80)
    assert result == "quatre-vingt"
    result = NumberToFrench(0).__double_digit_to_word(86)
    assert result == "quatre-vingt-six"
    result = NumberToFrench(0).__double_digit_to_word(90)
    assert result == "quatre-vingt-dix"
    result = NumberToFrench(0).__double_digit_to_word(99)
    assert result == "quatre-vingt-dix-neuf"


def test_triple_digit_to_word():
    result = NumberToFrench(0).__triple_digit_to_word(305)
    assert result == "trois cent cinq"
    result = NumberToFrench(0).__triple_digit_to_word(888)
    assert result == "huit cent quatre-vingt-huit"


def test_build_word():
    result = NumberToFrench(9).to_french_word()
    assert result == "neuf"
    result = NumberToFrench(16).to_french_word()
    assert result == "seize"
    result = NumberToFrench(105).to_french_word()
    assert result == "un cent cinq"
    result = NumberToFrench(10000).to_french_word()
    assert result == "dix mille"
    result = NumberToFrench(1653).to_french_word()
    assert result == "un mille six cent cinquante-trois"
    result = NumberToFrench(5135000).to_french_word()
    assert result == "cinq millions un cent trente-cinq mille"
    result = NumberToFrench(1005321).to_french_word()
    assert result == "un millions cinq mille trois cent vingt-et-un"
    result = NumberToFrench(289005321).to_french_word()
    assert (
        result
        == "deux cent quatre-vingt-neuf millions cinq mille trois cent vingt-et-un"
    )
    result = NumberToFrench(25021).to_french_word()
    assert result == "vingt-cinq mille vingt-et-un"
