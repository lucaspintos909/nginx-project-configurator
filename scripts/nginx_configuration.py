import os
from .config_template import get_config_template, get_html_template

NGINX_PATH = "/etc/nginx"
PROJECTS_PATH = "/var/www/html"


def get_nginx_configuration(domains: list) -> str:
    www_domain = domains[0] if "www" in domains[0] else domains[1]
    non_www_domain = domains[0] if not "www" in domains[0] else domains[1]
    configuration = get_config_template(www_domain, non_www_domain)
    return configuration

# TODO: Hacer validaciones de si los comandos se ejecutan de manera correcta
def write_nginx_configuration(domains:  str) -> dict:
    # Obtengo dominio sin prefijo www
    non_www_domain = domains[0] if not "www" in domains[0] else domains[1]

    # Genero configuraciones
    nginx_conf_string = get_nginx_configuration(domains)
    html_template = get_html_template(non_www_domain)

    # Creo archivo de configuracion de Nginx
    nginx_file_path = f"{NGINX_PATH}/sites-available/{non_www_domain}"
    with open(nginx_file_path, "w") as conf_file:
        conf_file.write(nginx_conf_string)

    # Si no existe creo link simbolico para habilitar la configuracion
    if not os.path.exists(f"{NGINX_PATH}/sites-enabled/{non_www_domain}"):
        os.symlink(nginx_file_path, f"{NGINX_PATH}/sites-enabled/{non_www_domain}")

    # Reinicio servicio de NGINX
    os.system("systemctl restart nginx")

    # Verifico si existe el directorio del proyecto
    # y si no existe lo creo
    project_path = f"{PROJECTS_PATH}/{non_www_domain}"
    if not os.path.exists(project_path):
        os.mkdir(project_path)

    # Creo el index.html de prueba si no existe
    if not os.path.exists(f"{project_path}/index.html"):
        with open(f"{project_path}/index.html", "w") as html_file:
            html_file.write(html_template)

    result = {"message": "", "valid": True}
    return result
