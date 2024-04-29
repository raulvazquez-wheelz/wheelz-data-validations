from wheelz_idp_validations.sanitizers.id_number import sanitize_id_number
from wheelz_idp_validations.sanitizers.gender import sanitize_gender
from wheelz_idp_validations.sanitizers.date import sanitize_dates

def sanitize_id(response_dict):
    # Sanitize ID Number
    try: 
        response_dict["documentNumber"] = sanitize_id_number(response_dict["documentNumber"], False)
    except Exception as e:
        response_dict["documentNumber"] = ""
        print("Error sanitizing document number:", str(e))
    
    # Sanitize Gender
    try:
        response_dict["gender"] = sanitize_gender(response_dict["gender"])
    except Exception as e:
        response_dict["gender"] = ""
        print("Error sanitizing gender:", str(e))
    
    # Sanitize Birth Date and Expiration Date
    try:
        response_dict["birthDate"] = sanitize_dates(response_dict["birthDate"])
    except Exception as e:
        response_dict["birthDate"] = ""
        print("Error sanitizing birth date:", str(e))

    try:
        response_dict["expirationDate"] = sanitize_dates(response_dict["expirationDate"])
    except Exception as e:
        response_dict["expirationDate"] = ""
        print("Error sanitizing expiration date:", str(e))

    return response_dict

