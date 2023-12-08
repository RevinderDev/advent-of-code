from enum import IntEnum
from collections import defaultdict
from functools import total_ordering


class CardRank(IntEnum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6


CARDS_TYPE = "J23456789TQKA"
CARD_RANK = {card: CARDS_TYPE.index(card) for card in CARDS_TYPE}


@total_ordering
class Hand:
    def __init__(self, cards: str, bid: str):
        self.cards = cards
        self.bid: int = int(bid)
        self.rank: CardRank = self.__determine_rank()
        self.card_strength = [CARD_RANK[card] for card in self.cards]

    def __determine_rank(self) -> CardRank:
        counter = defaultdict(int)
        for card in self.cards:
            counter[card] += 1
        values = sorted(counter.values(), reverse=True)
        length = len(values)
        if length == 1:
            card_rank = CardRank.FIVE_OF_A_KIND
        if length == 2 and values[0] == 4:
            card_rank = CardRank.FOUR_OF_A_KIND
        if length == 2 and values[0] == 3:
            card_rank = CardRank.FULL_HOUSE
        if length == 3 and values[0] == 3:
            card_rank = CardRank.THREE_OF_A_KIND
        if length == 3 and values[0] == 2 and values[1] == 2:
            card_rank = CardRank.TWO_PAIR
        if length == 4:
            card_rank = CardRank.ONE_PAIR
        if length == 5:
            card_rank = CardRank.HIGH_CARD
        if "J" in cards and card_rank != CardRank.FIVE_OF_A_KIND:
            if card_rank in (CardRank.FULL_HOUSE, CardRank.FOUR_OF_A_KIND):
                return CardRank.FIVE_OF_A_KIND
            if card_rank == CardRank.THREE_OF_A_KIND:
                return CardRank.FOUR_OF_A_KIND
            if card_rank == CardRank.TWO_PAIR and counter["J"] == 2:
                return CardRank.FOUR_OF_A_KIND
            if card_rank == CardRank.TWO_PAIR and counter["J"] == 1:
                return CardRank.FULL_HOUSE
            if card_rank == CardRank.ONE_PAIR:
                return CardRank.THREE_OF_A_KIND
            return CardRank.ONE_PAIR
        return card_rank

    def __repr__(self) -> str:
        return f"<{self.rank.name}> {self.cards=}"

    def __lt__(self, other):
        return self.card_strength > other.card_strength

    def __eq__(self, other):
        return self.card_strength == other.card_strength


players = open("input.txt").read().splitlines()

hands = []
for player in players:
    cards, bid = player.split(" ")
    hands.append(Hand(cards, bid))

t = defaultdict(list)
for hand in hands:
    t[hand.rank].append(hand)

for type_ in t.keys():
    hands = t[type_]
    t[type_] = sorted(hands)

hands_sorted = []

for hand_type in sorted(t.keys(), reverse=True):
    hands_sorted.extend(t[hand_type])

answer = 0
for rank, hand in zip(range(len(hands_sorted), 0, -1), hands_sorted):
    answer += rank * hand.bid
    print(f"{hand=} {rank=} * {hand.bid} += {answer}")
print(answer)

# hands = sorted(hands, key=lambda x: x.rank, reverse=True)
# print(hands)
