import aminofix
import concurrent.futures

email = input("Email: ")
password = input("Password: ")
message = input("Message: ")
msgtype = input("MessageType: ")
client = aminofix.Client()
client.login(email=email, password=password)
clients = client.sub_clients(start=0, size=1000)
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")
communityid = clients.comId[int(input("Select the community: "))-1]
sub_client = aminofix.SubClient(comId=communityid, profile=client.profile)
chats = sub_client.get_chat_threads(size=150)
for z, title in enumerate(chats.title, 1):
	print(f"{z}.{title}")
chatx = chats.chatId[int(input("Select the chat: "))-1]

def threadpoolspam():
	while True:
		with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
			print("Spamming")
			_ = [executor.submit(sub_client.send_message, chatx, message, msgtype) for _ in range(5000000)]
			
def threadpoolboost():
	while True:
		with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
			_ = [executor.submit(threadpoolspam) for _ in range(5000000)]
			
threadpoolboost()