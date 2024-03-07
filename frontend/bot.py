# bot.py
def check_for_numbers(text):
    """
    Checks if the given text contains any numbers.

    Parameters:
        text (str): The text to check.

    Returns:
        str: A message indicating whether the text contains numbers or not.
    """
    if any(char.isdigit() for char in text):
        return "Have numbers"
    else:
        return "No numbers"
