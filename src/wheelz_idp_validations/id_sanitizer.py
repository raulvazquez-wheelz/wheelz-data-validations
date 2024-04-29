from wheelz_idp_validations.sanitizers.id_number import sanitize_id_number
from wheelz_idp_validations.sanitizers.gender import sanitize_gender
from wheelz_idp_validations.sanitizers.full_name import sanitize_fullname
from wheelz_idp_validations.sanitizers.date import sanitize_dates


def sanitize_id(response_dict):
    # Sanitize ID Number
    response_dict["documentNumber"] = sanitize_id_number(response_dict["documentNumber"], False)
    # Sanitize Gender
    response_dict["gender"] = sanitize_gender(response_dict["gender"])
    # Sanitize ID Full Name
    (response_dict["name"], response_dict["firstSurname"],
     response_dict["secondSurname"]) = (
        sanitize_fullname(response_dict["name"], response_dict["firstSurname"],
                          response_dict["secondSurname"]))
    # Sanitize Birth Date and Expiration Date
    response_dict["birthDate"], response_dict["expirationDate"] = (
        sanitize_dates(response_dict["birthDate"], response_dict["expirationDate"]))
