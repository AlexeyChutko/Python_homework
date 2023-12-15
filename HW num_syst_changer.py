import string

# все возможные цифры

digits = string.digits + string.ascii_uppercase


def convert_to_decimal(num: str, syst_in: int) -> int:
    # Перевод числа в десятичную систему счисления

    decimal_num = 0

    for i, n in enumerate(num):
        decimal_num += digits.index(n.upper()) * (syst_in ** (len(num) - i - 1))
    return decimal_num


def convert_from_decimal(num: int, syst_out: int) -> str:
    # Перевод числа из десятичной системы счисления в любую другую

    out_num_list = []

    while num:
        out_num_list.append(digits[num % syst_out])
        num //= syst_out
    return ''.join(out_num_list[::-1])


def addition(syst_in: int, num1: str, num2: str, syst_out: int) -> str:
    # Числа в одинаковой системе счисления складываются и переводятся в другую систему счисления

    return convert_from_decimal(convert_to_decimal(num1, syst_in) +
                                convert_to_decimal(num2, syst_in), syst_out)
    
def addition111(syst_in: int, num1: str, num2: str, syst_out: int) -> str:
    # Числа в одинаковой системе переводятся в другую систему счисления и складываются в ней
    a = convert_from_decimal(convert_to_decimal(num1, syst_in), syst_out)
    b = convert_from_decimal(convert_to_decimal(num2, syst_in), syst_out)
    return a+b

syst_in = 2
num1 = '1101'
num2 = '1011'
syst_out = 10
print(addition(syst_in, num1, num2, syst_out))
print(addition111(syst_in, num1, num2, syst_out))
