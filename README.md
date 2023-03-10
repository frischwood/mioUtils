# README for prepareCustomSMET.py script

The script looks for a dataframe in input/dataFrames and write an SMET file (output/rendered.smet) with fields = df.columns and the data section filled with the corresponding content.  
The other keys of the smet file are not filled. As for the name of the .smet file they can be edited afterwards manually.
An example of dataframe in .csv format is given in input/example/

How to use:
 - requirements: pandas, jinja2 
 - put your dataframe in csv format in /input/dataFrames. It will not work if it is not a csv. 
 - Cmd line: python prepareCustomSMET.py
