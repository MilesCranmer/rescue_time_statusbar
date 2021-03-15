import rumps
from datetime import date, timedelta as td
from analyze import score_day, writing_time
from download import save_data
from time import sleep
import numpy as np

class RescueTime(rumps.App):
    def __init__(self):
        super(RescueTime, self).__init__(type(self).__name__, menu=['Week'])
        self.score = 0
        self.writing_time = 0
        rumps.debug_mode(True)

    @rumps.timer(60)
    def update_score(self, t):
        save_data(date.today())
        self.score = score_day(date.today())
        self.writing_time = int(writing_time(date.today()))

    @rumps.timer(2)
    def refresh(self, t):
        self.title = f'writing={self.writing_time:d}, score={self.score:.1f}'

    @rumps.clicked("Week")
    def week(self, sender):
        scores = np.array(
	    [score_day(date.today()-td(days=i)) for i in range(7, -1, -1)]
	)
        rumps.Window(str(scores)).run()

if __name__ == "__main__":
    RescueTime().run()
