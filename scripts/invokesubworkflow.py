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
    parser.add_argument('credentials', help='credentials.json')
    parser.add_argument('--serverurl', default='proteomics2.ucsd.edu', help='Server URL, default is proteomics2.ucsd.edu, other options are massive.ucsd.edu and gnps.ucsd.edu')
    parser.add_argument('--parametermapping', action='append', help='mapping of current workflow parameters to new parameters in the format: <old parameter>:<new parameter>')
    parser.add_argument('--newparameters', action='append', help='parameter key: <param name>:<parameter value>')
    args = parser.parse_args()

    print(args)

    credentials = json.loads(open(args.credentials).read())

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

    task_id = proteosafe.invoke_workflow(args.serverurl, new_parameters, credentials["username"], credentials["password"])
    if task_id == None:
        exit(1)
    proteosafe.wait_for_workflow_finish(args.serverurl, task_id)


if __name__ == "__main__":
    main()
