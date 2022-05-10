# Importing Values
import pandas as pd
import plotly.figure_factory as ff

# Initializong Data
df = pd.read_csv("data.csv")

# Creating Graph
fig = ff.create_distplot(
                            [df["Avg Rating"].tolist()],
                            ["Avg Rating"],
                            colors=["royalblue"],
                            curve_type="normal"
                        )

# Updating Graph
fig.layout.update({
                    "title": "Average Rating Of Amazon",
                    "xaxis": {"title": "Rating"}
                 })

# Plotting Graph
print('Plotting...')
fig.show()