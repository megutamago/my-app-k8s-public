
# Environment
WK_IP_1 = '192.168.11.121'
WK_IP_3 = '192.168.11.123'

lists = {
    # id           # LB_ID  # vrId  # IP             
    'service41': [ '41',    '41',   '192.168.11.141' ],
    'service42': [ '42',    '42',   '192.168.11.142' ],
    'service43': [ '43',    '43',   '192.168.11.143' ],
    'service44': [ '44',    '44',   '192.168.11.144' ],
    'service45': [ '45',    '45',   '192.168.11.145' ],
    'service46': [ '46',    '46',   '192.168.11.146' ],
    'service47': [ '47',    '47',   '192.168.11.147' ],
    'service48': [ '48',    '48',   '192.168.11.148' ],
    'service49': [ '48',    '48',   '192.168.11.149' ],

    'service51': [ '51',    '51',   '192.168.11.151' ],
    'service51': [ '52',    '52',   '192.168.11.152' ],
    'service51': [ '53',    '53',   '192.168.11.153' ],
    'service51': [ '54',    '54',   '192.168.11.154' ],

    'service81': [ '81',    '81',   '192.168.11.181' ],
    'service82': [ '82',    '82',   '192.168.11.182' ],
    'service83': [ '83',    '83',   '192.168.11.183' ],
}

# config gen keepalived
from jinja2 import Template

def generate_script(template_path, output_path, **kwargs):
    with open(template_path, 'r') as file:
        template_content = file.read()

    template = Template(template_content)

    rendered_script = template.render(**kwargs)

    with open(output_path, 'w') as output_file:
        output_file.write(rendered_script)

generate_script('../keepalived/template.conf', '../keepalived/keepalived_master.conf', lists=lists, WK_IP_1=WK_IP_1, WK_IP_3=WK_IP_3, state='MASTER', priority='101')
generate_script('../keepalived/template.conf', '../keepalived/keepalived_backup.conf', lists=lists, WK_IP_1=WK_IP_1, WK_IP_3=WK_IP_3, state='BACKUP', priority='102')