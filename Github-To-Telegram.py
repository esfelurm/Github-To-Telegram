# Bot Github-To-Telegram

admin_id = 'Admin numeric ID'
telegram_bot_token = "Token Bot"
telegram_channel_id = "ID Channel (ex : @esfelurm)"
Id_bot = "Username Bot : (ex : @esfelurm_bot)"







import os

try:
	import requests
except:
	os.system("pip install requests")
try:
	import telebot
except:
	os.system("pip install telebot")
try:
	import markdown
except:
	os.system("pip install markdown")

def read_github_readme(Url):
    url = Url.replace('github.com','raw.githubusercontent.com')+'/master/README.md'
    response = requests.get(url)
    readme_content = response.text
    html_content = markdown.markdown(readme_content)
    return html_content

try:
    with open("Links.txt", 'r') as file:
        existing_links = file.read().splitlines()
except FileNotFoundError:
    pass

def translate_text(text):
    url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=fa&dt=t&q={text}"
    response = requests.get(url)
    translation = response.json()[0][0][0]
    return translation

bot = telebot.TeleBot(telegram_bot_token)

bot.send_message(chat_id=admin_id,text="<b>Hello my friend!\nThis robot is for you to be able to publish people's projects in your own channel\nHow to work: \nIn order to publish projects related to a topic in your channel, you must use the following command :\n/change [name topic] [number] [OK/NO] [OK/NO] \n<i>The first parameter is the TOPIC name The second parameter is the number of projects you want to send The third parameter is for whether you want the readme.md file of the repositories to be sent or not The last parameter is the same as the third parameter, with the difference that it sends the source code of the project instead of the readme.md file \n\nExample : /change DDOS 10 OK OK</i></b>",parse_mode="HTML")

@bot.message_handler(commands=['change'])
def handle_change(message):
    existing_links = []
    if str(message.from_user.id) == admin_id:
        txt = message.text.split(' ')
        topic = txt[1]
        number = txt[2]
        Re = txt[3]
        Zp = txt[4]        	     	
        bot.reply_to(message, f'The topic was changed to {topic} !')
        bot.send_message(chat_id=admin_id,text=f'<b>Topic names: {topic}\nNumber of submissions: {number}\nSend File Readme.md : {Re}\nSend Source Code File : {Zp}</b>\n༼🆔 Channel: {telegram_channel_id}༽\n༼🆔 Bot: {Id_bot}༽',parse_mode="HTML")
        github_api_url = f"https://api.github.com/search/repositories?q=topic:{topic}"
        repositories = []
        response = requests.get(github_api_url)
        data = response.json()
        repositories.extend(data.get("items", []))    
        for i in range(0,int(number)):
        	for repo in repositories:
        	     try:
        	         existing_links = []
        	         with open("Links.txt", 'r') as file:
        	         	existing_links = file.read().splitlines()
        	     except FileNotFoundError:
                 	pass
        	     if repo['html_url'] in existing_links:
        	         continue
        	     else:
        	     	pass
        	     try:
        	     	translated_text = translate_text(repo.get('description', ''))      	     	
        	     	topics_with_hashtags = ' '.join(['#' + topic for topic in repo.get('topics', [])])
        	     	bot.send_message(chat_id=telegram_channel_id,text='<b>+++++ New repository! +++++</b>',parse_mode="HTML")
        	     	message = f"<b>🟢 Repository Name: {repo['name']}\n\n🟢 Description: <u>{repo.get('description', '')}</u>\n\n🟢 توضیحات: <u>{translated_text}</u>\n\n🟡 Topics: {topics_with_hashtags}\n\n🟡 Language: {repo.get('language', 'N/A')}\n\n🔵 URL: </b> {repo['html_url']}\n\n<b>🔵 writer: #{repo.get('owner', {}).get('login', 'N/A')}\n\n⚪️ Forks: {repo.get('forks', 0)}\n\n⚪️ Date of Release: {repo.get('pushed_at', 'N/A').replace('T', ' | Time : ').replace('Z','')}</b>\n\n\n༼🆔 Channel: {telegram_channel_id}༽\n༼🆔 Bot: {Id_bot}༽"
        	     	try:
        	     		try:
        	     		    im = open('photo.png', 'rb')
        	     		    bot.send_photo(chat_id=telegram_channel_id, caption=message, photo="https://browser.agenty.com/try?api=/api/screenshot&options={%22url%22:%22"+repo['html_url']+"%22,%22device%22:%22desktop%22,%22options%22:{%22type%22:%22png%22,%22fullPage%22:true}}", parse_mode="HTML")
        	     		except:
        	     			bot.send_photo(chat_id=telegram_channel_id, caption=message, photo=f"https://mini.site-shot.com/x/codebazan.ir-Web-screenshot/600/png/?{repo['html_url']}", parse_mode="HTML")
        	     	except:
        	     		bot.send_message(chat_id=telegram_channel_id, text=message, parse_mode="HTML")
        	     	if Re == 'OK':
        	     	    Read = read_github_readme(repo['html_url'])
        	     	    if len(Read) > 2501:
        	     	     f = open('README.html', 'w')
        	     	     f.write(Read)
        	     	     f.close()
        	     	     with open('README.html','rb') as r:
        	     	     	bot.send_document(telegram_channel_id,r)
        	     	    else:
        	     		    bot.send_message(telegram_channel_id,Read)
        	     	else:
        	     		pass
        	     	if Zp == 'OK':
        	     		url = f"{repo['html_url']}/archive/refs/heads/master.zip"
        	     		u = requests.get(url)
        	     		with open('source-code.zip','wb') as q:
        	     			q.write(u.content)
        	     		q.close()
        	     		with open('source-code.zip','rb') as s:
        	     		    bot.send_document(telegram_channel_id,s)
        	     	else:
        	     		pass
        	     	bot.send_message(chat_id=telegram_channel_id,text="<b>****** End Repository! ******</b>",parse_mode="HTML")
        	     	with open("Links.txt", "a+") as f:
        	     		f.write("\n")
        	     		f.write(repo['html_url'])
        	     except Exception as e:
        	     	print(f"An error occurred: {e}")
        		
    else:
        bot.reply_to(message, 'You are not allowed to do this!  ')

bot.polling()