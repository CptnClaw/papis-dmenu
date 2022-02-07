"""
dmenu gui
*********

See `dmenu <https://tools.suckless.org/dmenu/>`_ and the python wrapper
`here <http://dmenu.readthedocs.io/en/latest/>`_ for more information.

.. papis-config:: lines
    :section: dmenu-gui

.. papis-config:: case_insensitive
    :section: dmenu-gui

.. papis-config:: bottom
    :section: dmenu-gui

.. papis-config:: font
    :section: dmenu-gui

.. papis-config:: background
    :section: dmenu-gui

.. papis-config:: foreground
    :section: dmenu-gui

.. papis-config:: background_selected
    :section: dmenu-gui

.. papis-config:: foreground_selected
    :section: dmenu-gui

.. papis-config:: header-format
    :section: dmenu-gui

    This is not set per default, and it will default to
    the general header-format if not set.

.. papis-config:: editor
    :section: dmenu-gui

    Editor used for editing info files, you should probably use a
    non-terminal based editor, i.e., ``gvim``, ``gedit`` etc..


"""

import papis.config

configuration_settings = {
    "dmenu-gui": {
        "lines": 10,
        "case_insensitive": True,
        "bottom": False,
        "font": 'UbuntuMono Nerd Font:style=Regular Font:size=14',
        "background": '#1f2937',
        "foreground": '#dddddd',
        "background_selected": '#82aaff',
        "foreground_selected": '#212121',
        "header-format":
            '{doc[year]:<4} | {doc[title]:<120.120} | {doc[author]}',
        "editor": "subl",
    }
}


def register_default_settings():
    papis.config.register_default_settings(configuration_settings)
