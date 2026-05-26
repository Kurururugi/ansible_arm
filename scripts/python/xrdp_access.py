#!/usr/bin/python3

import os
from lxml import etree


def modify_access_policy(filepath):
#
# Изменение папаметров polkit-1 для работы xrdp
#

   # Бэкап /usr/share/polkit-1/actions/ru.astralinux.kcm.securitysettings.policy
   backup = f"{filepath}.bak"
   if not os.path.isfile(backup):
      os.system(f"cp {filepath} {backup}")

   # Загружаем и парсим файл
   parser = etree.XMLParser(remove_blank_text=True)
   tree = etree.parse(filepath, parser)
   root = tree.getroot()

   # Ищем нужные для редактирования теги
   action = root.find(".//action[@id='ru.astralinux.kcm.securitysettings.access']")
   defaults = action.find('defaults')

   # Изменяем значение allow_inactive и allow_active
   allow_inactive = defaults.find('allow_inactive')
   allow_active = defaults.find('allow_active')
   allow_inactive.text = 'auth_admin_keep'
   allow_active.text = 'auth_admin_keep'

   # Добавление allow_any, если отсутствует
   if defaults.find('allow_any') is None:
      allow_any = etree.Element('allow_any')
      allow_any.text = 'auth_admin_keep'
      defaults.append(allow_any)

   # Сохранение изменений в файле
   tree.write(filepath,
              encoding='utf-8',
              xml_declaration=True,
              pretty_print=True)


def admin_for_xrdp(filepath):
#
# Создаем и заполняем файл /var/lib/polkit-1/localauthority/75-polkitfly.d/ru.astralinux.kcm.securitysettings.pkla
#
   os.system(f'touch {filepath}')
   content = 'Identity=unix-user:administrator\n' + \
             'Action=ru.astralinux.kcm.securitysettings.access\n' + \
             'ResultAny=auth_admin_keep\n' + \
             'ResultInactive=auth_admin_keep\n' + \
             'ResultActive=auth_admin_keep\n'

   with open(filepath, 'w') as f:
      f.write(content)


modify_access_policy('/usr/share/polkit-1/actions/ru.astralinux.kcm.securitysettings.policy')
admin_for_xrdp('/var/lib/polkit-1/localauthority/75-polkitfly.d/ru.astralinux.kcm.securitysettings.pkla')
