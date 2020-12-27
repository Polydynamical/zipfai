# zipfai
Zipfai is an attempt to prove Zipf's Law and implement it to generate text using AI. 


### Navigaton
#### Data
Contains the words from various texts.  

#### Programs
Contains the programs available to run in analyzing the data.
    - Analyze.py returns the words in the data organized by frequency. Also returns ratio compared to most used word and number of occurences.
    - Graph.py graphs the data compared to their frequency.
  
#### Graphs  
##### Lin  
    - Contains the graphs from the current data in a linear graph.  
##### Log  
    - Contains the graphs from the current data in a logarithmic grpah.  
  
### Extra   
The following Regex command in vim will add a return after every word: ```%s/ \w\+/\r\0/g```  
The following Regex command in vim will remove all leading whitespace: ```%s/^\s\+//g```  
The following Regex command in vim will add double quotes to all words: ```%s/\w\+/"\0",/g```  
