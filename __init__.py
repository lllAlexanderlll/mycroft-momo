# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler, Message
from mycroft.util.log import LOG
import os

class MomoSkill(MycroftSkill):


    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(MomoSkill, self).__init__(name="Momo")
        with open(os.path.join(os.path.dirname(__file__), "data/interests")) as f:
            self.interests = f.readlines()
         
        self.userInterestsDict = {
            "Hans": ["Fishing", "Cooking", "Walking"],
            "Maria": ["Movies", "Gardening"]
        }

        self.eventInterest = {
            "Cooking": "Cooking class",
            "Walking": "Going to the park"
        }
    
    def initialize(self):  
        self.add_event('recognizer_loop:utterance', self.handle_utterance)

    def handle_utterance(self, data):
      self.speak_dialog(data["utterances"][0])
    
        #self.username = input("Please write your forename: ")
        
            
    @intent_handler(IntentBuilder("").require("hey.intent"))
    def handle_test_intent(self, message):
        self.speak_dialog("placeBracelet")

    def stop(self):
        self.speak_dialog("stop")
        return True

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return MomoSkill()