# word-counter-bot
A reddit bot that counts the number of occurances of a specific word entered by any user by scanning their comment history. It is made in python using reddit's **PRAW API** and hosted on **Heroku** platform.

call the bot with the following format in comments of any reddit post: 

    <u/word-counter-bot>  <u/username>  <search_word>
    
example:

    u/word-counter-bot u/liveshkumar apple
    
The above will return the number of times user u/liveshkumar has used the word "apple" in their last 1000 comments.


The bot uses reddit's PRAW API to access user details.

**Screenshots**


![bot_ss](https://user-images.githubusercontent.com/57588397/178424329-63fd4eb1-1797-4d37-88c4-4353a606d9db.PNG)

when username entered is incorrect:

![WhatsApp Image 2022-07-12 at 12 01 24 PM](https://user-images.githubusercontent.com/57588397/178424574-483aff61-de2b-4bc4-9c96-2b2b66bc9109.jpeg)
