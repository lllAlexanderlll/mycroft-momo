# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG
import os
import random

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num): continue
        line = aline
    return line

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
            "Cooking": ["Cooking class"],
            "Walking": ["Going to the park", "Walking around the hospital"]
        }

    
    def initialize(self):  
        self.add_event('recognizer_loop:utterance', self.handle_utterance)

    def handle_utterance(self, data):
        message = data.data["utterances"][0]
        self.speak_dialog(message)
        with open('/opt/mycroft/skills/mycroft-momo/user/message', 'a') as f:
            f.truncate(0)
            f.write(message)

    def showDialog(self, dialog):
        with open('/opt/mycroft/skills/mycroft-momo/momo/message', 'a') as f:
            f.truncate(0)
            f.write(dialog)

    def getRandomDialogEntryOrTheText(self, dialogOrText):
        p = os.path.join("/opt/mycroft/skills/mycroft-momo/dialog/en-us/" + dialogOrText[:-4])
        if(os.path.exists(p)):
            return random_line(p)
        else:
            return dialogOrText

    def showAndSpeakDialog(self, dialog, waitForResponse=False):
        text = self.getRandomDialogEntryOrTheText(dialog)
        self.showDialog(text)
        self.speak(text, waitForResponse)

    def get_user_response(self, dialog):
        response = self.get_response(dialog)
        return response

    @intent_handler(IntentBuilder("heyIntent").require("hey.intent"))
    def handle_start_intent(self, message):
        self.showAndSpeakDialog("Hey! Do we know each other? What is your name?")
        username = self.get_user_response("test")
        if(username in self.userInterestsDict.keys()):
            self.showAndSpeakDialog("Welcome back {}. Here is a list of your interests and events you have signed up for.".format(username))
            for interest in self.userInterestsDict[username]:
                if(interest in self.eventInterest.keys()):
                    self.showAndSpeakDialog("{}: {}".format(interest, self.eventInterest[interest]))
            self.showAndSpeakDialog("What do you want to do?")
        else:
            self.showAndSpeakDialog("Thank you, {}. I want to help you to connect to other people with similar interests in the hospital. Would you like to do that?".format(username))
            self.showDialog("showSuggestedInterests123456")
            #self.userInterestsDict[username] = newUsersInterests
    
    @intent_handler(IntentBuilder("bla"))
    def handle_wouldYouLikeHelp_intent(self, message):
        pass
        
    # def stop(self):
    #     self.showAndSpeakDialog("stop")
    #     return True

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return MomoSkill()