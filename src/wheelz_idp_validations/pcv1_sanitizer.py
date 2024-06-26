from wheelz_idp_validations.sanitizers.plate import sanitize_plate
from wheelz_idp_validations.sanitizers.vin import sanitize_vin
from wheelz_idp_validations.sanitizers.date import sanitize_dates


def sanitize_pcv1(response_dict):
    # Sanitize Plate
    response_dict["matricula"] = sanitize_plate(response_dict["matricula"])
    # Sanitize VIN
    response_dict["serieNumBastidor"] = sanitize_vin(response_dict["serieNumBastidor"])
    # Sanitize multiple Dates
    response_dict["fechaMatriculacion"], response_dict["fechaPrimeraMatriculacion"] = (
        sanitize_dates(response_dict["fechaMatriculacion"], response_dict["fechaPrimeraMatriculacion"]))
