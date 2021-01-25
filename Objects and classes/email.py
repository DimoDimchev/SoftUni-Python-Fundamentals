class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        print(f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}")


command = input()
emails = []

while command != "Stop":
    tokens = command.split()
    sender = tokens[0]
    receiver = tokens[1]
    content = tokens[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    command = input()

sent_emails = list(map(lambda x: int(x), input().split(", ")))

for x in sent_emails:
    emails[x].send()

for email in emails:
    email.get_info()