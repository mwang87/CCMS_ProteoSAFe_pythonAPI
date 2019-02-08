import ccmsproteosafepythonapi.proteosafe as pf
import sys

def launch_deconvolutoin_workflow(ftp_path, job_description, username, password, groups_present,email):
    invokeParameters = {}
    invokeParameters["workflow"] = "MZMINE-GC-MING"
    invokeParameters["desc"] = job_description
    # currently dropdown only has one choice. Might be more
    invokeParameters["MZMINE_BATCHPRESET"]="high_res_production_3_27_2018.xml"
    # put file into specific paths before submitting the job
    #invokeParameters["spec_on_server"] = "d.aaksenov/GC_data/Andrea_bacteria_fungus;"
    invokeParameters["spec_on_server"] = "d." + ftp_path + "/G1;"
    if "G2" in groups_present:
        invokeParameters["spec_on_server_group2"] = "d." + ftp_path + "/G2;"
    if "G3" in groups_present:
        invokeParameters["spec_on_server_group3"] = "d." + ftp_path + "/G3;"
    if "G4" in groups_present:
        invokeParameters["spec_on_server_group4"] = "d." + ftp_path + "/G4;"
    if "G5" in groups_present:
        invokeParameters["spec_on_server_group5"] = "d." + ftp_path + "/G5;"
    if "G6" in groups_present:
        invokeParameters["spec_on_server_group6"] = "d." + ftp_path + "/G6;"
    invokeParameters["email"] = email
    # do we need to assgin uuid?
    invokeParameters["uuid"] = "1E03495E-D631-0001-9A7C-3F912CE71542"
    task_id = pf.invoke_workflow("gnps.ucsd.edu", invokeParameters, username, password)
    return task_id

def launch_GCSearch_workflow(spec_path,lib_paths, job_description, username, password, email):
    #lib_paths is a list of all the libraries:
    #ie [staticlibs/AROMA-UNIV-CORSICA-GC,staticlibs/WILEY_EI_11,staticlibs/NIST_EI_14]
    invokeParameters = {}
    invokeParameters["workflow"] = "MOLECULAR-LIBRARYSEARCH-GC"
    invokeParameters["protocol"] = "None"
    invokeParameters["desc"] = job_description
    invokeParameters["library_on_server"] = "".join(["d.%s;"%(p) for p in lib_paths])
    invokeParameters["spec_on_server"] = "d." + spec_path + ";"
    #hard coded values
    #according to alexander's task (https://gnps.ucsd.edu/ProteoSAFe/status.jsp?task=8207e50c22b74370ba63e1942fbca8db)
    invokeParameters["tolerance.PM_tolerance"] = 20000
    invokeParameters["tolerance.Ion_tolerance"] = 0.5
    invokeParameters["WINDOW_FILTER"] = 0
    invokeParameters["TOP_K_RESULTS"] = 3
    invokeParameters["TOPK"] = 10
    invokeParameters["SEARCH_LIBQUALITY"] = 3
    invokeParameters["SCORE_THRESHOLD"] = 0.7
    invokeParameters["PAIRS_MIN_COSINE"] = 0.5
    invokeParameters["MIN_MATCHED_PEAKS"] = 5
    invokeParameters["MIN_PEAK_INT"] = 0
    invokeParameters["ANALOG_SEARCH"] = 0
    invokeParameters["MAX_SHIFT_MASS"] = 100.0
    invokeParameters["MAX_SHIFT"] = 500
    invokeParameters["MAXIMUM_COMPONENT_SIZE"] = 100
    invokeParameters["FORCE_EXACT_MATCH"] = 1
    invokeParameters["FILTER_STDDEV_PEAK_datasetsINT"] = 0.0
    invokeParameters["FILTER_SNR_PEAK_datasetsINT"] = 0.0
    invokeParameters["FILTER_PRECURSOR_WINDOW"] = 0
    invokeParameters["FILTER_LIBRARY"] = 0
    invokeParameters["ANALOG_SEARCH"] = 0
    invokeParameters["email"] = email
    invokeParameters["uuid"] = "1DCE40F7-1211-0001-979D-15DAB2D0B500"
    task_id = pf.invoke_workflow("gnps.ucsd.edu", invokeParameters, username, password)
    return task_id

#simple tryout
if __name__ == "__main__":
    ftp = "zhz077"
    job = "tryout"
    username = sys.argv[1]
    password = sys.argv[2]
    groups_present = ""
    email = "zhz077@ucsd.edu"
    spec_path ="aaksenov/GC_data/Andrea_bacteria_fungus/specs_ms2.mgf"
    spec_path2 = "zhz077/top_25.mgf"
    lib_paths = ["staticlibs/AROMA-UNIV-CORSICA-GC","staticlibs/WILEY_EI_11","staticlibs/NIST_EI_14"]
    print(launch_deconvolutoin_workflow(ftp,job,username,password,groups_present,email))
    print(launch_GCSearch_workflow(spec_path,lib_paths, job, username, password, email))
    print(launch_GCSearch_workflow(spec_path2,lib_paths, job, username, password, email))

