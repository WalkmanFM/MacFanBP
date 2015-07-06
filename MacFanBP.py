#! /usr/bin/python
#Author: Sergio Jose Martinez Perales
#email: sjmp93@gmail.com
from gi.repository import Gdk, GLib, GObject
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
import time
import os
import threading

os.system('sudo dmidecode -s system-product-name > ./pname.txt')
pname = 'nopname'
try:
    pnamef = open('./pname.txt', 'r')
    pname = pnamef.readline()
    pnamef.close()
except IOError:
	print('Error, MacFanBP can\'t continue')
	quit()
icon_image = "./icn.png"
menu = gtk.Menu()
# Fan RPM control
def RPM2000(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan1_min', 'w') 
    outfile.write('2000')
    outfile.close()

def RPM3000(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan1_min', 'w')
    outfile.write('3000')
    outfile.close()

def RPM4000(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan1_min', 'w') 
    outfile.write('4000')
    outfile.close()

def RPM5000(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan1_min', 'w')
    outfile.write('5000')
    outfile.close()
    
def RPM6000(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan1_min', 'w')
    outfile.write('6159')
    outfile.close()
  
def RPMMPCPU500(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan1_min', 'w') 
    outfile.write('500')
    outfile.close()

def RPMMPCPU750(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan1_min', 'w') 
    outfile.write('750')
    outfile.close()

def RPMMPCPU1000(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan1_min', 'w') 
    outfile.write('1000')
    outfile.close()
    
def RPMMPCPU1300(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan1_min', 'w') 
    outfile.write('1300')
    outfile.close()
    
def RPMMPCPU1750(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan1_min', 'w') 
    outfile.write('1750')
    outfile.close()       

def RPMMPCPU2000(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan1_min', 'w') 
    outfile.write('2000')
    outfile.close()
    
def RPMMPCPU2500(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan1_min', 'w') 
    outfile.write('2500')
    outfile.close()       

def RPMMPIO500(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan2_min', 'w') 
    outfile.write('500')
    outfile.close()

def RPMMPIO750(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan2_min', 'w') 
    outfile.write('750')
    outfile.close()

def RPMMPIO1000(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan2_min', 'w') 
    outfile.write('1000')
    outfile.close()
    
def RPMMPIO1300(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan2_min', 'w') 
    outfile.write('1300')
    outfile.close()
    
def RPMMPIO1750(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan2_min', 'w') 
    outfile.write('1750')
    outfile.close()       

def RPMMPIO2000(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan2_min', 'w') 
    outfile.write('2000')
    outfile.close()
    
def RPMMPIO2500(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan2_min', 'w') 
    outfile.write('2500')
    outfile.close()   

def RPMMPEXHAUST500(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan3_min', 'w') 
    outfile.write('500')
    outfile.close()

def RPMMPEXHAUST750(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan3_min', 'w') 
    outfile.write('750')
    outfile.close()

def RPMMPEXHAUST1000(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan3_min', 'w') 
    outfile.write('1000')
    outfile.close()
    
def RPMMPEXHAUST1300(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan3_min', 'w') 
    outfile.write('1300')
    outfile.close()
    
def RPMMPEXHAUST1750(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan3_min', 'w') 
    outfile.write('1750')
    outfile.close()       

def RPMMPEXHAUST2000(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan3_min', 'w') 
    outfile.write('2000')
    outfile.close()
    
def RPMMPEXHAUST2500(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan3_min', 'w') 
    outfile.write('2500')
    outfile.close() 

def RPMMPPS600(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan4_min', 'w') 
    outfile.write('600')
    outfile.close()

def RPMMPPS750(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan4_min', 'w') 
    outfile.write('750')
    outfile.close()

def RPMMPPS1000(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan4_min', 'w') 
    outfile.write('1000')
    outfile.close()
    
def RPMMPPS1300(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan4_min', 'w') 
    outfile.write('1300')
    outfile.close()
    
def RPMMPPS1750(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan4_min', 'w') 
    outfile.write('1750')
    outfile.close()       

def RPMMPPS2000(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan4_min', 'w') 
    outfile.write('2000')
    outfile.close()
    
def RPMMPPS2500(widget,data=None):
    outfile = open('/sys/devices/platform/applesmc.768/fan4_min', 'w') 
    outfile.write('2500')
    outfile.close() 

def quit(widget, data=None):
    gtk.main_quit()


class controlador:
		
    fanout = "Fan RPM"
    menu_fanout = gtk.MenuItem(fanout)
    menu_fanout.set_sensitive(False)
    menu.append(menu_fanout)
	
    item1 = "2000 RPM"
    menu_item1MB = gtk.MenuItem(item1)
    # Associate RPM2000 to item
    menu_item1MB.connect("activate", RPM2000)
    menu.append(menu_item1MB)

    item2 = "3000 RPM"
    menu_item2MB = gtk.MenuItem(item2)
    # Associate RPM3000 to item2
    menu_item2MB.connect("activate", RPM3000)
    menu.append(menu_item2MB)

    item3 = "4000 RPM"
    menu_item3MB = gtk.MenuItem(item3)
    # Associate RPM4000 to item3
    menu_item3MB.connect("activate", RPM4000)
    menu.append(menu_item3MB)
        
    item4 = "5000 RPM"
    menu_item4MB = gtk.MenuItem(item4)
    # Associate RPM5000 to item4
    menu_item4MB.connect("activate", RPM5000)
    menu.append(menu_item4MB)
        
    item5 = "6000 RPM"
    menu_item5MB = gtk.MenuItem(item5)
    # Associate RPM6000 to item5
    menu_item5MB.connect("activate", RPM6000)
    menu.append(menu_item5MB)
    
    '''---------------------------------------------------'''
    # Fan1
    fan1CPU = gtk.Menu() 
    # CPU/MEM RPM submenu
    CPUMEMitem = gtk.MenuItem("CPU/MEM")
    CPUMEMitem.set_submenu(fan1CPU)
    # Fan1 RPM output label
    CPUMEMoutrpm = gtk.MenuItem("CPU/MEM RPM")
    fan1CPU.append(CPUMEMoutrpm)
    CPUMEMoutrpm.set_sensitive(False)
    # RPM items
    rpm500CPU = gtk.MenuItem("500 RPM")
    rpm500CPU.connect("activate",RPMMPCPU500)
    fan1CPU.append(rpm500CPU)
    rpm750CPU = gtk.MenuItem("750 RPM")
    rpm750CPU.connect("activate",RPMMPCPU750)
    fan1CPU.append(rpm750CPU)
    rpm1000CPU = gtk.MenuItem("1000 RPM")
    rpm1000CPU.connect("activate",RPMMPCPU1000)
    fan1CPU.append(rpm1000CPU)
    rpm1300CPU = gtk.MenuItem("1300 RPM")
    rpm1300CPU.connect("activate",RPMMPCPU1300)
    fan1CPU.append(rpm1300CPU)
    rpm1750CPU = gtk.MenuItem("1750 RPM")
    rpm1750CPU.connect("activate",RPMMPCPU1750)
    fan1CPU.append(rpm1750CPU)
    rpm2000CPU = gtk.MenuItem("2000 RPM")
    rpm2000CPU.connect("activate",RPMMPCPU2000)
    fan1CPU.append(rpm2000CPU)
    rpm2500CPU = gtk.MenuItem("2500 RPM")
    rpm2500CPU.connect("activate",RPMMPCPU2500)
    fan1CPU.append(rpm2500CPU)
    
    # Fan2
    fan2IO = gtk.Menu() 
    # IO RPM submenu
    IOitem = gtk.MenuItem("IO")
    IOitem.set_submenu(fan2IO)
    # Fan2 RPM output label
    IOoutrpm = gtk.MenuItem("IO RPM")
    fan2IO.append(IOoutrpm)
    IOoutrpm.set_sensitive(False)
    # RPM items
    rpm500IO = gtk.MenuItem("500 RPM")
    rpm500IO.connect("activate",RPMMPIO500)
    fan2IO.append(rpm500IO)
    rpm750IO = gtk.MenuItem("750 RPM")
    rpm750IO.connect("activate",RPMMPIO750)
    fan2IO.append(rpm750IO)
    rpm1000IO = gtk.MenuItem("1000 RPM")
    rpm1000IO.connect("activate",RPMMPIO1000)
    fan2IO.append(rpm1000IO)
    rpm1300IO = gtk.MenuItem("1300 RPM")
    rpm1300IO.connect("activate",RPMMPIO1300)
    fan2IO.append(rpm1300IO)
    rpm1750IO = gtk.MenuItem("1750 RPM")
    rpm1750IO.connect("activate",RPMMPIO1750)
    fan2IO.append(rpm1750IO)
    rpm2000IO = gtk.MenuItem("2000 RPM")
    rpm2000IO.connect("activate",RPMMPIO2000)
    fan2IO.append(rpm2000IO)
    rpm2500IO = gtk.MenuItem("2500 RPM")
    rpm2500IO.connect("activate",RPMMPIO2500)
    fan2IO.append(rpm2500IO)
    
    # Fan3
    fan3EXHAUST = gtk.Menu() 
    # EXHAUST RPM submenu
    EXHAUSTitem = gtk.MenuItem("EXHAUST")
    EXHAUSTitem.set_submenu(fan3EXHAUST)
    # Fan3 RPM output label
    EXHAUSToutrpm = gtk.MenuItem("EXHAUST RPM")
    fan3EXHAUST.append(EXHAUSToutrpm)
    EXHAUSToutrpm.set_sensitive(False)
    # RPM items
    rpm500EXHAUST = gtk.MenuItem("500 RPM")
    rpm500EXHAUST.connect("activate",RPMMPEXHAUST500)
    fan3EXHAUST.append(rpm500EXHAUST)
    rpm750EXHAUST = gtk.MenuItem("750 RPM")
    rpm750EXHAUST.connect("activate",RPMMPEXHAUST750)
    fan3EXHAUST.append(rpm750EXHAUST)
    rpm1000EXHAUST = gtk.MenuItem("1000 RPM")
    rpm1000EXHAUST.connect("activate",RPMMPEXHAUST1000)
    fan3EXHAUST.append(rpm1000EXHAUST)
    rpm1300EXHAUST = gtk.MenuItem("1300 RPM")
    rpm1300EXHAUST.connect("activate",RPMMPEXHAUST1300)
    fan3EXHAUST.append(rpm1300EXHAUST)
    rpm1750EXHAUST = gtk.MenuItem("1750 RPM")
    rpm1750EXHAUST.connect("activate",RPMMPEXHAUST1750)
    fan3EXHAUST.append(rpm1750EXHAUST)
    rpm2000EXHAUST = gtk.MenuItem("2000 RPM")
    rpm2000EXHAUST.connect("activate",RPMMPEXHAUST2000)
    fan3EXHAUST.append(rpm2000EXHAUST)
    rpm2500EXHAUST = gtk.MenuItem("2500 RPM")
    rpm2500EXHAUST.connect("activate",RPMMPEXHAUST2500)
    fan3EXHAUST.append(rpm2500EXHAUST)
    
    # Fan4
    fan4PS = gtk.Menu() 
    # PS RPM submenu
    PSitem = gtk.MenuItem("PS")
    PSitem.set_submenu(fan4PS)
    # Fan4 RPM output label
    PSoutrpm = gtk.MenuItem("PS RPM")
    fan4PS.append(PSoutrpm)
    PSoutrpm.set_sensitive(False)
    # RPM items
    rpm600PS = gtk.MenuItem("600 RPM")
    rpm600PS.connect("activate",RPMMPPS600)
    fan4PS.append(rpm600PS)
    rpm750PS = gtk.MenuItem("750 RPM")
    rpm750PS.connect("activate",RPMMPPS750)
    fan4PS.append(rpm750PS)
    rpm1000PS = gtk.MenuItem("1000 RPM")
    rpm1000PS.connect("activate",RPMMPPS1000)
    fan4PS.append(rpm1000PS)
    rpm1300PS = gtk.MenuItem("1300 RPM")
    rpm1300PS.connect("activate",RPMMPPS1300)
    fan4PS.append(rpm1300PS)
    rpm1750PS = gtk.MenuItem("1750 RPM")
    rpm1750PS.connect("activate",RPMMPPS1750)
    fan4PS.append(rpm1750PS)
    rpm2000PS = gtk.MenuItem("2000 RPM")
    rpm2000PS.connect("activate",RPMMPPS2000)
    fan4PS.append(rpm2000PS)
    rpm2500PS = gtk.MenuItem("2500 RPM")
    rpm2500PS.connect("activate",RPMMPPS2500)
    fan4PS.append(rpm2500PS)
    
    
    
    menu.append(CPUMEMitem)
    menu.append(IOitem)
    menu.append(EXHAUSTitem)
    menu.append(PSitem)
    '''---------------------------------------------------'''
    
    # Exit button
    salir = "Salir"
    menu_item6 = gtk.MenuItem(salir)
    menu_item6.connect("activate", quit)
    menu.append(menu_item6)
    if(str(pname) == str("MacBookPro8,1") + "\n"): # MacBook Pro
        menu_fanout.show()
        menu_item1MB.show()
        menu_item2MB.show()   
        menu_item3MB.show()
        menu_item4MB.show()
        menu_item5MB.show()  
        menu_item6.show()
    else:
        CPUMEMitem.show()
        CPUMEMoutrpm.show()
        rpm500CPU.show()
        rpm750CPU.show()
        rpm1000CPU.show()
        rpm1300CPU.show()
        rpm1750CPU.show()
        rpm2000CPU.show()
        rpm2500CPU.show()
        
        IOitem.show()
        IOoutrpm.show()
        rpm500IO.show()
        rpm750IO.show()
        rpm1000IO.show()
        rpm1300IO.show()
        rpm1750IO.show()
        rpm2000IO.show()
        rpm2500IO.show()
        
        EXHAUSTitem.show()
        EXHAUSToutrpm.show()
        rpm500EXHAUST.show()
        rpm750EXHAUST.show()
        rpm1000EXHAUST.show()
        rpm1300EXHAUST.show()
        rpm1750EXHAUST.show()
        rpm2000EXHAUST.show()
        rpm2500EXHAUST.show()
        
        PSitem.show()
        PSoutrpm.show()
        rpm600PS.show()
        rpm750PS.show()
        rpm1000PS.show()
        rpm1300PS.show()
        rpm1750PS.show()
        rpm2000PS.show()
        rpm2500PS.show()
        
        menu_item6.show() # the quit button
 
    # Initialize the indicator
    ind = appindicator.Indicator.new("MacFanBP",icon_image,appindicator.IndicatorCategory.APPLICATION_STATUS)
    ind.set_status(appindicator.IndicatorStatus.ACTIVE) 
    ind.set_label('Here goes the temperature output','')
    
    # Updates the indicator label with the Core 0 and Core 1 temperature on MacBook Pro
    
    def functionMB(self, widget):
        infile = open('/sys/devices/platform/applesmc.768/temp4_input', 'r') #input Core 0 temp
        temperatureC0=str(int(infile.readline())/1000) +  u"\u2103".encode('utf-8')
        infile.close()  
        infile = open('/sys/devices/platform/applesmc.768/temp10_input', 'r') #input Core 1 temp
        temperatureC1=str(int(infile.readline())/1000) +  u"\u2103".encode('utf-8')
        infile.close()       
        self.ind.set_label(temperatureC0 + " " + temperatureC1,"")
        return True
        
    # Updates the indicator label with the Core 0 and Core 1 temperature on Mac Pro

    def functionMP(self, widget):
        infile = open('/sys/devices/platform/applesmc.768/temp2_input', 'r') #input Core 0 temp
        temperatureC0=str(100 - int(infile.readline())/1000) +  u"\u2103".encode('utf-8')
        infile.close()
          
        infile = open('/sys/devices/platform/applesmc.768/temp5_input', 'r') #input Core 1 temp
        temperatureC1=str(100 - int(infile.readline())/1000) +  u"\u2103".encode('utf-8')
        infile.close()
        
        infile = open('/sys/devices/platform/applesmc.768/fan1_intput', 'r') # MBP fan RPM output
        fmbp = infile.readline()
        infile.close() 
        
        infile = open('/sys/devices/platform/applesmc.768/fan1_output', 'r') # CPU/MEM fan RPM output
        f1 = infile.readline()
        infile.close() 
        
        infile = open('/sys/devices/platform/applesmc.768/fan2_output', 'r') # IO fan RPM output
        f2 = infile.readline()
        infile.close() 
        
        infile = open('/sys/devices/platform/applesmc.768/fan3_output', 'r') # EXHAUST fan RPM output
        f3 = infile.readline()
        infile.close() 

        infile = open('/sys/devices/platform/applesmc.768/fan4_output', 'r') # PS fan RPM output
        f4 = infile.readline()
        infile.close() 
  
        self.CPUMEMoutrpm.set_label(f1[:4]) # [:4] only first 4 characters
        self.IOoutrpm.set_label(f2[:4])       
        self.EXHAUSToutrpm.set_label(f3[:4])  
        self.PSoutrpm.set_label(f4[:4]) 
        self.menu_fanout.set_label(fmbp[:4]) 
        self.ind.set_label(temperatureC0 + " " + temperatureC1,"")
        return True
        
    def __init__(self):
        if(str(pname) == str("MacBookPro8,1") + "\n"): # MacBook Pro
            # Indicator update thread
            GObject.timeout_add(500,self.functionMB,None)
            print('MacBookPro8,1')
            # Changing permissions to write RPM
            os.system('sudo chmod 777 /sys/devices/platform/applesmc.768/fan1_min')
        elif(str(pname) == str("MacPro1,1") + "\n"): # Mac Pro
            # Indicator update thread
            GObject.timeout_add(500,self.functionMP,None)
            print('MacPro1,1')
            # Changing permissions to write RPM
            os.system('sudo chmod 777 /sys/devices/platform/applesmc.768/fan1_min')
            os.system('sudo chmod 777 /sys/devices/platform/applesmc.768/fan2_min')
            os.system('sudo chmod 777 /sys/devices/platform/applesmc.768/fan3_min')
            os.system('sudo chmod 777 /sys/devices/platform/applesmc.768/fan4_min')
        else: # If not MacBook Pro nor Mac Pro, then exit
			print('You are not using a MacBookPro8,1 (MacBook Pro Late 2011 13") nor a MacPro1,1 (Mac Pro 2006)')
			exit()
        # Associate the menu to ind
        self.ind.set_menu(menu);
        gtk.main()

if __name__ == "__main__":
    indicador = controlador()
