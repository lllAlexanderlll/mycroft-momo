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
            "hans": ["fishing", "cooking", "walking"],
            "sabine": ["movies", "gardening"]
        }

        self.eventInterest = {
            "cooking": ["cooking class"],
            "walking": ["going to the park", "walking around the hospital"]
        }

    
    # def initialize(self):  
    #     self.add_event('recognizer_loop:utterance', self.handle_utterance)

    # def handle_utterance(self, data):
    #     message = data.data["utterances"][0]
    #     self.speakAndWrite_dialog(message)
    def showUserMessage(self, message):
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
    #     self.speakAndWrite(text, waitForResponse)

    def speakAndWrite(self, text):
        self.speak(text)
        self.showDialog(text)

    # def showAndSpeakDialogResponse(self, dialog):
    #     text = self.getRandomDialogEntryOrTheText(dialog)
    #     self.showDialog(text)
    #     response = self.get_response(text)
    #     return response

    def get_user_response(self, dialog, data=None):
        response = self.get_response(dialog, data)
        return response

    @intent_handler(IntentBuilder("heyIntent").require("hey.intent"))
    def handle_start_intent(self, message):
        speech0 = "Hey! Do we know each other? What is your name?"
        self.username = self.get_user_response(speech0)
        self.showUserMessage(self.username)
        
        
        if(self.username in self.userInterestsDict.keys()):
            speech1 = "Welcome back {}.".format(self.username)
            self.speakAndWrite(speech1)
            for interest in self.userInterestsDict[self.username]:
                if(interest in self.eventInterest.keys()):
                    speech2 = "Here are some events that could interest you: {}".format(', '.join(self.eventInterest[interest]))
                    self.speakAndWrite(speech2)
                        
        else:
            speech3 = "Thank you, {}. I want to help you to connect to other people with similar interests in the hospital. Would you like to do that?".format(self.username)
            yesOrNo = self.get_user_response(speech3)

            if(yesOrNo == "yes"):
                speech4 = "Okay, to get started, please tell me some topics you are interested in. The following list can help you: Walking, Card games, Reading, Music, Cooking"
                interestsSentence = self.get_user_response(speech4)
                self.showUserMessage(interestsSentence)
                if not self.username in self.userInterestsDict:
                    self.userInterestsDict[self.username] = []
                    
                self.userInterestsDict[self.username].append(interestsSentence.lower())
                
                if len(self.userInterestsDict[self.username]) == 0:
                    speech5 = "I could not understand your interests, sorry."
                    self.speakAndWrite(speech5)
                    return

                speech6 = ", ".join(self.userInterestsDict[self.username])
                self.speakAndWrite(speech6)
                for interest in self.userInterestsDict[self.username]:
                    if(interest in self.eventInterest):
                        events = ', '.join(self.eventInterest[interest])
                if len(events) is 0:
                    self.speakAndWrite("Sorry, there are currently no events for this topic. Please ask later again.")
                else:
                    self.speakAndWrite("Perfect. Here are some events that could interest you: {}".format(events))
            else:
                self.speakAndWrite("That is okay. Just speak to me again, when you are ready.")
            
            
            #self.userInterestsDict[username] = newUsersInterests
    
    # def stop(self):
    #     self.showAndSpeakDialog("stop")
    #     return True

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return MomoSkill()