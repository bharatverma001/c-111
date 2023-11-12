 
mean_list = []
 for i in range(0,1000):
  set_of_means random_set_of_mean (100)
  mean_list.append(set_of_means)
  

 # calculating mean and standard deviation of the sampling distribution.
std_deviation statistics.stdev (mean_list)
mean statistics.mean (mean_list)
print("mean of sampling distribution:- ",mean)
print("Standard deviation of sampling distribution:- ", std_deviation)

mean of sampling distribution:- 6.1254
Standard deviation of sampling distribution: 0.32805008284842246
 # plotting the mean of the sampling
fig= ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace (go. Scatter (x= [mean, mean], y=[0, 0.20], mode="lines", name="MEAN")) 
fig.show()

