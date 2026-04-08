# A dictionary that stores programming terms and their meanings.
glossary = {
    'variable': 'A named location in memory that can store a value.',
    'function': 'A block of code that performs a specific task and can be reused.',
    'loop': 'A control structure that allows you to repeat a block of code multiple times.',
    'list': 'A collection of items that can be ordered and changed.',
    'dictionary': 'A collection of key-value pairs that allows you to store and retrieve data effectively.',
}
for term in sorted(glossary):
    print(f'{term.title()}: {glossary[term]}\n')