## The Problem
- I need to clean and preprocess the dataset. 
- I wanted to investigate whether NASA's event tracking data can be used in ML to discover hidden geographic patterns and predict whether a natural disaster will be high or low severity? This matters because early severity prediction can help emergency responders allocate resources more effectively and minimize damage.

## The Solution
*Preprocessing*
Firstly, I cleaned the dataset by dropping unnecessary columns (event_id, closed, title...) and changed the format of the time column. Then I extracted information I need to a new column (location). I also performed label encoding and one-hot encoding. Lastly, I filled NaN with median values of each column. 

*Visuals Analysis*
I created 3 meaningful visuals that gave me some insights about the dataset:
- Pie chart: Firstly, this pie chart shows that 92.3% of the natural disaster events in this dataset are wildfires. This extreme class imbalance creates a problem for me while deciding which ML model I should use. I can not treat this as a binary problem, because there are other values to consider. At the same time, other samples’ sizes are too small to train and test. I think that if I simply let a model learn from raw counts, it would predict Wildfire for everything and achieve 92% accuracy while being completely useless for predicting the other three types. 

- Bar chart: The second chart shows the average magnitude value grouped by unit. Acres, which measures wildfire size, has an average close to 3000 acres. Knots for storm wind speed. Nautical miles squared for sea ice extent is very small on this scale. An important insight here is that these three units are completely incomparable. We cannot say a wildfire of 3000 acres is bigger or smaller than a storm of 65 knots, they measure entirely different physical phenomena. This is why in my preprocessing step, I normalized magnitude within each unit group separately rather than change all to one unity.

- This visual directly motivated my choice to use K-Means clustering as one of my machine learning models for this project. Since different types of events cluster in completely different geographic regions, I expected the latitude and longitude features to show strong predictive signals. I noticed volcanoes event occurred spread out globally, unlike wildfires event that mostly based in the US. 

*ML Models*
I created 3 ML Models: K-Means Clustering, XG-Boost Classifier.
- K-Means Clustering: The first image shows many events plotted by latitude and longitude, with the cluster label annotated on each point. We can see from the image that the data separates into distinct geographic zones, a dense cluster of points near the origin representing US-based wildfires, and smaller scattered groups representing storms and other event types. 

Both distortion and inertias curves presented that K = 2, which indicates that splitting the data into two clusters significantly improves how tightly the data points are grouped. I think this ouput make sense because one cluster showing US-based Wildfires event(more geographically dense), and the other is non-wildfire evnts distributed globally. 

- XG-Boost Classifier: I used XGBoost to predict event severity, specifically, whether a natural disaster is high severity or low severity, based on features like location, category, and time. To create the target variable, I split the magnitude values at the median. Events above the median were labeled as high severity(1), and those below were labeled as low severity(0). This gave me a perfectly balanced dataset, which helps avoid bias in the model. Overall, the model achieves about 63% accuracy. 

This accuracy score may seem relatively low, but it's reasonable to me. Predicting severity is a difficult task because different types of events can have overlapping magnitude values, for example, a wildfire and a storm might have similar intensity but represent very different real-world situations.
