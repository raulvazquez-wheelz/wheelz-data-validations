import re
import logging
from datetime import datetime

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def sanitize_dates(text):
    # Comprobar si la entrada es una cadena vacía o solo contiene espacios
    if not text.strip():
        logging.info("Empty input received for date.")
        return ""  # Retornar cadena vacía directamente si no hay entrada

    date_pattern = r'\b(\d{2})[\/\s-](\d{2})[\/\s-](\d{4})\b'
    
    try:
        match = re.search(date_pattern, text)
        if match:
            day, month, year = match.groups()
            iso_formatted_date = f"{year}-{month}-{day}"
            datetime.strptime(iso_formatted_date, "%Y-%m-%d")  # Validar fecha
            return iso_formatted_date
        else:
            # Registra que no se encontró una fecha válida
            logging.warning(f"No valid date found in text: '{text}'")
            return ""  # Retornar cadena vacía si no se encuentra fecha
    except ValueError as e:
        # Registra el error específico con la fecha incorrecta
        logging.error(f"Invalid date format or logic error: {e}")
        return ""  # Retornar cadena vacía si la fecha es inválida
