import arcpy

# arcpy.env.workspace= r"D:\Gauspak other data\Utility_Data.gdb"
# fil = open(r"C:\Users\student.HPWS66.000\Desktop\Arcpy\test.txt","w")

# listdatasets =arcpy.ListDatasets()
# # for i in listdatasets:
# print(listdatasets)

# listfeatclass = arcpy.ListFeatureClasses("*","All","ElectricalNetwork")
# # for l in listfeatclass:
# print(listfeatclass)


#Readig the input datasets
arcpy.env.workspace= r"D:\Gauspak other data\Utility_Data.gdb"

#output path list of datasets and feature class
fil = open(r"C:\Users\student.HPWS66.000\Desktop\Arcpy\test.txt","w")
#Read the Datasets
lidist =arcpy.ListDatasets()
for lst in lidist:
    #Read the featue classs
    listfeatclass = arcpy.ListFeatureClasses("*","All",lst)
    for fc in listfeatclass:
                # print(listdatasets + "|"+ listfeatclass)
        fil.write(lst+"|"+fc+"\n")
#File Close      
fil.close()

print("Completed")

