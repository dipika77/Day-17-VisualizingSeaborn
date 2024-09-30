#Visualizing a categorical and Quantitative variable

#instructions
'''Use sns.catplot() to create a count plot using the survey_data DataFrame with "Internet usage" on the x-axis.
Make the bars horizontal instead of vertical.
Separate this plot into two side-by-side column subplots based on "Age Category", which separates respondents into those that are younger than 21 vs. 21 and older.'''

 # Separate into column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data,
            kind="count", col = 'Age Category')

# Show plot
plt.show()


#instructions
'''Use the survey_data DataFrame and sns.catplot() to create a bar plot with "Gender" on the x-axis and "Interested in Math" on the y-axis.'''

# Create a bar plot of interest in math, separated by gender
sns.catplot( x = 'Gender', y = 'Interested in Math', data = survey_data, kind = 'bar')


# Show plot
plt.show()


#instructions
'''Use sns.catplot() to create a bar plot with "study_time" on the x-axis and final grade ("G3") on the y-axis, using the student_data DataFrame.
Using the order parameter and the category_order list that is provided, rearrange the bars so that they are in order from lowest study time to highest.
Update the plot so that it no longer displays confidence intervals.'''

# List of categories from lowest to highest
category_order = ["<2 hours", 
                  "2 to 5 hours", 
                  "5 to 10 hours", 
                  ">10 hours"]

# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=category_order, ci = None)

# Show plot
plt.show()



#Creating box plot

#instructions
'''Use sns.catplot() and the student_data DataFrame to create a box plot with "study_time" on the x-axis and "G3" on the y-axis. Set the ordering of the categories to study_time_order.'''

# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours", 
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
g = sns.catplot( x = 'study_time', y = 'G3', data = student_data, kind = 'box', order = study_time_order)

# Show plot
plt.show()


#instructions
'''Use sns.catplot() to create a box plot with the student_data DataFrame, putting "internet" on the x-axis and "G3" on the y-axis.
Add subgroups so each box plot is colored based on "location".
Do not display the outliers.'''

# Create a box plot with subgroups and omit the outliers
g = sns.catplot( x = 'internet', y = 'G3', data = student_data, kind = 'box', sym = '', hue = 'location')

# Show plot
plt.show()


#instructions
'''Adjust the code to make the box plot whiskers to extend to 0.5 * IQR. Recall: the IQR is the interquartile range.
Change the code to set the whiskers to extend to the 5th and 95th percentiles.
Change the code to set the whiskers to extend to the min and max values.'''

# Extend the whiskers to the 5th and 95th percentile
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=0.5)

# Show plot
plt.show()


# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[5, 95])

# Show plot
plt.show()

# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[0, 100])

# Show plot
plt.show()



#Point plots

#instructions
'''Use sns.catplot() and the student_data DataFrame to create a point plot with "famrel" on the x-axis and number of absences ("absences") on the y-axis.
Add "caps" to the end of the confidence intervals with size 0.2.
Remove the lines joining the points in each category.'''

# Remove the lines joining the points
sns.catplot(x="famrel", y="absences",
            data=student_data,
            kind="point",
            capsize=0.2,
            join=False)

# Show plot
plt.show()



#instructions
'''Use sns.catplot() and the student_data DataFrame to create a point plot with relationship status ("romantic") on the x-axis and number of absences ("absences") on the y-axis. Color the points based on the school that they attend ("school").
Turn off the confidence intervals for the plot.
Since there may be outliers of students with many absences, use the median function that we've imported from numpy to display the median number of absences instead of the average.'''

# Import median function from numpy
from numpy import median

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			estimator = median, data=student_data,
            kind="point",
            hue="school",
            ci=None)

# Show plot
plt.show()



#Changing plot style and color
#instructions
'''Set the style to "whitegrid" to help the audience determine the number of responses in each category.'''

# Set the color palette to "Purples"
sns.set_style("whitegrid")


# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", 
                  "Often", "Always"]

sns.catplot(x="Parents Advice", 
            data=survey_data, 
            kind="count", 
            order=category_order)

# Show plot
plt.show()


#instructions
'''Change the context to "poster", which is the largest scale available.'''

# Change the context to "poster"
sns.set_context("poster")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()


#instructions
'''Set the style to "darkgrid".
Set a custom color palette with the hex color codes "#39A7D0" and "#36ADA4".'''

# Set the style to "darkgrid"
sns.set_style('darkgrid')

# Set a custom color palette
sns.set_palette(['#39A7D0', '#36ADA4'])

# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age", 
            data=survey_data, kind="box")

# Show plot
plt.show()


#Adding titles and labels
#instructions
'''Identify what type of object plot g is and assign it to the variable type_of_g'''

# Create scatter plot
g = sns.relplot(x="weight", 
                y="horsepower", 
                data=mpg,
                kind="scatter")

# Identify plot type
type_of_g = type(g)

# Print type
print(type_of_g)


#instructions
'''Add the following title to this plot: "Car Weight vs. Horsepower".'''

# Create scatter plot
g = sns.relplot(x="weight", 
                y="horsepower", 
                data=mpg,
                kind="scatter")

# Add a title "Car Weight vs. Horsepower"
g.fig.suptitle("Car Weight vs. Horsepower")

# Show plot
plt.show()


#instructions
'''Add the following title to the plot: "Average MPG Over Time".
Label the x-axis as "Car Model Year" and the y-axis as "Average MPG".'''

# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean", 
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")

# Add x-axis and y-axis labels
g.set(xlabel = 'Car Model Year', ylabel = 'Average MPG')


# Show plot
plt.show()


#instructions
'''Rotate the x-tick labels 90 degrees.'''

# Create point plot
sns.catplot(x="origin", 
            y="acceleration", 
            data=mpg, 
            kind="point", 
            join=False, 
            capsize=0.1)

# Rotate x-tick labels
plt.xticks(rotation = 90)

# Show plot
plt.show()


#Putting it all together
#instructions
'''Set the color palette to "Blues".
Add subgroups to color the box plots based on "Interested in Pets".
Set the title of the FacetGrid object g to "Age of Those Interested in Pets vs. Not".
Make the plot display using a Matplotlib function.'''

# Set palette to "Blues"
sns.set_palette('Blues')

# Adjust to add subgroups based on "Interested in Pets"
g = sns.catplot(x="Gender",
                y="Age", data=survey_data, 
                kind="box", hue= "Interested in Pets")

# Set title to "Age of Those Interested in Pets vs. Not"
g.fig.suptitle("Age of Those Interested in Pets vs. Not")

# Show plot
plt.show()


#  instructions
'''Set the figure style to "dark".
Adjust the bar plot code to add subplots based on "Gender", arranged in columns.
Add the title "Percentage of Young People Who Like Techno" to this FacetGrid plot.
Label the x-axis "Location of Residence" and y-axis "% Who Like Techno".'''

# Set the figure style to "dark"
sns.set_style("dark")

# Adjust to add subplots per gender
g = sns.catplot(x="Village - town", y="Likes Techno", 
                data=survey_data, kind="bar",
                col = 'Gender')

# Add title and axis labels
g.fig.suptitle("Percentage of Young People Who Like Techno", y=1.02)
g.set(xlabel="Location of Residence", 
       ylabel="% Who Like Techno")

# Show plot
plt.show()