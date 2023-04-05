# Autor : Baptiste LORTON

import json
import sys
from datetime import datetime

# ProcessMail function:
# Take as parameter a list containing the lines of the file
# Return a python dictionary containing the requested information

def processMail(data):
    dict = {}
    for line in data:
        line = line.replace("\n", "")
        element = line.split(" ")
        if "REF" in line :
            dict["reference"] = element[7]
            dict["reference"] = dict["reference"].replace(")", "")
        if "Deal" in line :
            date = datetime.strptime(element[3], "%d/%m/%Y")
            dict["tradeDate"] = date.strftime("%Y-%m-%d")
        if "SELL" in line :
            dict["currency"] = element[2]
            element[3] = element[3].replace(",", "")
            dict["amount"] = float(element[3])
        if "BUY" in line :
            element[3] = element[3].replace(",", "")
            dict["amountCounterValue"] = float(element[3])
            dict["symbol"] = element[2] + dict["currency"]
        if "RATE" in line :
            dict["rate"] = float(element[1])
        if "VALUE DATE" in line :
            date = datetime.strptime(element[2], "%d/%m/%Y")
            dict["valueDate"] = date.strftime("%Y-%m-%d")
    return dict

# toJSON function:
# Take as parameter a python dictionary
# Print a json file from a dictionary

def toJSON(dict):
    json_object = json.dumps(dict, indent=len(dict))
    print(json_object)


# main function:
# Take the name of the file as a parameter

def main(source):
    f = open(source, "r")
    data = f.readlines()
    dict = processMail(data)
    toJSON(dict)

if __name__ == "__main__":
    main(sys.argv[1])