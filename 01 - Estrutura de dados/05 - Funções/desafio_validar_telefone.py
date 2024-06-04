import re

def validate_numero_telefone(phone_number):
    pattern = r"\(\d{2}\) 9\d{5}-\d{4}"
    
    if re.match(pattern, phone_number):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."

print(validate_numero_telefone(input()))