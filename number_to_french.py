"""
NumberToFrench class converts numbers to french words
"""

from typing import Union


class NumberToFrench:
    """
    A class to convert numbers into their French word representation.

    Attributes:
    -----------
    number : int
        The number to be converted to French words.
    """

    def __init__(self, number: int) -> None:
        """
        Initializes the NumberToFrench class with the specified number.

        Parameters:
        -----------
        number : int
            The number to be converted to French words.
        """
        self.__digits_to_words = {
            1: "un",
            2: "deux",
            3: "trois",
            4: "quatre",
            5: "cinq",
            6: "six",
            7: "sept",
            8: "huit",
            9: "neuf",
            10: "dix",
            11: "onze",
            12: "douze",
            13: "treize",
            14: "quatorze",
            15: "quinze",
            16: "seize",
            17: "dix-sept",
            18: "dix-huit",
            19: "dix-neuf",
        }
        self.__tens = {
            1: "dix",
            2: "vingt",
            3: "trente",
            4: "quarante",
            5: "cinquante",
            6: "soixante",
        }
        self.__chunk_idx_to_special_word = {
            1: "mille",
            2: "millions",
        }

        self.number = number

    def _triple_digit_to_word(self, num: int) -> Union[str, None]:
        """
        Convert a number up to three digits to its French word representation.

        Parameters:
        -----------
        num : int
            The number to be converted.

        Returns:
        --------
        str | None
            The French word representation of the number, or None if the number is zero.
        """
        str_num = str(num)
        # if its less than 3 digits or if the number starts with 0
        if len(str_num) < 3 or str_num[0] == "0":
            return self._double_digit_to_word(int(str_num))
        else:
            first_digit, rest = str_num[0], str_num[1:3]
            if first_digit == 1:
                return f"cent {self._double_digit_to_word(int(rest))}"
            else:
                return f"{self.__digits_to_words[int(first_digit)]} cent {self._double_digit_to_word(int(rest))}"

    def _double_digit_to_word(self, num: int) -> Union[str, None]:
        """
        Convert a number up to two digits to its French word representation.

        Parameters:
        -----------
        num : int
            The number to be converted.

        Returns:
        --------
        str | None
            The French word representation of the number, or None if the number is zero.
        """
        if num == 0:
            return None
        if num < 20:
            return self.__digits_to_words[num]
        else:
            first_num, second_num = int(str(num)[0]), int(str(num)[1])
            # 20-69
            if num < 70:
                if second_num == 0:
                    return self.__tens[first_num]
                elif second_num == 1:
                    return f"{self.__tens[first_num]}-et-un"
                else:
                    return (
                        f"{self.__tens[first_num]}-{self.__digits_to_words[second_num]}"
                    )
            # 70-79
            elif num < 80:
                return f"soixante-{self.__digits_to_words[10 + second_num]}"
            # 80 +
            else:
                prefix = "quatre-vingt"
                if num < 90:
                    if second_num == 0:
                        return prefix
                    elif second_num == 1:
                        return f"{prefix}-et-un"
                    else:
                        return f"{prefix}-{self.__digits_to_words[second_num]}"
                else:
                    return f"{prefix}-{self.__digits_to_words[10 + second_num]}"

    def to_french_word(self) -> str:
        """
        Convert the number to its French word representation.

        Splits the number into chunks of three digits, converts each chunk to words,
        and appends special words (e.g., 'million', 'mille') where necessary.

        Returns:
        --------
        str
            The French word representation of the number.

        Raises:
        -------
        ValueError
            If the number has more than 9 digits.
        """
        if self.number < 0:
            raise ValueError("Number cannot be negative")
        # convert the number to string for easier parsing
        str_num = str(self.number)[::-1]
        if len(str_num) > 9:
            raise ValueError("Supported numbers up to 9 digits")
        elif self.number == 0:
            return "zéro"
        words = []
        # split the word in chunks of 3
        chunks = [str_num[i : i + 3] for i in range(0, len(str_num), 3)]
        # Reverse each chunk and then reverse the list of chunks
        reversed_chunks = [chunk[::-1] for chunk in chunks]
        # iterate chunks and build the word
        for idx, chunk in enumerate(reversed_chunks):
            if idx in self.__chunk_idx_to_special_word:
                words.append(self.__chunk_idx_to_special_word[idx])
            word = self._triple_digit_to_word(int(chunk))
            if word:
                words.append(word)
        return " ".join(reversed(words))
