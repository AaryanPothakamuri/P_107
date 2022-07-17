from cv2 import mean
import pandas as pd
import plotly.express as px
import csv

#reading files df = data frame
df=pd.read_csv("data1.csv")
mean = df.groupby(["student_id", "level"], as_index= False)["attempt"].mean()
fig=px.scatter( mean, 
     x = "student_id",
     y = "level",
     size = "attempt",
    color = "attempt"
   )

fig.show()