#!/usr/bin/python

import sys
import getopt
import os
import json
import argparse
from ccmsproteosafepythonapi import proteosafe

def main():
    parser = argparse.ArgumentParser(description='Invoking new workflow with parameters of given workflow')
    parser.add_argument('workflowparamters', help='workflowparamters')
    parser.add_argument('--parametermapping', action='append', help='mapping of current workflow parameters to new parameters in the format: <old parameter>:<new parameter>')
    parser.add_argument('--newparameters', action='append', help='parameter key: <param name>:<parameter value>')
    args = parser.parse_args()

    workflow_parameters_map = proteosafe.parse_xml_file(args.workflowparamters)

    new_parameters = {}

    if args.newparameters != None:
        for parameter_string in args.newparameters:
            parameter_key = parameter_string.split(":")[0]
            parameter_value = parameter_string.split(":")[1]

            new_parameters[parameter_key] = parameter_value

    if args.parametermapping != None:
        for parameter_string in args.parametermapping:
            parameter_old_key = parameter_string.split(":")[0]
            parameter_new_key = parameter_string.split(":")[1]

            new_parameters[parameter_new_key] = workflow_parameters_map[parameter_old_key][0]

    print(new_parameters)





if __name__ == "__main__":
    main()
