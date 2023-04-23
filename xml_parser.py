from sys import getsizeof
from threading import Thread
from helpers import print_RAM_usage, parse_XML

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

