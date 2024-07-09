from number_to_french import NumberToFrench


def test_number_to_word():

    result = NumberToFrench(0).number_to_word(4)
    assert result == "quatre"
    result = NumberToFrench(0).number_to_word(17)
    assert result == "dix-sept"
    result = NumberToFrench(0).number_to_word(30)
    assert result == "trente"
    result = NumberToFrench(0).number_to_word(51)
    assert result == "cinquante-et-un"
    result = NumberToFrench(0).number_to_word(63)
    assert result == "soixante-trois"
    result = NumberToFrench(0).number_to_word(73)
    assert result == "soixante-treize"
    result = NumberToFrench(0).number_to_word(80)
    assert result == "quatre-vingt"
    result = NumberToFrench(0).number_to_word(86)
    assert result == "quatre-vingt-six"
    result = NumberToFrench(0).number_to_word(90)
    assert result == "quatre-vingt-dix"
    result = NumberToFrench(0).number_to_word(99)
    assert result == "quatre-vingt-dix-neuf"
