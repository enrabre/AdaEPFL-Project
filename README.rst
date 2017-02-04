
ADA's project
===============

Project proposal : Detecting events (date, location, positive or negative sentiment)


Abstract:
-----------------

Text mining and analysis are areas of research that made amazing results these last years. Linked to the advent of Twitter, a huge amount of data are waiting to be process and analyse. In our project, we will try to process, organise tweets in Switzerland in order to detect events. The end goal of our project is to be able to label event and maybe highlight causality between place, date,positive or negative sentiment. Our biggest challenge will be 

Data description:
-----------------

The format of already collected tweets could be json or already extracted fields, for example, in csv format.
In case collected data has json format what we expect to get is next: 

		210 000  - approximate number of Twitter users in Swiss (2010)

		2012-2016 - 5*365 - approximate days of use 1825

		In case of JSON tweets format we expect to get in worst case 12-13k of symbols (see example response
		https://dev.twitter.com/rest/reference/get/search/tweets) i.e. 11KB

		Representing roughly, people do 1 tweet daily => 210000*1825*11 = 4 215 750 MB

Of course not all people who have an account are active Twitter users. So size of 4 215, 75 TB
could be exaggerated significantly. 

All useful information we can get by means of entities  - data from tweets including resolved URLs, media, hashtags and mentions. Entities are included in all Tweet Objects, located under the entities attribute. The details of entities are available here: media, urls, user_mentions, hashtags, symbols, extended_entities.
Also it worth to enumerate some useful fields available: 
contributors - official tweet authors
coordinates - the geographic location of a Tweet as reported by the user or client application. The inner coordinates array is formatted as geoJSON.
created_at - UTC time when a Tweet was created
favorite_count - times a Tweet has been liked
lang, place, retweet_count, text - tweet’s actual text
etc.
		
Feasibility and Risks: 
-----------------

Feasibilities:
~~~~~~~~~~~~~~~~~~~~~~

Tweets are popular and well known, therefore it should be easy to find help about how to deal with them. Our dataset should be quite clean, as it comes from an API. For data processing and analyzing, we will use API’s installed in the cluster.


Risks:
~~~~~~~~~~~~~~~~~~~~~~

However, this project has also high risks. Detecting event is not a straightforward task, so the challenge will be to provide an efficient classifier to distinguish real events from non-event ‘space’, in other words - ability to detect events from the data. We are still not sure which methods will work with our dataset. 
The dataset could be another issue, as Switzerland is a small country and Twitter is not used by the whole population, we could lack data to do proper analysis. Switzerland is also a multilingual country (french, german, italian). Therefore it will be a challenge to make a classifier which take this into account.

Deliverables:
-----------------

The main objective is to develop a model able to detect the top events of Switzerland that happened during the period 2012-2016. These “top” events would be the ones where people in Switzerland twitted the most about. The model should return all the tweets related to the event.
 
We have many ideas about “secondary” goals, if the main one was to be achieved quickly. However, as this project comport a lot of risks, it will not be our main focus, unless we have enough time to do them. Here is a list of these secondary objectives:


The model could give more information about the events it detects. The information could be estimations about the location of an event, its date and its size. In a more advanced step, we could try to predict the people’s feeling about the event.
We could make a model able to detect smaller events with less tweets.
We could then build a model and train it with parts of the data and try to predict the rest of the data. We could then use this model to try to detect event in real time.
Finally, a visualization of Switzerland with an event detection in real time could be created.

Timeplan:
-----------------

6.11: Project proposal

20.11: First analysis of the data, first tests with the cluster 

1.12: First tests of different techniques to detect events 

15.12: Working model to detect events. Decision of how to continue: 
       In case of very bad results or no working model: Change of techniques 
       In case of satisfying results: decision between improving the model or starting the secondary objectives. 
       In case of very good model: start of the secondary objectives. 
       
10.01: Final model decided, visualization started. 

20.01: Project finished, starting presentation. 

~30.01: Presentation of the project during the Mini-Symposium





