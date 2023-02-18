# importing required modules
import os
import sys
import argparse
import shutil
from validators import domains_validator
from scripts import write_nginx_configuration
# create a parser object
parser = argparse.ArgumentParser(description="NGINX proyect configurator.")

# add arguments
parser.add_argument("--domains", nargs="+", type=str, metavar="str",
                    help="Dominio con www y sin www. Ej: example.com www.example.com")

# parse the arguments from standard input
args = parser.parse_args()

columns = shutil.get_terminal_size().columns

domains = args.domains

# Validations
domain_verification = domains_validator(domains)
if not domain_verification["valid"]:
    print(domain_verification["message"])
    sys.exit()

nginx_configuration_result = write_nginx_configuration(domains)
if not nginx_configuration_result["valid"]:
    print(nginx_configuration_result["message"])
    sys.exit()

""" if not result["valid"]:
  print(f"**** Error: {result['message']}".center(columns))
  sys.exit()

if os.name == "posix":
  os.system("clear")
else:
  os.system("cls") """

""" print(f"Password: {result['password']} \n".center(columns))
print(f"**** The password has been copied to the clipboard! ****".center(columns)) """
