#! /usr/bin/python3
import gi
import signal
import os
gi.require_version("Gtk", "3.0")
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as ai

def suspend(source):
    os.system('systemctl suspend')
def hybsus(source):
    os.system('system-ctl hybrid-sleep')
def hib(source):
    os.system('systemctl hibernate')


def build_menu():
    menu = gtk.Menu()
    item_1= gtk.MenuItem('Suspend')
    item_2 = gtk.MenuItem('Hybrid Suspend')
    item_3 = gtk.MenuItem('Hibernate')
    item_4 =gtk.MenuItem('Quit')
    menu.append(item_1)
    menu.append(item_2)
    menu.append(item_3)
    menu.append(item_4)
    item_1.connect('activate', suspend)
    item_2.connect('activate',hybsus)
    item_3.connect('activate',hib)
    item_4.connect('activate',quit)
    menu.show_all()
    return menu


def quit(source):
    gtk.main_quit()
def main():
    indicator = ai.Indicator.new('Pan_Items', gtk.STOCK_INFO, ai.IndicatorCategory.OTHER)
    indicator.set_status(ai.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    signal.signal(signal.SIGINT,signal.SIG_DFL)

    gtk.main()

if __name__ == "__main__":
    main()