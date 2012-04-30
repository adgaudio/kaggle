a = '''"rowID","chunkID","position_within_chunk","month_most_common","weekday","hour","S
ed..Resultant_1","WindSpeed..Resultant_1018","Ambient.Max.Temperature_14","Ambient.Max.T
mperature_57","Ambient.Max.Temperature_76","Ambient.Max.Temperature_2001","Ambient.Max.T
n.Temperature_22","Ambient.Min.Temperature_50","Ambient.Min.Temperature_52","Ambient.Min
n.Temperature_3301","Ambient.Min.Temperature_6005","Sample.Baro.Pressure_14","Sample.Bar
_57","Sample.Baro.Pressure_76","Sample.Baro.Pressure_2001","Sample.Baro.Pressure_3301","
Sample.Max.Baro.Pressure_50","Sample.Max.Baro.Pressure_52","Sample.Max.Baro.Pressure_57"
_3301","Sample.Max.Baro.Pressure_6005","Sample.Min.Baro.Pressure_14","Sample.Min.Baro.Pr
Pressure_57","Sample.Min.Baro.Pressure_76","Sample.Min.Baro.Pressure_2001","Sample.Min.B
t_10_8003","target_11_1","target_11_32","target_11_50","target_11_64","target_11_1003","
get_15_57","target_2_57","target_3_1","target_3_50","target_3_57","target_3_1601","targe
et_4_1601","target_4_2001","target_4_4002","target_4_4101","target_4_6006","target_4_800
_8003","target_9_4002","target_9_8003"'''


b = a.split(',')


d = []
for x in b:
    if 'weekday' == x:
        d.append(x + " varchar")
    else:
        d.append(x + " double precision")
e = ",".join(d)

print "create table raw_data (%s);" % e

print "copy raw_data from './TrainingData.csv' DELIMITERS ',' CSV;"
