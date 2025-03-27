import pandas as pd   #---------------------------------------------------------------------------------------------------------------------------->  Allows us to make data frames
import matplotlib.pyplot as plt #------------------------------------------------------------------------------------------------------------------>  Allows us to visualize the data with various graphs

print(f"Pandas version: {pd.__version__}")


bob_data = {    #---------------------------------------------------------------------------------------------------------------------------------->  Contains the data regarding each element, as well as the percentage of paintings the elements have been in
    "Painting Elements:": ["At least one tree", "At least two trees", "Deciduous tree","Coniferous tree","Clouds","At least one mountain","Grass","Lake","River or stream","Bushes","Snow-covered mountain","At least two mountains","Man-made structure","Cumulus clouds","Rocks","Sun","Waterfall","Snow","Cabin","Winter setting","Frame","Path","Oval frame","Ocean","Waves","Beach","Cirrus clouds","Fence","Fog","Hills","Barn","Nighttime","Flowers","Palm tree","Cliff","Bridge",],
    "Percentage of Paintings Containing the Element:": [91, 85, 56, 53, 44, 39, 36, 34, 33, 30, 26, 24, 22, 21, 20, 20, 20, 19, 18, 18, 13, 13, 9, 9, 9, 7, 7, 6, 6, 4, 4, 3, 2, 2, 2, 2]
}                                                                                                                                                                     
                                                                                                                                                                           
df = pd.DataFrame(bob_data) #---------------------------------------------------------------------------------------------------------------------->  Makes a data frame containing the data above


print(df)   #-------------------------------------------------------------------------------------------------------------------------------------->  Prints the data frame

plt.figure(figsize=(15, 11))  #-------------------------------------------------------------------------------------------------------------------->  Sets the figure size (width, height in inches)
bars = plt.barh(df["Painting Elements:"], df["Percentage of Paintings Containing the Element:"], color="skyblue")   #------------------------------>  Creates the bars of the bar graph


most_common_index = df["Percentage of Paintings Containing the Element:"].idxmax() #------/-------------------------------------------------------->  Highlights the most common element
bars[most_common_index].set_color("green") #---------------------------------------------/


plt.xlabel("Percentage of Paintings Containing the Element") #-------------------\
plt.ylabel("Painting Elements") #                                                 |---------------------------------------------------------------->  Adds labels and a title to the graph
plt.title("Frequency of Elements in Bob Ross Paintings") #-----------------------/

plt.xticks(rotation=45)  #------------------------------------------------------------------------------------------------------------------------->  Rotates the x-axis labels


plt.tight_layout()  #------------------------------------------------------------------------------------------------------------------------------>  Ensures the layout looks good


plt.show() #--------------------------------------------------------------------------------------------------------------------------------------->  Shows the bar graph


plt.pie(df["Percentage of Paintings Containing the Element:"], labels=df["Painting Elements:"], rotatelabels=True) #------------------------------->  Makes a pie chart
plt.show() #--------------------------------------------------------------------------------------------------------------------------------------->  Shows the pie chart