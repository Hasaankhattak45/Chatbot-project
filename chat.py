from chatterbot import ChatBot
#pip install spacychatbot = ChatBot('My_Bot')



def main():
	chatbot= ChatBot("charli")
	while True:
		msg = input('You: ')
		if msg.strip() != 'Bye':
			result = chatbot.get_response(msg)                        
			reply = str(result)
			print(reply)
		if msg.strip() == 'Bye':
			print('Bye')
			break

if __name__ == '__main__':
	main()