import glob
import pandas as pd

path = r'C:\Users\Kyle Coapman\Google Drive\Project Kilkenny\Khan Academy Grading\Q4 Khan Academy Work'
filenames = glob.glob(path + "/*.csv")
nAssignments = len(filenames)

## Create Data Frame with Names
DF_temp = pd.read_csv(filenames[0])
GradeFrame = pd.DataFrame(index=DF_temp.iloc[:,1])
StudentNames = GradeFrame.index
GradeFrame.head()

## Read in Multiple Assignments

for name in filenames:
    DF_temp = pd.read_csv(name)
    AssignmentName = DF_temp.iloc[1,0]
    DFColumns = DF_temp.columns.values
    DFColumns[3] = AssignmentName
    DF_temp.columns = DFColumns
    DF_subset = pd.DataFrame(data=DF_temp.loc[:,AssignmentName])
    DF_subset.index = StudentNames
    GradeFrame = pd.concat([GradeFrame, DF_subset], axis=1)

GradeFrame.to_excel(r"C:\Users\Kyle Coapman\Google Drive\Project Kilkenny\Khan Academy Grading\CompleteKAGrades.xlsx")