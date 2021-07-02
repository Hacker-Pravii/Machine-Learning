import pandas as pd
x="abcde"
data={"head":pd.Series([1,2,3,4,5],index=range(0,5)),
      "Details":pd.Series([5,6,7,8,9],index=range(0,5))}
print(pd.DataFrame(data))

data={"head":pd.Series([1,2,3,4,5],index=(i for i in x)),
      "Details":pd.Series([5,6,7,8,9],index=(i for i in x))}
print(pd.DataFrame(data))


    
