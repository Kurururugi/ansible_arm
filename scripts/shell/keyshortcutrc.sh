#!/bin/bash

echo '[ShortCutKeys]' > /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Alt|Insert = FLYWM_DESKTOP_FOCUS' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Alt|Shift|Delete = FLYWM_CHANGE_WIN_BACK_INSCR' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Alt|Delete = FLYWM_CHANGE_WIN_INSCR' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo 'Alt|Shift|Escape = FLYWM_CHANGE_WIN_BACK' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo 'Alt|Escape = FLYWM_CHANGE_WIN' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|d = FLYWM_TOGGLE_MINIMIZE_ALL_INSCR' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|m = FLYWM_TOGGLE_MINIMIZE_ALL_INSCR' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|F11 = FLYWM_TOGGLE_FULLSCREEN' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|Shift|F11 = FLYWM_TOGGLE_FULLSCREEN' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|Shift|Left = FLYWM_MOVE_XINERAMA_PREV' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|Shift|Right = FLYWM_MOVE_XINERAMA_NEXT' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|Shift|KP_Left = FLYWM_MOVE_XINERAMA_PREV' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|Shift|KP_Right = FLYWM_MOVE_XINERAMA_NEXT' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Alt|Shift|Tab = FLYWM_SWITCH_TASK_BACK' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Alt|Tab = FLYWM_SWITCH_TASK' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Alt|F4 = FLYWM_CLOSE' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Ctrl|Alt|Down = FLYWM_LOWER' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Ctrl|Alt|Up = FLYWM_RAISE' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|Up = FLYWM_MAXIMIZE' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|Down = FLYWM_RESTORE' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|Left = FLYWM_SNAP_LEFT' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|Right = FLYWM_SNAP_RIGHT' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|Left|Up = FLYWM_SNAP_TOP_LEFT' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|Left|Down = FLYWM_BOTTOM_LEFT' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|Right|Up = FLYWM_TOP_RIGHT' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|Right|Down = FLYWM_TOP_LEFT' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Alt|space = FLYWM_POPUP_MENU' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Alt|F3 = FLYWM_POPUP_MENU' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Alt|BackSpace = FLYWM_POPUP_DESKTOP_MENU' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|Super_L = FLYWM_POPUP_START_MENU' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|Super_R = FLYWM_POPUP_START_MENU' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Ctrl|Super_L = FLYWM_POPUP_START_MENU' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Ctrl|Super_R = FLYWM_POPUP_START_MENU' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Shift|Super_L = FLYWM_POPUP_START_MENU' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Shift|Super_R = FLYWM_POPUP_START_MENU' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|Ctrl|Down = FLYWM_DOWN_PAGING' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|Ctrl|Up = FLYWM_UP_PAGING' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|Ctrl|Right = FLYWM_RIGHT_PAGING' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|Ctrl|Left = FLYWM_LEFT_PAGING' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Ctrl|F1 = "fly-wmfunc FLYWM_GOTO_PAGING 1"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Ctrl|F2 = "fly-wmfunc FLYWM_GOTO_PAGING 2"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Ctrl|F3 = "fly-wmfunc FLYWM_GOTO_PAGING 3"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Ctrl|F4 = "fly-wmfunc FLYWM_GOTO_PAGING 4"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';;None|F12= FLYWM_TOGGLE_FULLSCREEN_PAGER' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo 'Ctrl|a = FLYWM_ICON_SELECT_ALL' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo 'Ctrl|f = FLYWM_ICON_FIND' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo 'Shift|Insert = FLYWM_ICON_PASTE' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo 'Ctrl|v = FLYWM_ICON_PASTE' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo 'Ctrl|Insert = FLYWM_ICON_COPY' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo 'Ctrl|c = FLYWM_ICON_COPY' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo 'Ctrl|x = FLYWM_ICON_CUT' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo 'None|Delete = FLYWM_ICON_SEND_TO_TRASH' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Shift|Delete = FLYWM_ICON_DELETE' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo 'None|KP_Delete = FLYWM_ICON_SEND_TO_TRASH' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Shift|KP_Delete = FLYWM_ICON_DELETE' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo 'None|Return = FLYWM_EXEC_ICON' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo 'None|KP_Enter = FLYWM_EXEC_ICON' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|Up = FLYWM_ICON_UP' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|Down = FLYWM_ICON_DOWN' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|Left = FLYWM_ICON_LEFT' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|Right = FLYWM_ICON_RIGHT' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|KP_Up = FLYWM_ICON_UP' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|KP_Down = FLYWM_ICON_DOWN' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|KP_Left = FLYWM_ICON_LEFT' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|KP_Right = FLYWM_ICON_RIGHT' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|F2 = FLYWM_ICON_RENAME' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Alt|F1 = "assistant -collectionFile /usr/share/doc/fly/qthelp/ru/flyhelp.qhc"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|a = "assistant -collectionFile /usr/share/doc/fly/qthelp/ru/flyhelp.qhc"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Alt|F2 = "fly-run"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Alt|t = "x-terminal-emulator"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|t = "x-terminal-emulator"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Alt|Ctrl|Delete = "ksysguard --autosu"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Alt|Ctrl|KP_Delete = "ksysguard --autosu"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Shift|Ctrl|Escape = "ksysguard --autosu"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|Print = "spectacle -f"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Alt|Print = "spectacle -a"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|Shift|s = "spectacle -r -b -c"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|e = "fly-fm"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|l = "fly-wmfunc FLYWM_LOCK"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|r = "fly-run"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|f = "fly-find -d -s ~"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|w = "libreoffice --writer"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|b = "firefox"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|h = "chromium"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|c = "kcalc || speedcrunch"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|g = "gwenview"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|k = "kate"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|s = "pavucontrol"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|i = "fly-admin-center"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';Mod4|Pause = "kinfocenter"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';special  keys' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86AudioMedia = "vlc"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86CD = "vlc"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Video = "vlc"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Music = "vlc"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86AudioRecord = "fly-record"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';let kglobalaccel5+kmix process it' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86AudioRaiseVolume = "amixer -q sset Master playback 8%+ unmute"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86AudioLowerVolume = "amixer -q sset Master playback 8%- unmute"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86AudioMute = "amixer -q sset Master playback toggle"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Calculator = "kcalc || speedcrunch"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Search = "fly-find -d"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Mail = "thunderbird"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86WWW = "firefox"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Support' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Messenger' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Phone' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86HomePage = "fly-fm ~"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Memo = "fly-notes"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86ToDoList' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Calendar = "fly-admin-date"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86MyComputer = "fly-fm fly-fm:Computer"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Documents = "libreoffice --writer"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Word = "libreoffice --writer"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Excel = "libreoffice --calc"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Explorer = "fly-fm"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Pictures = "gwenview"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Spell' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Terminal = "x-terminal-emulator"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Eject = "eject"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86WebCam = "fly-videocamera"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Battery = "qbat"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Bluetooth' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86WLAN' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86UWB' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';let kglobalaccel5+powerdevil process it' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86MonBrightnessUp = "xbacklight -inc 10"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86MonBrightnessDown = "xbacklight -dec 10"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86ScreenSaver = FLYWM_LOCK' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Sleep = FLYWM_SUSPEND' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Suspend = FLYWM_SUSPEND' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Standby = FLYWM_STANDBY' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86Hibernate = FLYWM_HIBERNATE' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86LogOff = FLYWM_EXIT' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86PowerDown = FLYWM_SHUTDOWN' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86PowerOff = FLYWM_SHUTDOWN' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86PowerDown = "/usr/bin/fly-power-btn.sh"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
echo ';None|XF86PowerOff = "/usr/bin/fly-power-btn.sh"' >> /usr/share/fly-wm/keyshortcutrc.fly-kiosk
