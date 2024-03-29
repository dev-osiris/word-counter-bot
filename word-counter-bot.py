#! python3
import praw
import prawcore
import os


# checks if someone has triggered the bot
def match(text_in_message, message):
    string = str(text_in_message).split()
    if 'u/word-count-bot' == string[0].lower() or \
       '/u/word-count-bot' == string[0].lower():
        try:
            if len(string) >= 4:    # if user provides incorrect number of arguments
                raise IndexError

            else:
                second_arg = string[1]
                third_arg = string[2]

        # IndexError will occur if someone triggered the bot with
        # incorrect number of arguments
        except IndexError as err:
            print(f'replying to {message.author}')
            print(f'bot output: Inappropriate calling syntax\n'
                  f'error : {err} \n')

            message.reply(
                  f'Hey! {message.author} it looks like you have called me incorrectly.\n'
                  f'My format of calling is:\n\n<u/word-count-bot>  <u/username>  <search_word>\n\n'                
                  f'I works only for words not [sentences](https://www.reddit.com/user/Leetcoder20/'
                  f'comments/e7r530/what_counts_as_a_sentence/?utm_source=share&utm_medium=web2x).'
                  f'\n\n**Beep boop I\'m a bot.**\n'
                  f'**Contact my [creator](https://www.reddit.com/user/Leetcoder20)**')
            message.mark_read()
            return None

        athr = message.author
        return second_arg, third_arg, athr
    else:
        # all non-triggering meassages are ignored
        return None


def login():
    # create a reddit instance
    reddit = praw.Reddit(
                        client_id=os.environ["client_id"],
                        client_secret=os.environ["client_secret"],
                        user_agent='windows:word-counter-Bot(by /u/Leetcoder20)',
                        username=os.environ["username"],
                        password=os.environ["password"],
                        )

    if reddit.read_only:
        print('Bot is in read only mode')
        exit()
    else:
        print('logged in successfully')

    try:
        i = reddit.subreddit('all').stream.comments()
        i.__next__()  # iterate over the generator object i to catch OAuthException
    except prawcore.OAuthException as err:
        print('Incorrect login credentials.\n'
              f'error: {err}')
        exit()
    except prawcore.exceptions.RequestException as err:
        print('Unable to establish a connection, terminating...\n'
              f'error : {err}')
        exit()

    return reddit


def main():
    reddit = login()
    print('Running...')
    while reddit.inbox.stream():
        for message in reddit.inbox.unread():
            message_text = message.body

            if match(message_text, message) is None:
                continue
            else:
                argument_username, argument_search_text, author = match(message_text, message)

            comment_list = []
            i = 0   # sentinel value
            try:
                bot_target = reddit.redditor(str(argument_username[2:]))
                for comments in bot_target.comments.new(limit=None):
                    comment_list.append(str(comments.body))
                    i += 1

                count = 0   # counts the occurances of searched word
                for comment in comment_list:
                    if str(argument_search_text).lower() in comment.lower().split():
                        count += 1
                    else:
                        continue

                print(f'replying to {message.author} :\n')
                print(f'I have searched {i} comments in {argument_username}\'s profile and'
                      f' have found that {argument_username} has'
                      f' said \' {argument_search_text} \' {count} time(s)\n\n'
                      f'**Beep boop I\'m a bot.**\n'
                      f'**Contact my [creator](https://www.reddit.com/user/Leetcoder20)**')

                message.reply(
                      f'I have searched {i} comments in {argument_username}\'s profile and'
                      f' have found that {str(argument_username)} has'
                      f' said \' {argument_search_text} \' {count} time(s)\n\n'
                      f'**Beep boop I\'m a bot.**\n'
                      f'**Contact my [creator](https://www.reddit.com/user/Leetcoder20)**')
                message.mark_read()

            except (prawcore.exceptions.NotFound, TypeError):
                print(f'replying to {message.author} :\n')
                print(f'Thanks for calling me {message.author} , but it looks '
                      f'like the user {argument_username} doesn\'t exist.'
                      f'\n\n**Beep boop I\'m a bot.**\n'
                      f'**Contact my [creator](https://www.reddit.com/user/Leetcoder20)**')

                message.reply(
                      f'Thanks for calling me {message.author} , but it looks '
                      f'like the user {argument_username} doesn\'t exist.'
                      f'\n\n**Beep boop I\'m a bot.**\n'
                      f'**Contact my [creator](https://www.reddit.com/user/Leetcoder20)**')
                message.mark_read()


if __name__ == '__main__':
    main()
