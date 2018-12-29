class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck = sorted(deck, reverse=True)
        new_deck = []
        for i in deck:
            if not new_deck:
                new_deck.append(i)
            else:
                last = new_deck.pop()
                new_deck.insert(0,last)
                new_deck.insert(0,i)

        return new_deck

solu = Solution()
print solu.deckRevealedIncreasing([17,13,11,2,3,5,7])