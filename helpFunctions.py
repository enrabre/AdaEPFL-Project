import re
import copy


def extract_hashtags(text):
    '''
    Extract all the hashtags of a text and return the words attached to the '#' sign in a list.
    If the text has no hashtag, return an empty list.
    :param text: A string text in which to find hashtags.
    :return: A list of String, all in lower characters, which are the words linked to the '#' sign.
    '''
    ht_list = re.findall(r"#(\w+)", text)
    # Sometimes ht_list returned a list of empty lists, the next line corrects that.
    non_empty_hts = list(filter((lambda ht: ht != []), ht_list))
    lower_char_list = [ht.lower() for ht in non_empty_hts]
    return lower_char_list


addedHashtagsRowsList = []
def multiplyHashtagRows(row, columns):
    '''
    Examine each row. If there are multiple hashtags, it will return the first one.
    (so the first one will replace the list of hashtags in the df). Then for all the next ones,
    it will make a copy of the row in the addedHashtagsRowsList, (in a dictionary format).
    So this dictionary can in the end be transformed in a DF and added to the original DF.
    (The speed is increased a lot by doing it this way!)
    '''
    htList = row.hashtag
    if len(htList) > 1:
        ## Making the dictionary
        addedHashtag = {}
        addedHashtag['createdAt'] = row.name #the df index
        for col in columns:
            addedHashtag[col] = row[col]
        ## Copying the dict for each hashtag
        i = 1
        while i < len(htList) :
            deepCopy = copy.deepcopy(addedHashtag)
            deepCopy['hashtag'] = htList[i]
            global addedHashtagsRowsList
            addedHashtagsRowsList.append(deepCopy)
            i+=1
    return htList[0] # return the first hashtag

def reset_added_hashtag_rows_list():
    global addedHashtagsRowsList
    addedHashtagsRowsList = []

def get_added_hashtag_rows_list():
    return addedHashtagsRowsList


def isSpecificEventListIllegal(detectedEventDateList, max_event_duration, min_duration_before_new_event):
    '''
    Return true if the list of dates contain illegal tupples of events, so if the event is recurrent
    which would mean it is not a real event.
    '''
    def datesAreIllegal(date1, date2, date3):
        '''
        Return true if the 3 dates are not to be considered as regular events.
        '''
        ## Return if the difference is too small to be considered as 2 different events
        def diffIsSmall(timeDiff):  
            return timeDiff < max_event_duration

        ## Return true if the difference is not big enough to be an annual event.
        def isDiffSuspect(timeDiff):
            return timeDiff < min_duration_before_new_event

        diff1 = abs(date1 - date2)
        diff2 = abs(date2 - date3)
        diff3 = abs(date3 - date1)

        ## The difference is too small, it must be the same event
        if diffIsSmall(diff1) or diffIsSmall(diff2) or diffIsSmall(diff3):
            return False

        ## If there are at least 2 out of 3 suspect difference, then the dates are illegal
        if isDiffSuspect(diff1):
            return isDiffSuspect(diff2) or isDiffSuspect(diff3)
        else:
            return isDiffSuspect(diff2) and isDiffSuspect(diff3)
    
    ## MAIN FUNCTION : ##
    # Go through the list of events and try all "triples" to see if there is any illegal triples. This is a quickly done
    # code to do that. Code complexity bellow is in O(k^3), with k being the size of the list. We will apply this function
    # to n list so we will have an overall complexity in O(n*k^3). We can consider however that each list will
    # be small so k can be considered as constant and therefore the overall complexity will be in O(n).
    for i in range(len(detectedEventDateList) - 2):
        for j in range(i, len(detectedEventDateList) - 1):
            for k in range(j, len(detectedEventDateList)):
                if datesAreIllegal(detectedEventDateList[i], detectedEventDateList[j], detectedEventDateList[k]):
                    return True
    return False
	
def mergeCloseEvents(rowsList):
    '''
    Take a list of dictionary, where each dictionary is a "row" of the event df, which contained detected events.
    It will process the list to detect event that are close and merge them together.
    Return : the processed list of event.
    '''
    
    def areCloseEvents(event1, event2):
        '''
        Return true is 2 events dates are defined as "close"
        '''
        return abs(event1['date'] - event2['date']) < MAX_DURATION_OF_EVENT
        
    def mergeCloseEventsSublist(closeEventList):
        '''
        This will be applied to each close event sublist. It will merge all events into one unique event.
        The event will consist of the total number of tweets, with the concatenation of the tweet texts and the mean
        of longitude/latitude. A meanDate will be defined as a ponderated mean between all dates.
        The final date will be the one that is in the closeEventList and is closest to this mean date.
        We did this to keep the meaning of the date if it had some, and not have some meaningless "mean-date".
        '''
        latitude = 0
        longitude = 0
        numberOfTweets = 0
        text = ""
        originalDate = closeEventList[0]['date']
        dateDiff = timedelta(days=0)
        first = True        
        for tweet in closeEventList:
            longitude += tweet['longitude']
            latitude += tweet['latitude'] 
            numberOfTweets += tweet['numberOfTweets']
            if first:
                text = tweet['text']
                first = False
            else:
                text += delimiter + tweet['text']
                dateDiff = dateDiff + (tweet['date'] - originalDate) * tweet['numberOfTweets']

        ## It is multiplied by 2 then soustracted to round correctly to the nearest day
        meanDate = originalDate + 2* dateDiff / numberOfTweets - dateDiff / numberOfTweets        
        latitude = latitude / len(closeEventList)
        longitude = longitude / len(closeEventList)
        
        ## We are going to detect the event the closest to the mean date
        minSelectedDate = closeEventList[0]['date']
        minDistance = abs(closeEventList[0]['date'] - meanDate)
        for tweet in closeEventList:
            if abs(tweet['date'] - meanDate) < minDistance:
                minSelectedDate = tweet['date']    
        
        return {'date': minSelectedDate, 'hashtag': closeEventList[0]['hashtag'], 'text': text,
                    'longitude': longitude, 'latitude':latitude, 'numberOfTweets': numberOfTweets, }
    
    ############ -----  MAIN METHOD  ----- ############
    
    ## If the list is big enough, go through the list and form an export list and merge elements that needs to.
    if len(rowsList) < 2:
        return rowsList
    else:
        firstLastPosOfItemsToMerge = []
        sortedRowsList = sorted(rowsList, key=itemgetter('date')) 
        exportedEventList = []
        ## This goes through the *sorted* list and add the pair of indices (first indice and last indice) where events 
        ## that should be merged appear.
        lastEventWasClose = False
        firstItem = -1
        for i in range(0, len(sortedRowsList)-1):
            if areCloseEvents(sortedRowsList[i], sortedRowsList[i+1]):
                if not lastEventWasClose: # So it is the first pairs of the sublist of close events in the whole list
                    firstItem = i
                    lastEventWasClose = True
            else:
                if lastEventWasClose: # So the list has just ended.
                    exportedEventList.append(mergeCloseEventsSublist(sortedRowsList[firstItem:i+1]))
                    lastEventWasClose = False
                else: # The element is by itself, let's append it
                    exportedEventList.append(sortedRowsList[i])  
        if lastEventWasClose: # If there were events to merge till the last elem of list
            exportedEventList.append(mergeCloseEventsSublist(sortedRowsList[firstItem:len(sortedRowsList)]))
        else:
            exportedEventList.append(sortedRowsList[len(sortedRowsList)-1])
    
    return exportedEventList
	
from datetime import datetime 	
import pandas as pd 
import numpy as np 
epoch_dt = datetime(1970, 1, 1) 
def to_utc(date):
    d_dt = datetime.combine(date, datetime.min.time())
    return int((d_dt - epoch_dt).total_seconds()*1000)
	
def convert_to_unix_time(record):
    datetime_index = pd.DatetimeIndex([datetime(record['year'], record['month'], 1)])
    unix_time_index = datetime_index.astype(np.int64) // 10**6
    return unix_time_index[0]