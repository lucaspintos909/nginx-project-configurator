# importing required modules
import os, sys, argparse, shutil
from validators import domains_validator

# create a parser object
parser = argparse.ArgumentParser(description="NGINX proyect configurator.")

# add arguments
parser.add_argument("--domains", nargs="+", type=str, metavar="str",
                    help="Dominio con www y sin www. Ej: example.com www.example.com")

# parse the arguments from standard input
args = parser.parse_args()

columns = shutil.get_terminal_size().columns

# Validations
domain_verification = domains_validator(args.domains)
if not domain_verification["valid"]:
  print(domain_verification["message"])
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