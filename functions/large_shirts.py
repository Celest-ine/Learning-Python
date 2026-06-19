def make_shirt(size='large', phrase='I love Python'):
    """Print a sentence summarizing the size of a t-shirt and a phrase printed on it."""

    print(f"Your T-shirt size is {size} with the phrase: '{phrase.title()}' printed on it.")

make_shirt()
make_shirt(size='medium')
make_shirt(size='small', phrase='good vibes only')