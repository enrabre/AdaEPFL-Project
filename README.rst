Event detection on a Twitter dataset
===============
**Final visualization**: https://symsystem.github.io/ADA_Project/ (select "Events map" on the menu)

**Project proposal : Detecting events (related tweets, date and location)**

	*Twitter is an online news and social networking service. 
	Users post and interact with messages, "tweets", restricted to 140
	characters. They are using Twitter to report various things, including real-life events. 
	This constructs a big base of data, that will be used in our case to detect events.*
**Goal**:

The model that was developped detects past events on a dataset of 28 million tweets, which are dated from 2010 to 2016 and localized in Switzerland.

**Team**: Daniel Guggenheim, Sabrine Boumelala and Sergii Shynkaruk. (All Master students at EPFL)

Strategy:
-----------------

First, it is important to know that we teamed up with another group:

- We were in charge of the event detection.

- They created the visualisation based on our detection.


The goal of our team was to generate a JSON file containing detected events, which was used by the other team to make a visualization.

The event detection was based on hashtag analysis. Every hashtag was modeled as a time series that was discretized by day. The model tried to detect events by looking at peaks in these different time series. To do so, a threshold was defined, and it was stated that an event occurred on a defined day if the number of tweet with a specific hashtag happening on this day was above the threshold.

.. image :: images/threshold.png
	:width: 10

The location of a detected event was computed using the median of the longitude and the median of the latitude of all the tweets composing the peak.

Several other conditions were stated to define a "peak" as an event. For example, for an anomaly to be classified as a real event, at least a few different users should have tweeted about it. A basic strategy supposed that an event could only last one day, however festival, elections or celebrations can go on for several days. Therefore, close events were merged together. Two or more events were judged as "close" if they occurred in the same "time window" (as you can see on the figure below).

.. image :: images/window.png
	:width: 10

Finally, the model was improved by removing recurrent events with low frequency. Events like #weekend happen every week and are not "real" event while #christmas, which occurs every year, could be considered as a "real" event and therefore should not be removed from the detected events.

Results:
-----------------
Our model detected 3156 different events.

German, Italian and French tweets were correctly located into the different parts of Switzerland. Big events like sport games (football match, tennis match, etc.) and local events (like the "White Dinner" in Basel) were correctly detected. The model was also able to detect smaller events, like some conferences at the EPFL.

Here the link to the interactive map of the team we collaborated with: https://symsystem.github.io/ADA_Project/ .
|We thank Inês Valentim, Syméon del Marmol and Pierre Colombo for their amazing work on the vizualisation. Here is the link to their github repository: https://github.com/Symsystem/ADA_Project

Please, find below screenshots of a few examples.

.. image :: images/swissMap.png
	    :width: 10 
	  
+-------------------------------+--------------------------------+
| .. image :: images/result.png |  .. image :: images/privacy.png|
|	    :width: 10          |           :width: 10           |
+-------------------------------+--------------------------------+
