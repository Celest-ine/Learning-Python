def send_messages(text_messages, sent_messages):
    """Print each message and move each message to a listas if printed."""
    copy_text_messages = text_messages[:]
    while copy_text_messages:
        current_message = copy_text_messages.pop(0)
        print(f"Printing message to send: {current_message}")
        sent_messages.append(current_message)

text_messages = ['nope', 'OMG!', 'Hello', 'Happy Birthday', 'LOL']
sent_messages = []
send_messages(text_messages, sent_messages)
print(text_messages)
print(sent_messages)