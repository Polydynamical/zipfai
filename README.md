# zipfai
Zipfai is an attempt to prove Zipf's Law and implement it to generate text using AI. 


### Extra   
Add a return after every word: ```%s/ \w\+/\r\0/g```  
Remove all leading whitespace: ```%s/^\s\+//g```  
Add double quotes to all words: ```%s/\w\+/"\0",/g```  
