class NumberToFrench:

    def __init__(self, number: int) -> None:
        self.digits_to_words = {
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
        self.tens = {
            1: "dix",
            2: "vingt",
            3: "trente",
            4: "quarante",
            5: "cinquante",
            6: "soixante",
        }
        self.number = number

    def number_to_word(self, num: int) -> str:
        """
        Function that receives a number up to 2 digits and turns it to a word string
        """
        if num < 16:
            return self.digits_to_words[num]
        else:
            first_num, second_num = int(str(num)[0]), int(str(num)[1])
            # 17-69
            if num < 70:
                if second_num == 0:
                    return self.tens[first_num]
                # special case where number has 1 as the second number => need to append "et"
                elif second_num == 1:
                    return f"{self.tens[first_num]}-et-un"
                else:
                    return f"{self.tens[first_num]}-{self.digits_to_words[second_num]}"
            # 70-79
            elif num < 80:
                return f"soixante-{self.digits_to_words[10+second_num]}"
            # 80-89
            elif num < 90:
                if second_num == 0:
                    return "quatre-vingt"
                elif second_num == 1:
                    return "quatre-vingt-et-un"
                else:
                    return f"quatre-vingt-{self.digits_to_words[second_num]}"
            else:
                return f"quatre-vingt-{self.digits_to_words[10+second_num]}"
