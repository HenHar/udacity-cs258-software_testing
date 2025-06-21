# concise definition of the Luhn checksum:
#
# "For a card with an even number of digits, double every odd numbered
# digit and subtract 9 if the product is greater than 9. Add up all
# the even digits as well as the doubled-odd digits, and the result
# must be a multiple of 10 or it's not a valid card. If the card has
# an odd number of digits, perform the same addition doubling the even
# numbered digits instead."
#
# for more details see here:
# http://www.merriampark.com/anatomycc.htm
#
# also see the Wikipedia entry, but don't do that unless you really
# want the answer, since it contains working Python code!
#
# Implement the Luhn Checksum algorithm as described above.

def get_luhn_checksumm(n: int):
    return


# is_luhn_valid takes a credit card number as input and verifies
# whether it is valid or not. If it is valid, it returns True,
# otherwise it returns False.
def is_luhn_valid(n: int):
    return get_luhn_checksumm(n) == 0


# so now lets generate random VALID credit card numbers
def generate(prefix: int, n: int):
    # 1. find how many nums we need to fill up to limit n
    # 2. get random data and build credit card num
    # 3. correct that num
    # 4. return
    card_num = str(prefix)
    return