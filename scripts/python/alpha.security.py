#!/usr/bin/python3

import os
import subprocess

if not os.path.isfile('/opt/Automiq/Alpha.Security/access.ldif'):
    os.system('touch /opt/Automiq/Alpha.Security/access.ldif')
os.system('echo "dn: olcDatabase={1}mdb,cn=config" > touch /opt/Automiq/Alpha.Security/access.ldif')
os.system('echo "changetype: modify" >> touch /opt/Automiq/Alpha.Security/access.ldif')
os.system('echo "replace: olcAccess" >> touch /opt/Automiq/Alpha.Security/access.ldif')
os.system('echo "olcAccess: {0}to * by users write by * read" >> touch /opt/Automiq/Alpha.Security/access.ldif')

result = subprocess.run('/opt/Automiq/Alpha.Security/Utils/alpha.security.crypter',
                        input='Bzpa/123456789',
                        capture_output=True,
                        text=True)

password = result.stdout.lstrip('Crypter application has been started...\nType a password: Encrypted password: ')

if not os.path.isfile('/opt/Automiq/Alpha.Security/alpha.security.agent.xml'):
    os.system('cp /opt/Automiq/Alpha.Security/alpha.security.agent.xml /opt/Automiq/Alpha.Security/alpha.security.agent.xml.bak')
with open("/opt/Automiq/Alpha.Security/alpha.security.agent.xml", "r") as f:
    lines = f.readlines()
with open("/opt/Automiq/Alpha.Security/alpha.security.agent.xml", "w") as f:
    for line in lines:
        if 'LdapPassword' in line:
            line = '\t<LdapPassword value="' + password.strip() + '" />\n'
            f.write(line)
        else:
            f.write(line)
