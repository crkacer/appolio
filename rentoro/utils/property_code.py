import random
import string

def generate_unique_property_code():
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=7))
