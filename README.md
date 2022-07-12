# word-counter-bot
A reddit bot that counts the number of occurances of a specific word entered by any user by scanning their comment history.

call the bot with the following format in comments of any reddit post: 

    <u/word-counter-bot>  <u/username>  <search_word>
    
example:

    u/word-counter-bot u/liveshkumar apple
    
The above will return the number of times user u/liveshkumar has used the word "apple" in their last 1000 comments.


The bot uses reddit's PRAW API to access user details.
