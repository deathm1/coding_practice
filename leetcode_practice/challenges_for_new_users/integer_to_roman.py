def intToRoman(num: int):
    my_list = [
        ["I", 1],
        ["IV", 4],
        ["V", 5],
        ["IX", 9],
        ["X", 10],
        ["XL", 40],
        ["L", 50],
        ["XC", 90],
        ["C", 100],
        ["CD", 400],
        ["D", 500],
        ["CM", 900],
        ["M", 1000],

    ]
    my_roman_string = ""
    for symbol, value in reversed(my_list):
        if(num//value):
            count = num // value
            my_roman_string += symbol*count
            num = num%value
    return my_roman_string

print(intToRoman(1994))