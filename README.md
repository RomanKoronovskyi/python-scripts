## Apache config

Jinja2 template for Apache configuration.

---

## Overview

This project provide creation vhosts.j2 template, that will return similar Apache config:

```bash
<VirtualHost *:80>
  ServerName www.domain.tld
  DocumentRoot /www/domain
  ServerAdmin www-admin@foo.example.com
  <Directory "/usr/local/httpd/htdocs">
     AllowOverride All
     Options Indexes FollowSymLinks
     Order allow,deny
     Allow from all
  </Directory>
</VirtualHost>
```

Script conf.py return vhosts.conf, that contain multiple VirtualHosts and takes data from  data.yml.

## Requirements

- Python 3.10+
- Python modules:
  - `yaml`
  - `jinja2`

Install required dependencies:

```bash
pip install PyYAML
pip install jinja2
```
