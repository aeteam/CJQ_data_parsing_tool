import pandas
import os
import csv

def mkcsv():
    test2=item.split('_')[2]
    orin_path='C:\\CJQ_DATA\\'+item+'\\FioSynthFlash\\nvme_workload'
    files_1=os.listdir(orin_path)
    if not os.path.exists('C:\\CJQ_DATA\\'+test2): os.makedirs('C:\\CJQ_DATA\\'+test2)
    for ns in files_1:
        test3=ns.split('_')[3]
        origin=pandas.read_csv(r'C:\\CJQ_DATA\\'+item+'\\FioSynthFlash\\nvme_workload\\'+ns+'\\'+ns+'.csv',usecols=[0,2,4,14,16,18,8,20,28,30],skiprows=[11,12,13])
        df=pandas.DataFrame(origin) 
        df['DUT']=dut
        df['Namespace']=test3
        df['Cycle']=test2
        df=df[['DUT','Namespace','Cycle','Jobname','Read_BW','Write_BW','P99_Read_Latency','P99.99_Read_Latency','P99.9999_Read_Latency','Max_Read_Latency','P99.99_Write_Latency','P99.9999_Write_Latency','Max_Write_Latency']]
        df.to_csv('C:\\CJQ_DATA\\'+test2+'\\Workload_Loop_Stress_'+test3+'_'+test2+'_'+dut+'.csv', index=False)    

files=os.listdir('C:\\CJQ_DATA')
for item in files:
    if 'WN5304403EN1C' in item:
        dut='W1-01'
        mkcsv()
    if 'WN5304407PN1C' in item:
        dut='W1-02'
        mkcsv()
    if 'WN5304406NN1C' in item:
        dut='W1-03'
        mkcsv()
    if 'WN5304403KN1C' in item:
        dut='W1-04'
        mkcsv()
    if 'WN530440BLN1C' in item:
        dut='W1-05'
        mkcsv()
    if 'WN53044073N1C' in item:
        dut='W1-06'
        mkcsv()
    if 'WN5304407UN1C' in item:
        dut='W1-07'
        mkcsv()
    if 'WN5304407UN1C' in item:
        dut='W1-07'
        mkcsv()
    if 'WN53044064N1C' in item:
        dut='W1-08'
        mkcsv()
    if 'WN530440C6N1C' in item:
        dut='W1-09'
        mkcsv()
    if 'WN530440AUN1C' in item:
        dut='W1-10'
        mkcsv()
    if 'WN5304407YN1C' in item:
        dut='W1-11'
        mkcsv()
    if 'WN5304403XN1C' in item:
        dut='W1-12'
        mkcsv()
    if 'WN5304407VN1C' in item:
        dut='W1-13'
        mkcsv()
    if 'WN5304409SN1C' in item:
        dut='W1-14'
        mkcsv()
    if 'WN5304408SN1C' in item:
        dut='W1-15'
        mkcsv()
    if 'WN530440AKN1C' in item:
        dut='W1-16'
        mkcsv()
    if 'WN53044091N1C' in item:
        dut='W1-17'
        mkcsv()
    if 'WN530440AMN1C' in item:
        dut='W1-18'
        mkcsv()
    if 'WN530440ANN1C' in item:
        dut='W1-19'
        mkcsv()
    if 'WN5304407RN1C' in item:
        dut='W1-20'
        mkcsv()
    if 'WN530440B3N1C' in item:
        dut='W1-21'
        mkcsv()
    if 'WN5304407NN1C' in item:
        dut='W1-22'
        mkcsv()
    if 'WN530440B9N1C' in item:
        dut='W1-23'
        mkcsv()
    if 'WN5304407WN1C' in item:
        dut='W1-24'
        mkcsv()
    if 'WN5304403LN1C' in item:
        dut='W1-25'
        mkcsv()
    if 'WN5304405GN1C' in item:
        dut='W1-26'
        mkcsv()
    if 'WN5304405FN1C' in item:
        dut='W1-27'
        mkcsv()
    if 'WN530440CCN1C' in item:
        dut='W1-28'
        mkcsv()
    if 'WN530440BTN1C' in item:
        dut='W1-29'
        mkcsv()
    if 'WN5304403JN1C' in item:
        dut='W1-30'
        mkcsv()
    if 'WN5304403ZN1C' in item:
        dut='W1-31'
        mkcsv()
    if 'WN5304403UN1C' in item:
        dut='W1-32'
        mkcsv()



