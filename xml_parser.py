from xml.dom.minidom import parseString
from psutil import virtual_memory
from sys import getsizeof
from threading import Thread

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

xml_string = input("Enter an XML string at most 1 KB large: \n")
xml_size = getsizeof(xml_string)

if xml_size > 1024:
    print(f"The XML string you entered is larger than 1 KB because it is {xml_size} KB large.")
    exit(1)
else:
    print("The XML string you entered is at most 1 KB large.")

ram_usage_thread = Thread(target = print_RAM_usage)
xml_parsing_thread = Thread(target = parse_XML, args = (xml_string,))
xml_parsing_thread.start()
ram_usage_thread.start()
xml_parsing_thread.join()
ram_usage_thread.join()

