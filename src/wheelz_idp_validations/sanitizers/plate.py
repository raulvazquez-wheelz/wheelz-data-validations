import re
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def sanitize_plate(text):
    # Definir patrones para los diferentes tipos de matrículas
    patterns = [
        r'\b\d{4}[BCDFGHJKLMNPQRSTVWXYZ]{3}\b',  # Tipo 1: 4 números seguidos de 3 letras no vocales
        r'\b[A-Z]{1,3}\d{6}\b',                  # Tipo 2: Hasta 3 letras seguidas de 6 números
        r'\b[A-Z]{1,2}\d{4}[A-Z]{1,2}\b',        # Tipo 3: 1-2 letras seguidas de 4 números y 1-2 letras
        r'\bR\d{3}[A-Z]{3}\b',                   # Tipo 4: Una R, 3 números y 3 letras
        r'\bH\d{4}[A-Z]{3}\b',                   # Tipo 5: Una H, 4 números y 3 letras
        r'\bC\d{4}[A-Z]{3}\b',                   # Tipo 6: Una C, 4 números y 3 letras
    ]

    # Comprobar si la entrada es una cadena vacía o solo contiene espacios
    if not text.strip():
        logging.info(f"Empty input received for plate processing: '{text}'")
        return ""  # Retornar cadena vacía directamente si no hay entrada

    # Buscar la primera matrícula que coincida con alguno de los patrones
    for pattern in patterns:
        match = re.search(pattern, text.upper().replace(' ', ''))
        if match:
            return match.group(0)
    
    # Registra que no se encontró una matrícula válida, incluyendo el texto original
    logging.warning(f"No valid plate found in text: '{text}'")
    return ""  # Retornar cadena vacía si no se encuentra matrícula
