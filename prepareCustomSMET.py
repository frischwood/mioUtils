"""
Renders an SMET file with data contained in input/dataFrames/df_data.csv
Can be ran from command line if files are in the correct folders
"""
import pandas as pd
import jinja2
import os


TEMPLATE_PATH = "input/templates/"
DATAFRAME_PATH = "input/dataFrames/"
OUTPUT_PATH = "output/"

# get dataframe
if os.listdir(DATAFRAME_PATH):
    df = pd.read_csv(os.listdir(DATAFRAME_PATH)[0])
else:
    print("there is no data frame in input/dataFrames")

# form fields string
fieldsString = " ".join(df.columns)
# for data strings
dataStrings = ""
for row in df.iterrows():
    listRowElem = [str(RowElem) for RowElem in row[1].values]
    dataStrings += " ".join(listRowElem) + "\n"
# group strings in dict for rendering template
dictTemplateSmet = {"fields":fieldsString, "data":dataStrings}

# get template
templateLoader = jinja2.FileSystemLoader(TEMPLATE_PATH)
templateEnv = jinja2.Environment(loader=templateLoader)
template_smet = templateEnv.get_template("data.smet")
# render template with dict
rendered = template_smet.render(dictTemplateSmet)
# write template
with open(OUTPUT_PATH + "rendered.smet",'w') as f:
    f.write(rendered)

