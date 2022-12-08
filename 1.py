import re


def to_camel_case(text):
    return re.split('_|-', text)[0] + ''.join(word.title() for word in re.split('_|-', text)[1::])


print(to_camel_case('idk-what-to-write'))