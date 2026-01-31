class IntegerToRoman:
    def __init__(self, number):
        self.number = number

    def converttoroman(self):
        romanmap = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        result= ""
        num= self.number

        for value, symbol in romanmap:
            while num >= value:
                result += symbol
                num -= value

        return result

number= int(input("Enter an integer: "))
converter= IntegerToRoman(number)

print("Roman Numeral:", converter.converttoroman())
