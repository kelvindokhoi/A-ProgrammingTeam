    if val2 in cards:
        if not isinstance(cards[val2],set):
            if pos2!=cards[val2]:
                cards[val2]={cards[val2],pos2}
    else:
        cards[val2]=pos2