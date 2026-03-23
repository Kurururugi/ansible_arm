#!/usr/bin/python3

import os
import subprocess

result = subprocess.run('/opt/Automiq/Alpha.Security/Utils/alpha.security.crypter',
                        input='Bzpa/123456789',
                        capture_output=True,
                        text=True)
password = result.stdout.lstrip('Crypter application has been started...\nType a password: Encrypted password: ')
print(password)

with open("/opt/Automiq/Alpha.Security/alpha.security.agent.xml", "r") as f:
    lines = f.readlines()
with open("/opt/Automiq/Alpha.Security/alpha.security.agent.xml", "w") as f:
    for line in lines:
        if 'LdapPassword' in line:
            line = '<LdapPassword value="' + password.strip() + '" />\n'
            f.write(line)
        else:
            f.write(line)

