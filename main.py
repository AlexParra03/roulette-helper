class Token:
    def __init__(self, number):
        if number == 0:
            self.color = 'G'
            self.number = 0
        else:
            if number >= 1 and number <= 10:
                self.color = 'B' if number % 2 == 0 else 'R'
                self.number = number
            elif number >= 11 and number <= 18:
                self.color = 'R' if number % 2 == 0 else 'B'
                self.number = number
            elif number >= 19 and number <= 28:
                self.color = 'B' if number % 2 == 0 else 'R'
                self.number = number
            elif number >= 29 and number <= 36:
                self.color = 'R' if number % 2 == 0 else 'B'
                self.number = number            

class Plays:
    def oneToTwelve(self, tokenList):
        counter = 0
        for token in tokenList:
            if token.number >= 1 and token.number <= 12:
                counter += 1
        return counter

    def thirteenToTwentyfour(self, tokenList):
        counter = 0
        for token in tokenList:
            if token.number >= 20 and token.number <= 24:
                counter += 1
        return counter

    def twentyfiveToThirtysix(self, tokenList):
        counter = 0
        for token in tokenList:
            if token.number >= 25 and token.number <= 36:
                counter += 1
        return counter

    def oneToEighteen(self, tokenList):
        counter = 0
        for token in tokenList:
            if token.number >= 1 and token.number <= 18:
                counter += 1
        return counter

    def nineteenToThirtysix(self, tokenList):
        counter = 0
        for token in tokenList:
            if token.number >= 19 and token.number <= 36:
                counter += 1
        return counter

    def red(self, tokenList):
        counter = 0
        for token in tokenList:
            if token.color == 'R':
                counter += 1
        return counter

    def black(self, tokenList):
        counter = 0
        for token in tokenList:
            if token.color == 'B':
                counter += 1
        return counter

    def even(self, tokenList):
        counter = 0
        for token in tokenList:
            if token.number % 2 == 0 and token.number != 0:
                counter += 1
        return counter

    def odd(self, tokenList):
        counter = 0
        for token in tokenList:
            if token.number % 2 != 0  and token.number != 0:
                counter += 1
        return counter

class Game:
    def __init__(self):
        self.tokenHistory = []
        self.plays = Plays()

    def play(self):
        print("=========================================================")
        red = self.plays.red(self.tokenHistory)
        black = self.plays.black(self.tokenHistory)
        if red > black:
            print('RED','%{:.2f}'.format(((red/len(self.tokenHistory))*100)), "50")
        elif red < black:
            print('BLACK','%{:.2f}'.format(((black/len(self.tokenHistory))*100)), "%50")

        even = self.plays.even(self.tokenHistory)
        odd = self.plays.odd(self.tokenHistory)
        if even > odd:
            print('EVEN','%{:.2f}'.format(((even/len(self.tokenHistory))*100)), "%50")
        elif even < odd:
            print('ODD','%{:.2f}'.format(((odd/len(self.tokenHistory))*100)), "%50")

        firstHalf = self.plays.oneToEighteen(self.tokenHistory)
        secondHalf = self.plays.nineteenToThirtysix(self.tokenHistory)
        if firstHalf > secondHalf:
            print('1-18','%{:.2f}'.format(((firstHalf/len(self.tokenHistory))*100)), "%50")
        elif firstHalf < secondHalf:
            print('19-36','%{:.2f}'.format(((secondHalf/len(self.tokenHistory))*100)), "%50")

        low = self.plays.oneToTwelve(self.tokenHistory)
        mid = self.plays.thirteenToTwentyfour(self.tokenHistory)
        hig = self.plays.twentyfiveToThirtysix(self.tokenHistory)

        if round(low/len(self.tokenHistory),2) > 33.33:
            print('1-12','%{:.2f}'.format(((low/len(self.tokenHistory))*100)), "%33.33")
        if round(mid/len(self.tokenHistory),2) > 33.33:
            print('13-24','%{:.2f}'.format(((mid/len(self.tokenHistory))*100)), "%33.33")
        if round(hig/len(self.tokenHistory),2) > 33.33:
            print('25-36','%{:.2f}'.format(((hig/len(self.tokenHistory))*100)), "%33.33")

    def start(self):
        while True:
            x = 0
            while True:
                errOcurred = False
                x = input()
                if x == 'q':
                    return
                try:
                   x = int(x)
                except ValueError:
                    errOcurred = True
                    print("That's not an number!")
                if not errOcurred:
                    break
            self.tokenHistory.append(Token(int(x)))
            self.play()

game = Game()
game.start()
