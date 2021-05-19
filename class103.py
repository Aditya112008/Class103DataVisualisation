# TO CREATE A DATA FRAME WE NEED THE PYTHON MODULE PANDAS
import pandas as pd
df = pd.DataFrame()
print(df)


import pandas as pd
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)

import pandas as pd 
data = [['s101','Aditya',92],['s102','Soham',91],['s103','Amruta',95]]
df = pd.DataFrame(data,columns=['ID','Name','Marks'])
print(df)

#PLOTLY IS USED TO DESIGN GRAPHS

