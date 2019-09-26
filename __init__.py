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

class MomoSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(MomoSkill, self).__init__(name="Momo")
        
        # Initialize working variables used within the skill.
        self.iterests = ["card games", "sports", "movies", "reading", "walking", "gardening"]
    

    def initialize(self):  
        self.add_event('recognizer_loop:wakeword', self.handle_hey_momo)  

    def handle_hey_momo(self, message):  
        self.speak_dialog("heyMomo")

    @intent_handler(IntentBuilder("").require("test.intent"))
    def handle_test_intent(self, message):
        self.gui["test_string"] = self.
        self.gui.show_page("clock_face.qml")
        self.speak_dialog("test")
        self.register_vocabulary("TestWordA", "test")
        self.register_vocabulary("TestWordB", "test.intent")

    # @intent_handler(IntentBuilder("").require("Count").require("Dir"))
    # def handle_count_intent(self, message):
    #     if message.data["Dir"] == "up":
    #         self.count += 1
    #     else:  # assume "down"
    #         self.count -= 1
    #     self.speak_dialog("count.is.now", data={"count": self.count})

    def stop(self):
        self.speak_dialog("stop")
        return True

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return MomoSkill()