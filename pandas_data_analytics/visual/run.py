import seaborn as sns
import matplotlib.pyplot as plt
import pandas_data_analytics.utils as u

# Apply the default theme
sns.set_theme()

# # Load an example dataset
# tips = sns.load_dataset("tips")

# print(tips.head())
# print(tips.describe())
# print(tips['size'].unique())

# # Create a visualization
# sns.relplot(
#     data=tips,
#     x="total_bill", y="tip", col="time",
#     hue="smoker", style="smoker", size="size",
# )

dots = sns.load_dataset("dots")
u.general_df_stats(dots)
print(dots['align'].unique())
sns.relplot(
    data=dots, kind="line",
    x="time", y="firing_rate", col="align",
    hue="choice", size="coherence", style="choice",
    facet_kws=dict(sharex=False),
)



# plt.show()
