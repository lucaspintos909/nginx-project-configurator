
def domains_validator(domains: list) -> dict:
    # TODO: Validar dominio con REGEX
    valid = True
    error_message = ""

    if valid and not len(domains) == 2:
        error_message += "\n**** Error: Debes indicar dos dominios, uno con prefijo www y otro sin.\n**** Ejemplo: example.com www.example.com\n"
        valid = False

    if valid and "www" not in domains[0] and "www" not in domains[1]:
        error_message += "\n**** Error: Debes indicar un dominio con prefijo www.\n**** Ejemplo: www.example.com\n"
        valid = False

    result = {"message": error_message, "valid": valid}

    return result

def redirect_domain_validator(domain: str) -> dict:
    # TODO: Validar dominio con REGEX
    valid = True
    error_message = ""

    if valid and "www" in domain:
        error_message += "\n**** Error: Debes indicar un dominio sin prefijo www.\n**** Ejemplo: example.com\n"
        valid = False

    result = {"message": error_message, "valid": valid}

    return result