def show_messages(text_messages):
    """Print each text message in the list text_messages."""
    
    print("Here are your text messages:")
    for index, text_message in enumerate(text_messages, start=1): # Start indexing at 1
        print(f"{index}. {text_message}")

text_messages = ['nope', 'OMG!', 'Hello', 'Happy Birthday', 'LOL']
show_messages(text_messages)