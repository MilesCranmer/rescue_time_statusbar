import rumps
from datetime import date, timedelta as td
from analyze import score_day
from time import sleep

class SomeApp(rumps.App):
    def __init__(self):
        super(SomeApp, self).__init__(type(self).__name__, menu=[])
        self.score = 0
        # rumps.debug_mode(True)

    @rumps.timer(10)
    def update_score(self, t):
        self.score = score_day(date.today())

    @rumps.timer(1)
    def refresh(self, t):
        self.title = f'Score={self.score:.1f}'

if __name__ == "__main__":
    SomeApp().run()
