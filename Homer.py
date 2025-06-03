import time
import random

eight_hours = 8 * 60 * 60  # 8 hours in seconds

class NuclearMeltdownException(Exception):
    pass

class MissingDonutException(Exception):
    pass

class HomerSimpson:
    def __init__ (self):
        self.name = "Homer Simpson"
        self.age = 39
        self.occupation = "Safety Officer at Springfield Nuclear Power Plant"
        self.family = {
            "wife": "Marge Simpson",
            "children": ["Bart", "Lisa", "Maggie"]
        }
        self.hobbies = ["eating donuts", "watching TV", "drinking beer"]
        self.catchphrases = [
            "D'oh!",
            "Mmm... donuts",
            "Woohoo!",
            "Why you little!"
        ]
    
    def keepWorking(self):

        start_time = time.time()
        alert = False

        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time > eight_hours:
                print(f"{self.name} has completed a full workday.")
                break

            print(f"{self.name} ... working")

            try:

                if random.random() < 0.05:
                    alert = True
                    print(f"{self.name} noticed a safety hazard at the plant!")
                    raise NuclearMeltdownException("Oh no!")

            finally:

                if alert:
                    if random.random() < 0.5:
                        raise MissingDonutException("Homer's workday was interrupted by a donut craving!")
                
                    print(f"{self.name} is still working hard at the plant...fixed the issue and moving on.")
                    alert = False

homer = HomerSimpson()
homer.keepWorking()

