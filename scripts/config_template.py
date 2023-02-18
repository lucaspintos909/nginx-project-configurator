
def get_config_template(www_domain: str, non_www_domain: str) -> str:
    template = f"""
server {{
    server_name {non_www_domain};

    root /var/www/html/{non_www_domain};

    index index.html index.htm index.php;

    location / {{
        try_files $uri $uri/ =404;
    }}

    location ~ \.php$ {{
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php8.1-fpm.sock;
    }}

    location ~ /\.ht {{
        deny all;
    }}

    listen 80;
}}

server {{
    server_name {www_domain};

    location /{{
        try_files $uri $uri/ =404;
    }}

    location ~ \.php$ {{
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php8.1-fpm.sock;
    }}

    location ~ /\.ht {{
        deny all;
    }}

    listen 80;
    return 301 $scheme://{non_www_domain}$request_uri;
}}

"""

    return template


def get_config_redirection_template(www_domain: str, non_www_domain: str, redirection: str) -> str:
    template = f"""
server {{
    server_name {non_www_domain};

    location / {{
        try_files $uri $uri/ =404;
    }}

    location ~ /\.ht {{
        deny all;
    }}

    return 301 $scheme://{redirection}$request_uri;

    listen 80;
}}

server {{
    server_name {www_domain};
    
    location / {{
        try_files $uri $uri/ =404;
    }}

    location ~ /\.ht {{
        deny all;
    }}

    return 301 $scheme://{redirection}$request_uri;

    listen 80;
}}

"""
    return template


def get_html_template(non_www_domain: str) -> str:
    template = f"""
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{non_www_domain}</title>
  </head>
  <body>El dominio {non_www_domain} está configurado!</body>
</html>

"""

    return template
