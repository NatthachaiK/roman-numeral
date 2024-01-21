"""the Roman numeral module"""

def to_roman(arabic_num):
    """Convert Hindoo-arabic number to roman number."""
    
    # Storing roman values of digits from 0-9
    # when placed at different places
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]
 
    # Converting to roman
    thousands = m[arabic_num // 1000]
    hundreds = c[(arabic_num % 1000) // 100]
    tens = x[(arabic_num % 100) // 10]
    ones = i[arabic_num % 10]
 
    ans = (thousands + hundreds +
           tens + ones)
 
    return ans