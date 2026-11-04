from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        D = deque()
        R = deque()

        for i in range(len(senate)):
            ch = senate[i]

            if ch == 'R':
                R.append(i)
            else:
                D.append(i)

        while D and R:
            dTurn = D.popleft()
            rTurn = R.popleft()

            if dTurn < rTurn:
                D.append(dTurn + len(senate))
            else:
                R.append(rTurn + len(senate))

        if R:
            return "Radiant"
        else:
            return "Dire"
        
