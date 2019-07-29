#.mat file to .csv
import scipy.io as sio
import csv

#mat = scipy.io.loadmat('data_all.mat')
#mat = {k:v for k, v in mat.items() if k[0] != '_'}
#data = pd.DataFrame({k: pd.Series(v[0]) for k, v in mat.items()})
#data.to_csv("data.csv")

#mat_contents = sio.loadmat('data_all.mat')
#X_data = mat_contents['data_all']
#
#with open("data.csv","w")as f:
#    data = csv.writer(f)
#    data.writerows(X_data)

#with open('data.csv', 'rt') as File:  
#    reader = csv.reader(File)
#    print("Total no. of rows: %d"%(reader.line_num))
##    for row in reader:
##        print(row)        
#        
import pandas as pd

df = pd.read_csv('data.csv')
