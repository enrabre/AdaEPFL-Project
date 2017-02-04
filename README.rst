
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

- we were in charge of the event detect 

- they created the visualisation based on our detection
We based our detection on time series analysis. For every hashtags, we looked for peaks in their time series and stated that an event occured this day if the peak was above the threshold. A peak represented the number of tweets caontaining the specific hashtag.

.. image :: threshold.png
	:width: 10

The location of a detected event was computed using the median of the longitude and latitude of every tweets composing the peak.
Several different users should have posted about an event to avoid to detect event created by only one user.
This basic strategy supposed that an event could only last one day, however festival, election or celebration can go on several days. To catch this information, close events were merged. Two events were judged close if they occured in the same time window.

.. image :: window.png
	:width: 10

Finally, the model was improved by removing reccurent event with low frequency. Event like #weekend accures every week and are not real event while #christmas occures every years and should not be removed from the detected events.

Results:
-----------------
Our model detected ... different events.

German, Italian and French tweets were correctly located into the different part of Switzerland.

Big events like sport games and local events like the white dinner in Basel were correctly detected. The model was, as well, able to detect smaller events, like conferences at the EPFL.
Here the link to the interactive map of the other team: Symeon del Marmol: https://symsystem.github.io/ADA_Project/
PLease, find below screenshots of representative example.

.. image :: swissMap.png
	    :width: 10 
	  
+------------------------+-------------------------+
| .. image :: result.png |  .. image :: privacy.png|
|	    :width: 10   |           :width: 10    |
+------------------------+-------------------------+
