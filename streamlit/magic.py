# Draw a title and some text to the app;
'''
# This the Document Title

This is some _markdown_.
''';
import pandas as pd
#df Draw the dataframe
df = pd.DataFrame({'col':[1,2,3]})

x = 10;
'x',x; # Draw the string 'x' and then the value of x

# Also works with  most supported chart types

import matplotlib.pyplot as plt
import numpy as np;
arr = np.random.normal(1,1,size=100)
fig,ax = plt.subplot() # fig for Draw a Matplotlib chart
ax.hist(arr,bins = 20)