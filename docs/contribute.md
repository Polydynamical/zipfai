# Contribute
All pull requests are welcome and should be reviewed within 72 hours. More data is essential to this project. Here are some helpful regex commands.

### Regex Commands
- Add a return after every word: ```%s/ \w\+/\r\0/g```  
- Remove all leading whitespace: ```%s/^\s\+//g```  
- Add double quotes to all words: ```%s/\w\+/"\0",/g```  
- Make all words uppercase: ```%s/\w\+/\U\0/g```  

