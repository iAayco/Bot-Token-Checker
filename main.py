#just @Aayco On Telegram
#When All World Left You, I Will Be Here For You
try:
    #Check That Telebot Module Was Installed
    import telebot
except ImportError:
    #If Not Installed
    print('Telebot Module Not Install It By `pip install telebot`')
#The File That Contains Tokens
tokens = 'tokens.txt'
#Open The File And Read His Content
with open(tokens, 'r') as tokens:
    #Get Every Token In File One By One
    for token in tokens:
        #Clear Unused Spaces
        token = token.strip()
        #Print The Token We Will Test
        print(f'Testing Token: {token}')
        try:
            #Trying To Login To Telegram Via Token
            bot = telebot.TeleBot(token)
            #Get The Bot Username
            username = bot.get_me().username
            #If We Get the Username Successfully
            if username:
                #Print The Token And Bot Username
                print(f'TOKEN: {token} BOT: {username}')
                #Save Vaild Tokens With Bots Usernames To File
                with open('vaild_tokens.txt', 'a') as good:
                    good.write(f'TOKEN: {token} BOT: {username}')
            else:
                #Print The Invaild Tokens (No Need To Save Them But If You Want You Can Add It)
                print(f'TOKEN: {token} Is Invaild')
            #Error Handling
        except Exception as e:
            #Print The Error
            print(e)
