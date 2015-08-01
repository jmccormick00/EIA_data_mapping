import pandas as pd

plantFile = 'data/PlantY2012.csv'
gen_opFile = 'data/GeneratorY2012_op.csv'
gen_propFile = 'data/GeneratorY2012_prop.csv'

plant_DF = pd.read_csv(plantFile)
genOp_DF = pd.read_csv(gen_opFile)
genProp_DF = pd.read_csv(gen_propFile)

# Pull the data you want from the plant dataframe
p_sub = plant_DF[['Transmission or Distribution System Owner', 'Plant Code', 'Primary Purpose (NAICS Code)', 'Latitude', 'Longitude']]
genOpMaster_DF = pd.merge(genOp_DF, p_sub, on='Plant Code')
#genPropMaster_DF = pd.merge(gen_propFile, p_sub, on='Plant Code')

#save the data to csv files
genOpMaster_DF.to_csv("data/Generators_Operating_Master.csv", index=False)
#genPropMaster_DF.to_csv("Generators_Proposed_Master.csv", index=False)

#Pull the plants by energy source
ng = genOpMaster_DF[genOpMaster_DF['Energy Source 1'] == "NG"]
ng.to_csv('C:/Dropbox/Docs/Code/PyCharm/Mapping/data/NaturalGas_op.csv')

bit = genOpMaster_DF[genOpMaster_DF['Energy Source 1'] == "BIT"]
bit.to_csv('C:/Dropbox/Docs/Code/PyCharm/Mapping/data/BIT_Coal_op.csv')

ant = genOpMaster_DF[genOpMaster_DF['Energy Source 1'] == "ANT"]
ant.to_csv('C:/Dropbox/Docs/Code/PyCharm/Mapping/data/ANT_Coal_op.csv')

sub = genOpMaster_DF[genOpMaster_DF['Energy Source 1'] == "SUB"]
sub.to_csv('C:/Dropbox/Docs/Code/PyCharm/Mapping/data/SUB_op.csv')

nuc = genOpMaster_DF[genOpMaster_DF['Energy Source 1'] == "NUC"]
nuc.to_csv('C:/Dropbox/Docs/Code/PyCharm/Mapping/data/NUC_op.csv')

lig = genOpMaster_DF[genOpMaster_DF['Energy Source 1'] == "LIG"]
lig.to_csv('C:/Dropbox/Docs/Code/PyCharm/Mapping/data/LIG_op.csv')

solar = genOpMaster_DF[genOpMaster_DF['Energy Source 1'] == "SUN"]
solar.to_csv('C:/Dropbox/Docs/Code/PyCharm/Mapping/data/SUN_op.csv')

wind = genOpMaster_DF[genOpMaster_DF['Energy Source 1'] == "WND"]
wind.to_csv('C:/Dropbox/Docs/Code/PyCharm/Mapping/data/WND_op.csv')
