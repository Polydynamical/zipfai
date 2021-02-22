# Contribute
All pull requests are welcome and should be reviewed within 72 hours. More data is essential to this project.

### Helpful Vim Regex Commands
- Add a return after every word: ```%s/ \w\+/\r\0/g```  
- Remove all leading whitespace: ```%s/^\s\+//g```  
- Add double quotes to all words: ```%s/\w\+/"\0",/g```  
- Make all words uppercase: ```%s/\w\+/\U\0/g```  
- Remove all occurences of ```\```: ```%s/\\\+//g```  
- Replace ```",'"``` with ```'```: ```%s/",'"\+/'/g```
- Replace ```Â€"``` with a space ```%s/Â€?\+//c```  
- Replace ```+``` with a space ```%s/+\+/ /g```
- Replace ```Ã©``` (é) with ```E``` ```%s/Ã©\+/E/g```
- Remove all occurences of ```*```: ```%s/*\+//g```
- Replace ```Ä«``` (ī) with ```i```: ```%s/Ä«\+//g```
- Remove all double quotes: ```%s/"\+//g```
- Replace all single quotes preceded by a space with a space: ```%s/ '\+/ /g```
- Replace all single quotes at the end of a line: ```%s/'\r\+//g```
- Remove all non-ASCII characters: ```%s/[^\x00-\x7F]\+//g```  
- Remove all characters except letters: ```%s/[^A-Za-z ]\+//g```
- Remove all nonwords: ```%s/(?!\p{L}+(?!\S))\S+//g```
