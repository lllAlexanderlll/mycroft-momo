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

def random_line(file):
    with open(file) as f:
        return random.choice(list(f))


class MomoSkill(MycroftSkill):


    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(MomoSkill, self).__init__(name="Momo")

        self.username = None
        with open(os.path.join(os.path.dirname(__file__), "data/interests")) as f:
            self.interests = f.readlines()
         
        self.userInterestsDict = {
            "Hans": ["Fishing", "Cooking", "Walking"],
            "Sabine": ["Movies", "Gardening"]
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
        with open('/opt/mycroft/skills/mycroft-momo/messages/userMessage', 'a') as f:
            f.truncate(0)
            f.write(message)
    
    # def getRandomDialogEntryOrTheText(self, dialogOrText):
    #     p = os.path.join("/opt/mycroft/skills/mycroft-momo/dialog/en-us/" + dialogOrText[:-4])
    #     if(os.path.exists(p)):
    #         return random_line(p)
    #     else:
    #         return dialogOrText

    def showDialog(self, dialogOrText):
        #text = self.getRandomDialogEntryOrTheText(dialogOrText)
        with open('/opt/mycroft/skills/mycroft-momo/messages/momoMessage', 'a') as f:
            f.truncate(0)
            f.write(dialogOrText)
        return dialogOrText

    # def showAndSpeakDialog(self, dialog, waitForResponse=False):
    #     text = self.getRandomDialogEntryOrTheText(dialog)
    #     self.showDialog(text)
    #     self.speak(text, waitForResponse)

    # def showAndSpeakDialogResponse(self, dialog):
    #     text = self.getRandomDialogEntryOrTheText(dialog)
    #     self.showDialog(text)
    #     response = self.get_response(text)
    #     return response

    def get_user_response(self, dialog):
        response = self.get_response(dialog)
        return response

    @intent_handler(IntentBuilder("heyIntent").require("hey.intent"))
    def handle_start_intent(self, message):
        self.username = self.get_user_response('who.is.there')
        self.username = "Hans"
        self.showDialog("Hey! Do we know each other? What is your name?")
        self.speak_dialog("welcome.back", data={"username" : self.username})
        self.showDialog("Welcome back {}. Here is a list of your interests and events you have signed up for.".format(self.username))
        #utterance = self.dialog_renderer.render("welcome.back", data={"username" : self.username})
        #self.showDialog(utterance)

        # if(self.username in self.userInterestsDict.keys()):
        #     utterance = self.dialog_renderer.render("welcome.back", data={"username" : self.username})
        #     self.showDialog(utterance)
        #     for interest in self.userInterestsDict[self.username]:
        #         if(interest in self.eventInterest.keys()):
        #             self.showAndSpeakDialog("{}: {}".format(interest, self.eventInterest[interest]))
        #     self.showAndSpeakDialog("What do you want to do?")
        # else:
        #     self.showAndSpeakDialog("Thank you, {}. I want to help you to connect to other people with similar interests in the hospital. Would you like to do that?".format(self.username))
        #     self.showDialog("showSuggestedInterests123456")
            
            #self.userInterestsDict[username] = newUsersInterests
    
    # def stop(self):
    #     self.showAndSpeakDialog("stop")
    #     return True

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return MomoSkill()