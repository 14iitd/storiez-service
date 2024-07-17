import random
def convert_to_str(data):
    if isinstance(data, (int, float, bool, str, type(None))):
        # Keep primitive types as is
        return data
    elif isinstance(data, dict):
        # Convert dictionary values recursively
        return {key: convert_to_str(value) for key, value in data.items()}
    elif isinstance(data, (list, tuple)):
        # Convert list or tuple elements recursively
        return [convert_to_str(item) for item in data]
    elif isinstance(data, set):
        # Convert set elements recursively
        return {convert_to_str(item) for item in data}
    else:
        # Convert non-primitive types to string representation
        return str(data)


import re


def extract_hashtags(post_content):
    # Define a regular expression pattern for hashtags
    hashtag_pattern = r'#\w+'

    # Use re.findall to find all occurrences of the pattern in the post content
    hashtags = re.findall(hashtag_pattern, post_content)

    return hashtags

def generate_random_hex_code():
    # Generate random RGB values between 50 and 168
    red = random.randint(160, 240)
    green = random.randint(160, 245)
    blue = random.randint(160, 245)

    # Convert RGB values to hex format
    hex_code = "{:02X}{:02X}{:02X}".format(red, green, blue)

    return "#"+hex_code
def generate_random_hex_code_dark():
    # Generate random RGB values between 50 and 168
    red = random.randint(0, 100)
    green = random.randint(0, 100)
    blue = random.randint(0, 100)

    # Convert RGB values to hex format
    hex_code = "{:02X}{:02X}{:02X}".format(red, green, blue)

    return "#"+hex_code
import datetime
import secrets
import string
def is_weekend():
    today = datetime.datetime.now().weekday()
    # Check if today is Saturday (5) or Sunday (6)
    return today == 5 or today == 6

# Check if today is a weekend day
if is_weekend():
    print("It's a weekend!")
else:
    print("It's not a weekend.")
def generate_random_string(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))