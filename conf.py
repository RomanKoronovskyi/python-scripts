import yaml
from jinja2 import Template

with open("data.yml") as f:
    config_data = yaml.safe_load(f)

with open("vhosts.j2") as f:
    template = Template(f.read())

with open("vhosts.conf", "w") as f:
    f.write(template.render(config_data))
