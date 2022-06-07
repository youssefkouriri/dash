from dash.dash_table import DataTable, FormatTemplate
import main
import pandas as pd
table1 =[{'status': 'PASS', 'wallc-locktime': 542.0, 'hostname': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpu': 432.0, 'optimalcpu': 432.0, 'CUSTOM_KPI-No._of_Flops': 159439.0, 'Design-testname': '/powerpro/tests/main/qa_repository/shasta_qor/testcases/ati/pa_data/ati_tcc0.1_prob0.4.def high SKIP_VISA'}, {'status': 'FAIL', 'wallc-locktime': 642.0, 'hostname': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpu': 332.0, 'optimalcpu': 332.0, 'CUSTOM_KPI-No._of_Flops': 259439.0, 'Design-testname': '/powerpro/tests/main/qa_repository/shasta_qor/testcases/ati/pa_data/ati_cg_pa_rc_integrated.def high SKIP_VISB'}, {'status': 'PASS', 'wallc-locktime': 742.0, 'hostname': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpu': 232.0, 'optimalcpu': 232.0, 'CUSTOM_KPI-No._of_Flops': 359439.0, 'mem': 200.0, 'Design-testname': 
'/powerpro/tests/main/qa_repository/shasta_qor/testcases/Ipars/Ipars.def high SKIP_VISC'}, {'status': 'PASS', 'wallc-locktime': 842.0, 'hostname': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpu': 132.0, 'optimalcpu': 132.0, 'CUSTOM_KPI-No._of_Flops': 459439.0, 'power': 300.0, 'Design-testname': '/powerpro/tests/main/qa_repository/shasta_qor/testcases/Ipars/Ipars.def high SKIP_VISD'}, {'status': 'FAIL', 'wallc-locktime': 942.0, 'hostname': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpu': 532.0, 'optimalcpu': 532.0, 'CUSTOM_KPI-No._of_Flops': 559439.0, 'Design-testname': '/powerpro/tests/main/qa_repository/shasta_qor/testcases/Ipars/Ipars.def high SKIP_VISE'},{'status': 'FAIL', 'wallc-locktime': 942.0, 'hostname': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpu': 532.0, 'optimalcpu': 532.0, 'CUSTOM_KPI-No._of_Flops': 559439.0, 'Design-testname': '/powerpro/tests/main/qa_repository/shasta_qor/testcases/Ipars/Ipars.def high SKIP_VISF'}]

table2 = [{'status': 'PASS', 'wallc-locktime': 530.0, 'hostname': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpu': 450.0, 'optimalcpu': 430.0, 'CUSTOM_KPI-No._of_Flops': 159430.0, 'Design-testname': '/powerpro/tests/main/qa_repository/shasta_qor/testcases/ati/pa_data/ati_tcc0.1_prob0.4.def high SKIP_VISA'}, {'status': 'FAIL', 'wallc-locktime': 647.0, 'hostname': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpu': 339.0, 'optimalcpu': 320.0, 'CUSTOM_KPI-No._of_Flops': 259410.0, 'Design-testname': '/powerpro/tests/main/qa_repository/shasta_qor/testcases/ati/pa_data/ati_cg_pa_rc_integrated.def high SKIP_VISB'}, {'status': 'PASS', 'wallc-locktime': 749.0, 'hostname': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpu': 132.0, 'optimalcpu': 332.0, 'CUSTOM_KPI-No._of_Flops': 359430.0, 'mem': 250.0, 'Design-testname': 
'/powerpro/tests/main/qa_repository/shasta_qor/testcases/Ipars/Ipars.def high SKIP_VISC'}, {'status': 'PASS', 'wallc-locktime': 842.0, 'hostname': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpu': 130.0, 'optimalcpu': 133.0, 'CUSTOM_KPI-No._of_Flops': 459440.0, 'power': 310.0, 'Design-testname': '/powerpro/tests/main/qa_repository/shasta_qor/testcases/Ipars/Ipars.def high SKIP_VISD'}, {'status': 'FAIL', 'wallc-locktime': 942.0, 'hostname': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpu': 539.0, 'optimalcpu': 531.0, 'CUSTOM_KPI-No._of_Flops': 559439.0, 'Design-testname': '/powerpro/tests/main/qa_repository/shasta_qor/testcases/Ipars/Ipars.def high SKIP_VISE'}]

table_final = []
dict1 = {}
def get_taller_table(table1,table2):
    if len(table1)> len(table2):
        return table1
    else:
        return table2  
          
def get_shorter_table(table1,table2):
    if len(table1)<= len(table2):
        return table1
    else:
        return table2     

def change_table(table,version):
    table_mod = []
    dict1={}
    for dict in table:
       for key in dict:
           dict1.update({key + version: dict[key]})
       table_mod.append(dict1)
       dict1={}
    return table_mod 
               

def merge_qor(table1,table2,version1,version2):
    table_pro = change_table(get_taller_table(table1,table2),version1)
    for i in range(len(table_pro)):
        for j in  range(len(change_table(get_shorter_table(table1,table2), version2))):
           if table_pro[i]["Design-testname" + version1] == change_table(get_shorter_table(table1,table2), version2)[j]["Design-testname" + version2]:
               table_pro[i].update(change_table(get_shorter_table(table1,table2), version2)[j])
    
    for i in table_pro:
        i.pop("Design-testname" + version2, "done")

    return table_pro

#print(merge_qor(table1,table2,"VersionA","VersionB")[0])
#print(len(merge_qor(table1,table2,"VersionA","VersionB")))
      
def perc_change(x,y):
	try:
				
		diff_per = round(((float(x) - float(y)))/float(y),4)
	except:	
		diff_per = ""
	return diff_per

#dictA = {'statusVersionA': 'PASS', 'wallc-locktimeVersionA': 542.0, 'hostnameVersionA': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionA': 432.0, 'optimalcpuVersionA': 432.0, 'CUSTOM_KPI-No._of_FlopsVersionA': 159439.0, 'Design-testnameVersionA': '/powerpro/tests/main/qa_repository/shasta_qor/testcases/ati/pa_data/ati_tcc0.1_prob0.4.def high SKIP_VISA', 'statusVersionB': 'PASS', 'wallc-locktimeVersionB': 542.0, 'hostnameVersionB': 'svr-inn-clpqor-32.inn.mentorg.com', 'cpuVersionB': 432.0, 'optimalcpuVersionB': 432.0, 'CUSTOM_KPI-No._of_FlopsVersionB': 159439.0}
#dict1.update(dictA)
#for key in dictA:
    #for key2 in dictA:
        #if key.replace("VersionA","") == key2.replace("VersionB",""):

          #dict1.update({key.replace("VersionA","") + "diff" : perc_change(dictA[key],dictA[key2]) })

   
#print(dict1)
# for dict in merge_qor(table1,table2,"VersionA","VersionB"):
#     dict1.update(dict)
#     for key in dict:
#         for key2 in dict:
#            if key.replace("VersionA","") == key2.replace("VersionB",""):
#                dict1.update({key.replace("VersionA","") + "diff" : perc_change(dict[key],dict[key2]) })
#     table_final.append(dict1)
#     dict1 = {}

# print(table_final)
#print(len(table_final))
vid = []
vid2 = []
for dict in table_final:
    for key in dict:
        if key.endswith("diff") and dict[key] !="" :
            vid.append(key)
    

for dict in table_final:
    for key in dict:
        vid2.append(key)     
   
#print(merge_qor(table1,table2,"VersionA","VersionB"))
   
def completion_rate(table):
    i=0
    for dic in table:
        for key in dic:
            if key =="status" and dic[key] == "PASS":
                i += 1
    return (i/len(table))*100 

print(completion_rate(table2))

def append_diff(table1,table2,version1,version2):
    table_final =[]
    dict1={}
    for dict in merge_qor(table1,table2,version1,version2):
        dict1.update(dict)
        for key in dict:
         for key2 in dict:
           if key.replace(version1,"") == key2.replace(version2,""):
               dict1.update({key.replace(version1,"") + "diff" : perc_change(dict[key],dict[key2]) })
        table_final.append(dict1)
        dict1 = {}
    return table_final

def get_all_columns(table1,table2,version1,version2):
    vid2= []
    for dict in append_diff(table1,table2,version1,version2):
        for key in dict:
          vid2.append(key) 
    return vid2

def get_diff_headers(table1,table2,version1,version2):
    vid = []
    for dict in append_diff(table1,table2,version1,version2):
      for key in dict:
        if key.endswith("diff") and dict[key] !="" :
            vid.append(key)
    final_vid = list(dict.fromkeys(vid))         
    return final_vid     

         
