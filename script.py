

import pandas as pd
def convertDelimitedFileToDF(file,separator):
    return pd.read_csv(file, sep=separator)

def convertDelimitedTextToDf(text,seperator):
    finalArray = []
    lines = text.split("\n")
    for line in lines: 
        entry = line.split(seperator)
        finalArray.append(entry)


    # step 2: convert the array to a df
    return pd.DataFrame(finalArray)

def convertDfToXLSX(df,filename="Untitled"):  
    df.to_excel(filename,header = False,index = False)

def convertTextToXLSX(text,seperator,filename="Untitled"):
    df = convertDelimitedTextToDf(text,seperator)
    convertDfToXLSX(df,filename)
    