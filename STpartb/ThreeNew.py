import pandas as pd

def writeToSheet(Names, USN, S1, S2, S3):

    writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')

    df = pd.DataFrame({'Name': Names, 'USN': USN, 'Subject 1': S1, 'Subject 2': S2, 'Subject 3': S3})

    df.to_excel(writer, sheet_name='Sheet1', index=False)

    writer.save()

if __name__ == '__main__':
    Names=[]
    USN=[]
    Sub1=[]
    Sub2=[]
    Sub3=[]
    inpFile = open("Input.txt",'r')
    for line in inpFile:
        n,u,m1,m2,m3 = line.split()
        Names.append(n)
        USN.append(u)
        Sub1.append(int(m1))
        Sub2.append(int(m2))
        Sub3.append(int(m3))
    
    inpFile.close()
    
    writeToSheet(Names,USN,Sub1,Sub2,Sub3)

