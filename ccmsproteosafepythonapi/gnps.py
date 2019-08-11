



def get_classic_networking_lowres_parameters():
    invokeParameters = {}
    invokeParameters["workflow"] = "METABOLOMICS-SNETS-V2"
    invokeParameters["protocol"] = "None"
    invokeParameters["library_on_server"] = "d.speclibs;"
    invokeParameters["tolerance.PM_tolerance"] = "2.0"
    invokeParameters["tolerance.Ion_tolerance"] = "0.5"
    invokeParameters["PAIRS_MIN_COSINE"] = "0.70"
    invokeParameters["MIN_MATCHED_PEAKS"] = "6"
    invokeParameters["TOPK"] = "10"
    invokeParameters["CLUSTER_MIN_SIZE"] = "2"
    invokeParameters["RUN_MSCLUSTER"] = "on"
    invokeParameters["MAXIMUM_COMPONENT_SIZE"] = "100"
    invokeParameters["MIN_MATCHED_PEAKS_SEARCH"] = "6"
    invokeParameters["SCORE_THRESHOLD"] = "0.7"
    invokeParameters["ANALOG_SEARCH"] = "0"
    invokeParameters["MAX_SHIFT_MASS"] = "100.0"
    invokeParameters["FILTER_STDDEV_PEAK_datasetsINT"] = "0.0"
    invokeParameters["MIN_PEAK_INT"] = "0.0"
    invokeParameters["FILTER_PRECURSOR_WINDOW"] = "1"
    invokeParameters["FILTER_LIBRARY"] = "1"
    invokeParameters["WINDOW_FILTER"] = "1"
    invokeParameters["CREATE_CLUSTER_BUCKETS"] = "1"
    invokeParameters["CREATE_ILI_OUTPUT"] = "0"

    return invokeParameters


def get_classic_networking_highres_parameters():
    invokeParameters = {}
    invokeParameters["workflow"] = "METABOLOMICS-SNETS-V2"
    invokeParameters["protocol"] = "None"
    invokeParameters["library_on_server"] = "d.speclibs;"
    invokeParameters["tolerance.PM_tolerance"] = "0.05"
    invokeParameters["tolerance.Ion_tolerance"] = "0.05"
    invokeParameters["PAIRS_MIN_COSINE"] = "0.70"
    invokeParameters["MIN_MATCHED_PEAKS"] = "6"
    invokeParameters["TOPK"] = "10"
    invokeParameters["CLUSTER_MIN_SIZE"] = "2"
    invokeParameters["RUN_MSCLUSTER"] = "on"
    invokeParameters["MAXIMUM_COMPONENT_SIZE"] = "100"
    invokeParameters["MIN_MATCHED_PEAKS_SEARCH"] = "6"
    invokeParameters["SCORE_THRESHOLD"] = "0.7"
    invokeParameters["ANALOG_SEARCH"] = "0"
    invokeParameters["MAX_SHIFT_MASS"] = "100.0"
    invokeParameters["FILTER_STDDEV_PEAK_datasetsINT"] = "0.0"
    invokeParameters["MIN_PEAK_INT"] = "0.0"
    invokeParameters["FILTER_PRECURSOR_WINDOW"] = "1"
    invokeParameters["FILTER_LIBRARY"] = "1"
    invokeParameters["WINDOW_FILTER"] = "1"
    invokeParameters["CREATE_CLUSTER_BUCKETS"] = "1"
    invokeParameters["CREATE_ILI_OUTPUT"] = "0"

    return invokeParameters


def get_featurenetworking_lowres_parameters():
    invokeParameters = {}
    invokeParameters["workflow"] = "FEATURE-BASED-MOLECULAR-NETWORKING"
    invokeParameters["protocol"] = "None"
    invokeParameters["desc"] = "Job Description"
    invokeParameters["library_on_server"] = "d.speclibs;"

    #Networking
    invokeParameters["tolerance.PM_tolerance"] = "2.0"
    invokeParameters["tolerance.Ion_tolerance"] = "0.5"
    invokeParameters["PAIRS_MIN_COSINE"] = "0.70"
    invokeParameters["MIN_MATCHED_PEAKS"] = "6"
    invokeParameters["TOPK"] = "10"
    invokeParameters["MAX_SHIFT"] = "500"

    #Network Pruning
    invokeParameters["MAXIMUM_COMPONENT_SIZE"] = "100"

    #Library Search
    invokeParameters["MIN_MATCHED_PEAKS_SEARCH"] = "6"
    invokeParameters["SCORE_THRESHOLD"] = "0.7"
    invokeParameters["TOP_K_RESULTS"] = "1"
    invokeParameters["ANALOG_SEARCH"] = "0"
    invokeParameters["MAX_SHIFT_MASS"] = "100.0"
    invokeParameters["FILTER_STDDEV_PEAK_datasetsINT"] = "0.0"
    invokeParameters["MIN_PEAK_INT"] = "0.0"
    invokeParameters["FILTER_PRECURSOR_WINDOW"] = "1"
    invokeParameters["FILTER_LIBRARY"] = "1"
    invokeParameters["WINDOW_FILTER"] = "1"

    #Quant
    invokeParameters["QUANT_TABLE_SOURCE"] = ""
    invokeParameters["GROUP_COUNT_AGGREGATE_METHOD"] = "Mean"
    invokeParameters["QUANT_FILE_NORM"] = "RowSum"

    #External tools
    invokeParameters["RUN_DEREPLICATOR"] = "1"

    invokeParameters["email"] = "ccms.web@gmail.com"
    invokeParameters["uuid"] = "1DCE40F7-1211-0001-979D-15DAB2D0B500"

    return invokeParameters

def get_featurenetworking_highres_parameters():
    invokeParameters = {}
    invokeParameters["workflow"] = "FEATURE-BASED-MOLECULAR-NETWORKING"
    invokeParameters["protocol"] = "None"
    invokeParameters["desc"] = "Job Description"
    invokeParameters["library_on_server"] = "d.speclibs;"

    #Networking
    invokeParameters["tolerance.PM_tolerance"] = "0.05"
    invokeParameters["tolerance.Ion_tolerance"] = "0.05"
    invokeParameters["PAIRS_MIN_COSINE"] = "0.70"
    invokeParameters["MIN_MATCHED_PEAKS"] = "6"
    invokeParameters["TOPK"] = "10"
    invokeParameters["MAX_SHIFT"] = "500"

    #Network Pruning
    invokeParameters["MAXIMUM_COMPONENT_SIZE"] = "100"

    #Library Search
    invokeParameters["MIN_MATCHED_PEAKS_SEARCH"] = "6"
    invokeParameters["SCORE_THRESHOLD"] = "0.7"
    invokeParameters["TOP_K_RESULTS"] = "1"
    invokeParameters["ANALOG_SEARCH"] = "0"
    invokeParameters["MAX_SHIFT_MASS"] = "100.0"
    invokeParameters["FILTER_STDDEV_PEAK_datasetsINT"] = "0.0"
    invokeParameters["MIN_PEAK_INT"] = "0.0"
    invokeParameters["FILTER_PRECURSOR_WINDOW"] = "1"
    invokeParameters["FILTER_LIBRARY"] = "1"
    invokeParameters["WINDOW_FILTER"] = "1"

    #Quant
    invokeParameters["QUANT_TABLE_SOURCE"] = ""
    invokeParameters["GROUP_COUNT_AGGREGATE_METHOD"] = "Mean"
    invokeParameters["QUANT_FILE_NORM"] = "RowSum"

    #External tools
    invokeParameters["RUN_DEREPLICATOR"] = "1"

    invokeParameters["email"] = "ccms.web@gmail.com"
    invokeParameters["uuid"] = "1DCE40F7-1211-0001-979D-15DAB2D0B500"

    return invokeParameters

