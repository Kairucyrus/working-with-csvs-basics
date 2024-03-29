import pandas as pd

from matplotlib import pyplot as plt

dta = pd.read_csv('countries.csv')

# print(dta)
#comparing population growth of USA and Chine from 1952 through 2007:

#boolean check that returns true where column 'country' reads 'United States'

us = dta[dta.country == "United States"]
print(us)
#returns
"""
		country			year 	population
1608	United States	1952	157553000
1609	United States	1957	171984000
1610	United States	1962	186538000
1611	United States	1967	198712000
1612	United States	1972	209896000
1613	United States	1977	220239000
1614	United States	1982	232187835
1615	United States	1987	242803533
1616	United States	1992	256894189
1617	United States	1997	272911760
1618	United States	2002	287675526
1619	United States	2007	301139947
"""

# print(dta[dta.country == 'Uniited States']) # returns empty data frame

china = dta[dta.country == 'China']
print(china)
#returns 
"""
    country	year	population
288	China	1952	556263527
289	China	1957	637408000
290	China	1962	665770000
291	China	1967	754550000
292	China	1972	862030000
293	China	1977	943455000
294	China	1982	1000281000
295	China	1987	1084035000
296	China	1992	1164970000
297	China	1997	1230075000
298	China	2002	1280400000
299	China	2007	1318683096
"""


"""setting initial population(1952) as 100%
us.population / us.population.iloc[0] *100
china.population / china.population.iloc[0] *100
"""
plt.plot(us.year, us.population / us.population.iloc[0] *100)
plt.plot(china.year, china.population / china.population.iloc[0] *100)
plt.legend(['United States', 'China'])
plt.title('Population growth comparison (China vs USA) - 1952-2007')
plt.xlabel("Year")
plt.ylabel('Population growth (first year = 100)')
plt.show()





