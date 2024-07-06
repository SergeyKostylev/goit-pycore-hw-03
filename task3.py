import re


# task 3

def normalize_phone(phone_number: str):
    prepared_number = re.findall(r'\+|\d*', phone_number)
    prepared_number = "".join(prepared_number)

    if (re.match(r'^\+', prepared_number)):
        prefix = ''
    else:
        prefix = '+' if (re.match('^38', prepared_number)) else '+38'

    # TODO: maybe need to think about the condition and if after preparation strlen of the result not equal 13 return None

    return f"{prefix}{prepared_number}"


# print(normalize_phone("(050)123-32-34"))
