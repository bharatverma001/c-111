import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("data.csv")
Height_list = df["Height(Inches)"].to_list()
Weight_list = df["Weight(Pounds)"].to_list()
height_mean = statistics.mean(Height_list)
Weight_mean = statistics.mean(Weight_list)
height_mode = statistics.mode(Height_list)
weight_mode = statistics.mode(Weight_list)
height_median= statistics.median(Height_list)
weight_median = statistics.median(Weight_list)


height_std_devation = statistics.stdev(Height_list)
weight_std_devation = statistics.stdev(Weight_list)

height_first_std_devation_start,height_first_std_devation_end = height_mean-height_std_devation,height_mean+height_std_devation
height_second_std_devation_start,height_second_std_devation_end = height_mean-(2*height_std_devation),height_mean+(2*height_std_devation)
height_thrice_std_devation_start,height_thrice_std_devation_end = height_mean-(3*height_std_devation),height_mean+(3*height_std_devation)

weight_first_std_devation_start,weight_first_std_devation_end = weight_mean-weight_std_devation,weight_mean+weight_std_devation
weight_second_std_devation_start,weight_second_std_devation_end = weight_mean-(2*weight_std_devation),weight_mean+(2*weight_std_devation)
weight_thrice_std_devation_start,weight_thrice_std_devation_end = weight_mean-(3*weight_std_devation),weight_mean+(3*weight_std_devation)
print(height_median,weight_median,height_mode,weight_mode,height_median,weight_median,height_std_devation,weight_std_devation)

height_list_of_data_within_1_std_devation = [result for result in Height_list if result > height_first_std_devation_start and result < height_first_std_devation_end]
height_list_of_data_within_2_std_devation = [result for result in Height_list if result > height_second_std_devation_start and result < height_second_std_devation_end]
height_list_of_data_within_3_std_devation = [result for result in Height_list if result > height_third_std_devation_start and result < height_first_std_devation_end]

fig = ff.create_distplot([df["Height(Inches)"].tolist()],["H"],show_hist=False)
fig.show()
