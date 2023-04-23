from xml.dom.minidom import parseString
from psutil import Process

done = False
currProcess = Process()

def print_VM_usage():
    print("Starting VM usage Thread.")
    while(not done):
        VM_usage_mb = currProcess.memory_info().vms / (1024.0 * 1024.0) 
        print(f"Usage in MB: {VM_usage_mb}")	
        if VM_usage_mb > 1024:
            print("CTF_Flag{Exponential_Entity_Expansion_Attack_in_XML!}")
        
def parse_XML(xml_string):
    global done
    print("Starting to parse the XML.")
    dom = parseString(xml_string)
    done = True
    print("Finished parsing the XML.")