ADA's project
===============
**Project proposal : Detecting events (date, location, positive or negative sentiment)**

	*Twitter is an online news and social networking service. 
	Users post and interact with messages, "tweets," restricted to 140
	characters. They are using Twitter to report real-life events. 
	It constructs a big base of data on events sometime located.*
**Goal**:

This model detects past events based on a database of 28 million of tweets. This data set was only composed of Swiss tweets.

Strategy:
-----------------

We teamed up with another group:

- we were in charge of the event detection 

- they created the visualisation based on our detection
We widely used time series analysis for our detection. For every hashtags, we looked for peaks in their time series and stated that an event occured this day if the peak was above a threshold. The threshold was computed using the avarage number of time a hashtag was used. A peak represented the number of tweets containing the specific hashtag.

.. image :: images/threshold.png
	:width: 10

The location of a detected event was placed at the median of the longitude and latitude of every tweets composing the peak.
Several different users should have posted about an event to avoid to detect events created by only one user.

This basic strategy supposed that an event could only last one day, however festival, election or celebration can go on several days. To catch this information, close events were merged. Two events were judged close if they occured in the same time window.

.. image :: images/window.png
	:width: 10

Finally, the model was improved by removing reccurent event with low frequency. Event like #weekend occures every week and are not real events while #christmas occures every year and should not be removed from the detected events.

Results:
-----------------
Our model detected 3156 different events.

German, Italian and French tweets were correctly located into the different parts of Switzerland.

Big events like sport games and local events like the white dinner in Basel were correctly detected. The model was, as well, able to detect smaller events, like conferences at the EPFL.

Here the link to the interactive map of the other team: https://symsystem.github.io/ADA_Project/

Please, find below screenshots of representative examples.

.. image :: images/swissMap.png
	    :width: 10 
	  
+-------------------------------+--------------------------------+
| .. image :: images/result.png |  .. image :: images/privacy.png|
|	    :width: 10          |           :width: 10           |
+-------------------------------+--------------------------------+
