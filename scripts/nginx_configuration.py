import os
from .config_template import get_config_template, get_html_template, get_config_redirection_template

NGINX_PATH = "/etc/nginx"
PROJECTS_PATH = "/var/www/html"


def get_nginx_configuration(domains: list, redirection) -> str:
    www_domain = domains[0] if "www" in domains[0] else domains[1]
    non_www_domain = domains[0] if not "www" in domains[0] else domains[1]

    if redirection:
        configuration = get_config_redirection_template(www_domain, non_www_domain, redirection)
    else:
        configuration = get_config_template(www_domain, non_www_domain)

    return configuration

# TODO: Hacer validaciones de si los comandos se ejecutan de manera correcta


def write_nginx_configuration(domains:  str, redirection=None) -> dict:
    errors = False
    # Obtengo dominio sin prefijo www
    non_www_domain = domains[0] if not "www" in domains[0] else domains[1]

    # Genero configuracion
    nginx_conf_string = get_nginx_configuration(domains, redirection)

    # Creo archivo de configuracion de Nginx
    nginx_file_path = f"{NGINX_PATH}/sites-available/{non_www_domain}"
    with open(nginx_file_path, "w") as conf_file:
        conf_file.write(nginx_conf_string)

    # Si no existe creo link simbolico para habilitar la configuracion
    if not os.path.exists(f"{NGINX_PATH}/sites-enabled/{non_www_domain}"):
        os.symlink(nginx_file_path,
                   f"{NGINX_PATH}/sites-enabled/{non_www_domain}")

    # Chequeo si la configuracion de nginx esta bien
    ext_code = os.system("nginx -t")

    # Reinicio servicio de NGINX
    if ext_code == 0:
        os.system("systemctl restart nginx")
    else:
        errors = True

    if not redirection:
        html_template = get_html_template(non_www_domain)

        # Verifico si existe el directorio del proyecto
        # y si no existe lo creo
        project_path = f"{PROJECTS_PATH}/{non_www_domain}"
        if not os.path.exists(project_path):
            os.mkdir(project_path)

        # Creo el index.html de prueba si no existe
        if not os.path.exists(f"{project_path}/index.html"):
            with open(f"{project_path}/index.html", "w") as html_file:
                html_file.write(html_template)

    result = {"message": "", "valid": not errors}
    return result
