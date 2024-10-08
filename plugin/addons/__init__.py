# -*- coding: utf-8 -*-
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS
from os import environ as os_environ
import gettext


def localeInit():
    lang = language.getLanguage()[:2]  # getLanguage returns e.g. "fi_FI" for "language_country"
    os_environ["LANGUAGE"] = lang  # Enigma doesn't set this (or LC_ALL, LC_MESSAGES, LANG). gettext needs it!
    gettext.bindtextdomain("FileCommander", resolveFilename(SCOPE_PLUGINS, "Extensions/FileCommander/locale"))


def _(txt):
    t = gettext.dgettext("FileCommander", txt)
    if t == txt:
        t = gettext.gettext(txt)
    return t


def ngettext(singular, plural, n):
    t = gettext.dngettext('FileCommander', singular, plural, n)
    if t in (singular, plural):
        t = gettext.ngettext(singular, plural, n)
    return t


localeInit()
language.addCallback(localeInit)
