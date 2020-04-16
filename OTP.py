am = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
}

# return letter = a - b


def letter_compute(a, b):
    num = am[a] - am[b]
    if num <= 0:
        num += 26

    for letter, numeric in am.items():
        if num == numeric:
            return letter

# return strA - strB


def guess_compute(strA, strB):
    ans = ""
    for i in range(len(strA)):
        ans += letter_compute(strA[i], strB[i])

    return ans


def string_compute(string, guess):
    len_g = len(guess)
    for i in range(0, len(string), len_g):
        substring = string[i:i+len_g]
        if len(substring) == len_g:
            print(guess_compute(substring, guess))


string1 = "LpaGbbfctNiPvwdbjnPuqolhhtygWhEuafjlirfPxxl".lower()
string2 = "WdafvnbcDymxeeulWOtpoofnilwngLhblUfecvqAxs".lower()
string3 = "UijMltDjeumxUnbiKstvdrVhcoDasUlrvDypegublg".lower()
string4 = "LpaAlrhGmjikgjdmLlcsnnYmIsoPcglaGtKeQcemiu".lower()
string5 = "LpaDohqcOzVbglebjPdTnoTzbyRbuwGftflTliPiqp".lower()

s = [string1, string2, string3, string4, string5]

#KEY: rhvnwynxzttsmipsvgkzyzpyokjsnozwxaxzddl
# KEY_GUESS: rhvnwynxzttsmipsvgkzyzpyokjsnozwxaxzddlhwo

# MSG1: The secret to winning eurovision is excellent hair
# MSG2: Everyone deserves a hippopotamus when theyre sad
# MSG3: Can you please help oliver find the flux capacitor
# MSG4: The most important person in the world is me myself
# MSG5: The price of bitcoin is too damn high given the data

# First find OTP from guess: OTP = encryption - msg (guess)
string_compute(string5, 'rhvnwynxzttsmipsvgkzyzpyokjsnozwxaxzddlhwo')

# Final Key: rhvnwynxzttsmipsvgkzyzpyokjsnozwxaxzddlhwo
