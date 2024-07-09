class NumberToFrench:

    def __init__(self, number: int) -> None:
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

    def __triple_digit_to_word(self, num: int) -> str | None:
        """
        Convert triplets of numbers to words
        """
        str_num = str(num)
        # if its less than 3 digits or if the number starts with 0
        if len(str_num) < 3 or str_num[0] == "0":
            return self.__double_digit_to_word(int(str_num))
        else:
            first_digit, rest = str_num[0], str_num[1:3]
            if first_digit == 1:
                return f"cent {self.__double_digit_to_word(int(rest))}"
            else:
                return f"{self.__digits_to_words[int(first_digit)]} cent {self.__double_digit_to_word(int(rest))}"

    def __double_digit_to_word(self, num: int) -> str | None:
        """
        Function that receives a number up to 2 digits and turns it to a word string
        """
        if num == 0:
            return None
        if num < 19:
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
                    return f"{self.__tens[first_num]}-{self.__digits_to_words[second_num]}"
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
        Splits the word in chunks of three, then converts each chunk of three numbers to words.

        In any chunk apart from the first one appends special words (million, mille etc)
        """
        # convert the number to string for easier parsing
        str_num = str(self.number)[::-1]
        if len(str_num) > 9:
            raise Exception("Supported numbers up to 9 digits")
        elif self.number == 0:
            return "zero"
        words = []
        # split the word in chunks of 3
        chunks = [str_num[i : i + 3] for i in range(0, len(str_num), 3)]
        # Reverse each chunk and then reverse the list of chunks
        reversed_chunks = [chunk[::-1] for chunk in chunks]
        # iterate chunks and build the word
        for idx, chunk in enumerate(reversed_chunks):
            if idx in self.__chunk_idx_to_special_word:
                words.append(self.__chunk_idx_to_special_word[idx])
            word = self.__triple_digit_to_word(int(chunk))
            if word:
                words.append(word)
        return " ".join(reversed(words))
