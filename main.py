# importing required modules
import os
import sys
import argparse
import shutil
from validators import domains_validator, redirect_domain_validator
from scripts import write_nginx_configuration
# create a parser object
parser = argparse.ArgumentParser(description="NGINX proyect configurator.")

# add arguments
parser.add_argument("--domains", nargs="+", type=str, metavar="str",
                    help="Dominio con www y sin www. Ej: example.com www.example.com")

parser.add_argument("--redirect", nargs="?", type=str, metavar="str",
                    help="Dominio sin www a donde se va a redirigir. Ej: example.com")

# parse the arguments from standard input
args = parser.parse_args()

columns = shutil.get_terminal_size().columns

if not os.geteuid() == 0:
    print("\n**** Error: Debes correr el script como usuario root. \n")
    sys.exit()


domains = args.domains
redirect_domain = args.redirect

# Validations
domain_verification = domains_validator(domains)
if not domain_verification["valid"]:
    print(domain_verification["message"])
    sys.exit()

if redirect_domain:
    redirect_domain_verification = redirect_domain_validator(redirect_domain)
    if not redirect_domain_verification["valid"]:
        print(redirect_domain_verification["message"])
        sys.exit()

# Corriendo configuraciones
nginx_configuration_result = write_nginx_configuration(domains, redirect_domain)
if not nginx_configuration_result["valid"]:
    print(nginx_configuration_result["message"])
    sys.exit()
