from datetime import datetime


class Greeter:

    def __init__(self):
        self._day = self._get_current_day()
        self._part_of_day = self._get_part_of_day()

    def _get_current_day(self):
        return datetime.now().strftime('%A')

    def _get_part_of_day(self):
        hour = datetime.now().hour

        if 6 <= hour < 12:
            return "Morning"
        elif 17 > hour >= 12:
            return "Afternoon"
        else:
            return "Evening"

    def greet(self, store):
        print(f"Hi, welcome to {store}")
        print(f'How\'s your {self._day} {self._part_of_day} going?')
        print('Here\'s a coupon for 20% off!')


g = Greeter()
g.greet("The Best Store Ever")