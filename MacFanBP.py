#! /usr/bin/python
#Author: Sergio José Martínez Perales
from gi.repository import Gdk, GLib, GObject
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
import time
import os
import threading

#icon_image = "/home/icn.png"
menu = gtk.Menu()
# Fan RPM control
def RPM2000(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan1_min', 'w') # Indicamos el valor 'w'.
    outfile.write('2000')
    outfile.close()

def RPM3000(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan1_min', 'w') # Indicamos el valor 'w'.
    outfile.write('3000')
    outfile.close()

def RPM4000(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan1_min', 'w') # Indicamos el valor 'w'.
    outfile.write('4000')
    outfile.close()

def RPM5000(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan1_min', 'w') # Indicamos el valor 'w'.
    outfile.write('5000')
    outfile.close()
    
def RPM6000(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan1_min', 'w') # Indicamos el valor 'w'.
    outfile.write('6159')
    outfile.close()

def quit(widget, data=None):
    gtk.main_quit()
# item0 shows temp
item0 = "Core 0"
menu_item0 = gtk.MenuItem(item0)
menu_item0.set_sensitive(False)
menu.append(menu_item0)

class controlador:
    item = "2000 RPM"
    menu_item = gtk.MenuItem(item)
    # Associate RPM2000 to item
    menu_item.connect("activate", RPM2000)
    menu.append(menu_item)

    item2 = "3000 RPM"
    menu_item2 = gtk.MenuItem(item2)
    # Associate RPM3000 to item2
    menu_item2.connect("activate", RPM3000)
    menu.append(menu_item2)

    item3 = "4000 RPM"
    menu_item3 = gtk.MenuItem(item3)
    # Associate RPM4000 to item3
    menu_item3.connect("activate", RPM4000)
    menu.append(menu_item3)
        
    item4 = "5000 RPM"
    menu_item4 = gtk.MenuItem(item4)
    # Associate RPM5000 to item4
    menu_item4.connect("activate", RPM5000)
    menu.append(menu_item4)
        
    item5 = "6000 RPM"
    menu_item5 = gtk.MenuItem(item5)
    # Associate RPM6000 to item5
    menu_item5.connect("activate", RPM6000)
    menu.append(menu_item5)
    
    # Exit button
    salir = "Salir"
    menu_item6 = gtk.MenuItem(salir)
    menu_item6.connect("activate", quit)
    menu.append(menu_item6)
    
    menu_item0.show()
    menu_item.show()
    menu_item2.show()   
    menu_item3.show()
    menu_item4.show()
    menu_item5.show()  
    menu_item6.show()
    
    # Initialize the indicator
    ind = appindicator.Indicator.new("Temperatura","icon"'''icon_image''',appindicator.IndicatorCategory.APPLICATION_STATUS)
    ind.set_status(appindicator.IndicatorStatus.ACTIVE) 
    ind.set_label('Here goes the temperature output','')
    
    # Updates the indicator label with the Core 0  temperature (does not work with the indicator label, updates menu_item0 label)
    
    def function(self, widget):
        infile = open('/sys/devices/platform/applesmc.768/temp4_input', 'r') #input Core 0 temp
        temperaturaC0=str(int(infile.readline())/1000) +  u"\u2103".encode('utf-8')
        infile.close()        
        self.ind.set_label("asd","")
        menu_item0.set_label(temperaturaC0)
        return True
    def __init__(self):
		# Update thread
        GObject.timeout_add(500,self.function,None)
        # Associate the menu to ind
        self.ind.set_menu(menu);
        gtk.main()

if __name__ == "__main__":
    
    indicador = controlador()
