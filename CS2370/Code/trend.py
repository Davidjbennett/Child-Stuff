# plot3.py: Multiple plots on the same axis, uses a legend
import matplotlib.pyplot as plt

_,axis = plt.subplots()
xs = range(0,20)
ys = [174.0, 174.2, 174.1, 174.7, 174.2, 175.2, 176.2, 175.6, 176.2, 174.8, 
      174.4, 174.9, 175.7, 175.5, 175.7, 174.2, 173.8, 175.0, 173.9, 173.7]
# Labels go in the legend
axis.plot(xs,ys,label="orig")			

ys3 = [174.0, 174.1, 174.3, 174.3, 174.7, 175.2, 175.7, 176.0, 175.5, 175.1,
       174.7, 175.0, 175.4, 175.6, 175.1, 174.6, 174.3, 174.2, 174.2, 173.7 ]
# r = red, -- = dashed line
axis.plot(xs,ys3,'r--',label="trend3")

# Create and place legend
axis.legend(loc="best")					
plt.savefig("trend.pdf")
