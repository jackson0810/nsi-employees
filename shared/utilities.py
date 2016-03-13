import string
import random
import re
import uuid

from django.conf import settings
from django.core.management import call_command


def make_uuid():
    return str(uuid.uuid4())


# Random Password Generator
def random_password_generator(size=10, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    symbols = '!@#$%^&*()'
    chars += symbols

    random_password = ''

    # require size of at least 10
    if size < 10:
        raise Exception('Cannot generate a random password of fewer than 8 characters.')

    # get the uppercase letter, lowercase letter, digit, and symbol required by the regex out of the way first
    # randomly choose order of required items so it's not the same for every random password
    choices = [string.ascii_uppercase, string.ascii_lowercase, string.digits, symbols]
    random.shuffle(choices)

    for c in choices:
        random_password += random.choice(c)

    # add random characters to achieve the desired final length
    for i in range(1, size - len(random_password) + 1):
        random_password += random.choice(chars)

    # final check to make sure it matches the regex before returning
    if not re.match(settings.PASSWORD_REGEX, random_password):
        raise Exception('The random password does not meet the complexity requirements.')

    return random_password


def collect_static():
    call_command('collectstatic', verbosity=0, interactive=False)

