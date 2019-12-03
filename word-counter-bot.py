import praw
import prawcore
# from prawcore import exceptions
# import time
import os


def main():
    # reddit = praw.Reddit('livesh_bot_id')
    # Retrieve heroku env variables
    reddit = praw.Reddit(
                        client_id=os.environ["client_id"],
                        client_secret=os.environ["client_secret"],
                        user_agent='windows:word-counter-Bot(by /u/Liveshkumar)',
                        username=os.environ["username"],
                        password=os.environ["password"],
                        )
    if reddit.read_only:
        print('read only mode')
    else:
        print('logged in successfully')
    try:
        i = reddit.subreddit('all').stream.comments()
        i.__next__()    # iterate over the generator object i to catch OAuthException
    except prawcore.OAuthException:
        print('Incorrect login credentials.')
        exit()
    print('Running...')
    while reddit.inbox.stream():
        for message in reddit.inbox.unread():
            message_text = message.body
            print(message_text)
            # checks if someone has triggered the bot

            def matching(text_in_message):
                string = str(text_in_message).split()
                if 'u/word-counter-bot' == string[0].lower() or \
                   '/u/word-counter-bot' == string[0].lower() or \
                   'word-counter-bot' == string[0].lower():

                    try:
                        second_arg = string[1]
                        third_arg = string[2]
                    # IndexError will occur if someone triggered the bot with incorrect arguments

                    except IndexError:
                        print(f'replying to {message.author}')
                        print('bot output: inappropriate calling syntax\n')

                        message.reply(f'Hey! {message.author} it looks like you have called me incorrectly.\n'
                                      f'My format of calling is:\n\n<u/word-counter-bot>  <u/username>  <search_word>'
                                      f'\n\n**Beep boop I\'m a bot.**\n'
                                      f'**Contact my [creator](https://www.reddit.com/user/Liveshkumar)**')
                        message.mark_read()
                        return None

                    athr = message.author
                    return second_arg, third_arg, athr
                else:
                    # all non-triggering meassages are ignored
                    return None

            if matching(message_text) is None:
                continue
            argument_username, argument_search_text, author = matching(message_text)
            
            cmt_list = []
            i = 0
            bot_target = reddit.redditor(str(argument_username[2:]))
            try:
                for cmt in bot_target.comments.new(limit=None):
                    cmt_list.append(str(cmt.body))
                    i += 1

                count = 0
                for cmnt in cmt_list:
                    if str(argument_search_text) in cmnt.lower().split():
                        count += 1
                    else:
                        continue

                print(f'replying to {message.author}\n')
                print(f'I have searched {i} comments in {argument_username}\'s profile and'
                      f' have found that {str(argument_username)} has'
                      f' said \'{argument_search_text}\' {count} time(s)\n\n'
                      f'**Beep boop I\'m a bot.**\n'
                      f'**Contact my [creator](https://www.reddit.com/user/Liveshkumar)**')

                message.reply(f'I have searched {i} comments in {argument_username}\'s profile and'
                              f' have found that {str(argument_username)} has'
                              f' said \'{argument_search_text}\' {count} time(s)\n\n'
                              f'**Beep boop I\'m a bot.**\n'
                              f'**Contact my [creator](https://www.reddit.com/user/Liveshkumar)**')
                message.mark_read()

            except prawcore.exceptions.NotFound:
                print(f'replying to {message.author}\n')
                print(f'Thanks for calling me {message.author} , but the user '
                      f'{argument_username} does not exist.'
                      f'\n\n**Beep boop I\'m a bot.**\n'
                      f'**Contact my [creator](https://www.reddit.com/user/Liveshkumar)**')

                message.reply(f'Thanks for calling me {message.author} , but the user '
                              f'{argument_username} does not exist.'
                              f'\n\n**Beep boop I\'m a bot.**\n'
                              f'**Contact my [creator](https://www.reddit.com/user/Liveshkumar)**')
                message.mark_read()


if __name__ == '__main__':
    main()
