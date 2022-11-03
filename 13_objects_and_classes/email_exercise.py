class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
command = input()
while command != "Stop":
    command_list = command.split(" ")
    sender = command_list[0]
    receiver = command_list[1]
    content = command_list[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    command = input()
sent_emails = list(map(lambda x: int(x), input().split(", ")))
for x in sent_emails:
    emails[x].send()
for each in emails:
    print(each.get_info())
