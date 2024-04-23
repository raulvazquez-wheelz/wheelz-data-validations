import re


# TODO ADD PARAM TO FUNCTION TO SEARCH MULTIPLE DNI fitxer a originals
def sanitize_id_number(received_id):
    dni_regexp = "([0-9O]{8})([A-Z])"
    letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    not_valid = {"00000000T", "00000001R", "99999999R"}

    # Get only the ID number
    match = re.search(dni_regexp, received_id)

    # If there is no match, throw exception
    if not match:
        raise NoIDMatchFoundException(received_id)

    # Replace O (letter) for 0 (number) in case of errors
    processed_id = match.group(1).replace('O', '0')
    # Add the letter to the ID
    processed_id += match.group(2)

    # Received id cannot bet one of these: "00000000T", "00000001R", "99999999R"
    if processed_id in not_valid:
        raise InvalidIDException(received_id)

    # Getting the module of the number of the ID with 23, gives us the position of the letter
    # the ID should have on the defined letters array
    if not processed_id[8] == letters[int(processed_id[0:8]) % 23]:
        raise IDValidationFailedException(processed_id)

    # Return the valid id
    return processed_id
