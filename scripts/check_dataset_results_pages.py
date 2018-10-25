#!/usr/bin/python


import sys
import getopt
import os
from ccmsproteosafepythonapi import proteosafe
import requests
import json
from collections import defaultdict
from datetime import datetime, timedelta
try:
    import requests_cache
    requests_cache.install_cache('cache')
except:
    print("no requests cache")

try:
    from urllib import urlencode
except:
    from urllib.parse import urlencode, quote_plus

def get_mztab_result_page(task_id, view_name, file_descriptor):
    parameters = urlencode({'task': task_id, 'view': view_name, 'file': file_descriptor})
    url = "https://massive.ucsd.edu/ProteoSAFe/result_json.jsp?%s" % (parameters)

    #   print(url)

    r = requests.get(url)
    try:
        json_object = json.loads(r.text)
        return json_object
    except:
        print("ERROR MZTab Page", url)
        return None

def check_dataset_results(task_id):
    dataset_information = proteosafe.get_dataset_information(task_id)
    dataset_identifications = []
    if dataset_information["complete"] == "true":
        dataset_identifications = proteosafe.get_dataset_mzTab_list(task_id)


    total_dataset_psms = 0
    total_dataset_1_percent_psms = 0
    #Count total number of PSMs
    for mztab in dataset_identifications:
        #print(mztab["File_descriptor"])
        mztab_results_first_page = get_mztab_result_page(task_id, "group_by_spectrum", mztab["File_descriptor"])
        try:
            if mztab_results_first_page["blockData"]["total_rows"] == 0:
                print("ERROR", mztab)
        except:
            print("ERROR Dataset Result", task_id, mztab["File_descriptor"])


    reanalysis_tasks = proteosafe.get_dataset_reanalysis(task_id)["massivereanalyses"]

    for reanalysis_task in reanalysis_tasks:
        reanalysis_task_id = reanalysis_task["task"]
        reanalysis_identifications = proteosafe.get_dataset_mzTab_list(reanalysis_task_id)
        current_reanalysis_psms = 0
        for mztab in reanalysis_identifications:
            mztab_results_first_page = get_mztab_result_page(reanalysis_task_id, "group_by_spectrum", mztab["File_descriptor"])
            try:
                if mztab_results_first_page["blockData"]["total_rows"] == 0:
                    print("ERROR", mztab)
            except:
                print("ERROR Dataset Result", task_id, mztab["File_descriptor"])

def main():
    command = sys.argv[1]

    if command == "all":
        all_datasets = proteosafe.get_all_datasets()
        datasets_to_consider = []
        for dataset in all_datasets:
            if len(dataset["task"]) != 32:
                continue
            if dataset["title"].find("GNPS") != -1:
                continue
            datasets_to_consider.append(dataset)

        dataset_count= 0
        for dataset in datasets_to_consider:
            try:
                dataset_count += 1
                check_dataset_results(dataset["task"])
            except KeyboardInterrupt:
                raise
            except:
                print("ERROR", dataset["dataset"], dataset["task"])
                raise
                continue
    if command == "dataset":
        dataset_task = sys.argv[2]
        dataset_stats = check_dataset_results(dataset_task)
        print(dataset_stats)


if __name__ == "__main__":
    main()
