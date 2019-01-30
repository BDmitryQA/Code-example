WIN_GAME = 7
DROW_GAME = 1
LOST_GAME = 3
GOALS = 16
MISS = 14

class One(object):

    # Инициализация
    def __init__(self,win_game,draw_game,lost_game):
        self.win_game = win_game
        self.draw_game = draw_game
        self.lost_game = lost_game
        self.goals = 0
        self.miss = 0

    # Фиксация результатов матча
    def results(self, goals, miss):
        self.goals = goals
        self.miss = miss

    # Запись очков клуба
    def score(self):
        return self.win_game * 3 + self.draw_game * 1

    # Разница голов и промахов
    def difference(self):
        return self.goals - self.miss

class Two(One):
    # Сумма всех игр
    def total_game(self):
        return self.win_game + self.draw_game + self.lost_game

if __name__ == '__main__':
    statistic_game = One(WIN_GAME,DROW_GAME,LOST_GAME)
    statistic_game.results(GOALS,MISS)
    print("Очки заработанные клубом в этом сезоне : " + str(statistic_game.score()))
    print("Разница голов и промохов: " + str(statistic_game.difference()))
    total_games = Two(WIN_GAME,DROW_GAME,LOST_GAME)
    print("Всего сыграно игр: " + str(total_games.total_game()))