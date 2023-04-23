from sys import getsizeof
from threading import Thread
from helpers import print_VM_usage, parse_XML

xml_string = input("Enter an XML string at most 10 KB large: \n")
xml_size = getsizeof(xml_string)

if xml_size > 10240:
    print(f"The XML string you entered is larger than 10 KB because it is {xml_size} KB large.")
    exit(1)
else:
    print("The XML string you entered is at most 10 KB large.")

vm_usage_thread = Thread(target = print_VM_usage)
xml_parsing_thread = Thread(target = parse_XML, args = (xml_string,))
xml_parsing_thread.start()
vm_usage_thread.start()
xml_parsing_thread.join()
vm_usage_thread.join()

