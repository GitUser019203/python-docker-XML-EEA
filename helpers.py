from xml.dom.minidom import parseString
from psutil import Process

done = False
currProcess = Process()

def print_VM_usage():
    print("Starting VM usage Thread.")
    while(not done):
        VM_usage_mb = currProcess.memory_info().vms / (1024.0 * 1024.0) 
        if VM_usage_mb > 1024:
            for i in range(0,1000):
                print("CTF_SDaT{Entity_Expansion_Attack_in_XML!}")
        else:
            print(f"Usage in MB: {VM_usage_mb}")	
            
def parse_XML(xml_string):
    global done
    print("Starting to parse the XML.")
    dom = parseString(xml_string)
    done = True
    print("Finished parsing the XML.")