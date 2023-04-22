from xml.dom.minidom import parseString
from psutil import virtual_memory

done = False

def print_RAM_usage():
    while(not done):
        RAM_usage_mb = virtual_memory()[3] / (1024.0 * 1024.0)
        print(f"Usage in MB: {RAM_usage_mb}")
        if RAM_usage_mb > 3072:
            print("CTF_Flag{Exponential_Entity_Expansion_Attack_in_XML!}")
        else:
            print("The RAM usage of this program hasn't reached 3 GB yet.")

def parse_XML(xml_string):
    dom = parseString(xml_string)
    done = True