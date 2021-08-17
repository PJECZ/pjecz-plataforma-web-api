"""
Safe string
"""
import re
from datetime import date
from unidecode import unidecode


def safe_string(input_str):
    """Safe string"""
    if not isinstance(input_str, str):
        return ""
    new_string = re.sub(r"[^a-zA-Z0-9]+", " ", unidecode(input_str))
    removed_multiple_spaces = re.sub(r"\s+", " ", new_string)
    return removed_multiple_spaces.strip().upper()


def safe_message(input_str):
    """Safe message"""
    message = str(input_str)
    if message == '':
        message = "Sin descripción"
    return (message[:250] + '...') if len(message) > 250 else message


def safe_expediente(input_str):
    """Safe expediente"""
    if not isinstance(input_str, str) or input_str.strip() == "":
        return ""
    elementos = re.sub(r"[^0-9]+", "-", input_str).split("-")
    try:
        numero = int(elementos[0])
        ano = int(elementos[1])
    except (IndexError, ValueError) as error:
        raise error
    if numero < 0:
        raise ValueError
    if not 1925 <= ano <= date.today().year:
        raise ValueError
    return f"{str(numero)}/{str(ano)}"