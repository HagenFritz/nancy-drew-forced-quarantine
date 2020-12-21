import sys

from treelib import Node, Tree

import config

class Conversations():

    def __init__(self):
        pass

    def firstConversation(self):
        c = Tree()
        # root
        c.create_node("Waltz Ingman",1,data={"loc":"u","answer":"...","audio":"fc_1"})

        c.create_node("Who the hell are you?",11,parent=1,data={"loc":"u","answer":"I could ask you the same thing.","audio":"fc_11"})
        c.create_node("Umm hi.",12,parent=1,data={"loc":"d","answer":"Hello! I am Dr. Waltz Ingman.","audio":"fc_12"})
        # I could ask you the same thing
        c.create_node("I asked first.",111,parent=11,data={"loc":"u","answer":"Okay then. I am Dr. Waltz Ingman. Who are you?","audio":"fc_111"})
        c.create_node("My name is Nancy Drew.",112,parent=11,data={"loc":"d","answer":"Nancy? Pretty name. My name is Dr. Waltz Ingman!","audio":"fc_112"})
        # Okay then. I am Dr. Waltz Ingman. Who are you?
        c.create_node("Dr.?",1111,parent=111,data={"loc":"u","answer":"of psychology. Although that won't seem to help in our present situation.","audio":"fc_1121"})
        c.create_node("My name is Nancy Drew.",1112,parent=111,data={"loc":"d","answer":"Nancy? Pretty name. My name is Dr. Waltz Ingman!","audio":"fc_112"})
        # of psychology. Although that won't seem to help in our present situation
        c.create_node("Hmm perhaps I should look around.",11111,parent=1111,data={"loc":"u","answer":"You still haven't answered my question...who are YOU?","audio":"fc_11111"})
        # You still haven't answered my question...who are YOU?
        c.create_node("Oh, sorry. My name is Nancy. Nancy Drew!",111110,parent=11111,data={"loc":"u","answer":"Pretty name. Well Nancy, feel free to look about. I'll need a moment here.","audio":"fc_12110"})
        # Nancy? Pretty name. My name is Dr. Waltz Ingman!
        c.create_node("Dr.?",11121,parent=1112,data={"loc":"u","answer":"of psychology. Although that won't seem to help in our present situation.","audio":"fc_1121"})
        c.create_node("Do you know what we are doing here?",11122,parent=1112,data={"loc":"d","answer":"Not a clue. One minute I was at home, now I am here.","audio":"fc_1122"})
        # of psychology. Although that won't seem to help in our present situation.
        c.create_node("Hmm perhaps I should look around.",111210,parent=11121,data={"loc":"u","answer":"Have at it. I'm going to take a moment to gather myself.","audio":"fc_111210"})
        #Not a clue. One minute I was at home, now I am here
        c.create_node("Hmm perhaps I should look around.",111220,parent=11122,data={"loc":"u","answer":"Be careful. I'm going to take a moment to gather myself.","audio":"fc_111220"})
        # Hello! I am Dr. Waltz Ingman
        c.create_node("Dr.?",121,parent=12,data={"loc":"u","answer":"of psychology. Although that won't seem to help in our present situation.","audio":"fc_1121"})
        c.create_node("Do you know what we are doing here?",122,parent=12,data={"loc":"d","answer":"Not a clue. I figured YOU might be able to tell me.","audio":"fc_122"})
        # of psychology. Although that won't seem to help in our present situation."
        c.create_node("Hmm perhaps I should look around.",1211,parent=121,data={"loc":"u","answer":"You still haven't answered my question...who are YOU?","audio":"fc_11111"})
        # You still haven't answered my question...who are YOU?
        c.create_node("Oh, sorry. My name is Nancy. Nancy Drew!",12110,parent=1211,data={"loc":"u","answer":"Pretty name. Well Nancy, feel free to look about. I'll need a moment here.","audio":"fc_12110"})
        # I haven't a clue. I was hoping you might be able to tell me.
        c.create_node("Me? I am just as confused as you.",1221,parent=122,data={"loc":"u","answer":"Hmm then seems we are in a bit of a pickle here. Still, nice place.","audio":"fc_1221"})
        c.create_node("Hmm perhaps I should look around.",1220,parent=122,data={"loc":"d","answer":"Knock yourself out. Well...not literally.","audio":"fc_1221"})
        # Hmm then seems we are in a bit of a pickle here. Still, nice place.
        c.create_node("Hmm perhaps I should look around.",12210,parent=1221,data={"loc":"u","answer":"Have at it. Im going to take a moment to gather myself.","audio":"fc_111210"})
        # My name is Nancy Drew
        c.create_node("Dr.?",1121,parent=112,data={"loc":"u","answer":"of psychology. Although that won't seem to help in our present situation.","audio":"fc_1121"})
        c.create_node("Do you know what we are doing here?",1122,parent=112,data={"loc":"d","answer":"Not a clue. One minute I was at home, now I am here.","audio":"fc_1122"})
        # of psychology. Although that won't seem to help in our present situation.
        c.create_node("Yeah that won't help here unless there is someone else about.",11211,parent=1121,data={"loc":"u","answer":"I sure hope not. Then again, it seems there are other rooms.","audio":"fc_11211"})
        c.create_node("Hmm perhaps I should look around.",11210,parent=1121,data={"loc":"d","answer":"Yes please! I am just going to wait for your all-clear.","audio":"fc_112110"})
        # I sure hope not. Then again, it seems there are other rooms.
        c.create_node("Hmm perhaps I should look around.",112110,parent=11211,data={"loc":"u","answer":"Yes please! I am just going to wait for your all-clear.","audio":"fc_112110"})
        # Not a clue. One minute I was at home, now I am here.
        c.create_node("Hmm perhaps I should look around.",11220,parent=1122,data={"loc":"u","answer":"Be my guest. Well...err...poor choice of words.","audio":"fc_11220"})

        return c

    def coffeeConversation(self):
        c = Tree()
        # root
        c.create_node("Waltz Ingman",1,data={"loc":"u","answer":"ugh","audio":"cc_1"})

        c.create_node("What's wrong?",11,parent=1,data={"loc":"u","answer":"Just so tired...never felt so groggy","audio":"cc_11"})
        
        # Just so tired...never felt so groggy
        c.create_node("Can I help?",111,parent=11,data={"loc":"u","answer":"Actually yeah. I could really use a cup of coffee. Think you could make me some?","audio":"cc_111"})
        c.create_node("Hmm perhaps I can get you some coffee or tea?",112,parent=11,data={"loc":"d","answer":"That would be amazing! I am sure there is a mug around here somewhere.","audio":"cc_112"})

        # Actually yeah. I could really use a cup of coffee. Think you could make me some?
        c.create_node("Absolutely!",1111,parent=111,data={"loc":"u","answer":"Thank you so much! I promise to help once I can think properly.","audio":"cc_1111"})
        c.create_node("Yeah, I suppose.",1112,parent=111,data={"loc":"d","answer":"I know it's a lot to ask, but it's hard enough to speak right now properly.","audio":"cc_1112"})
        # Thank you so much! I promise to help once I can think properly.
        c.create_node("I think I saw a mug around here. Let me ge check.",11111,parent=1111,data={"loc":"u","answer":"Oh thank you so much! I owe you big time.","audio":"cc_11111"})
        # I know it's a lot to ask, but it's hard enough to speak right now properly.
        c.create_node("I think I saw a mug around here. Let me ge check.",11112,parent=1112,data={"loc":"u","answer":"Oh thank you so much! I owe you big time.","audio":"cc_11111"})
        
        return c

    def badCoffee(self):
        c = Tree()
        # root
        c.create_node("Waltz Ingman",1,data={"loc":"u","answer":"Hey","audio":"bc_1"})

        c.create_node("Here's your coffee.",11,parent=1,data={"loc":"u","answer":"Excellent! Sorry, that is just a bad cup of coffee.","audio":"bc_11"})
        # Excellent! Sorry, this is just a bad cup of coffee...
        c.create_node("Oh, well let me try again.",111,parent=11,data={"loc":"u","answer":"Thanks! There should be a note around here about proper brewing","audio":"bc_111"})
        c.create_node("Seriously? You are that picky? We are in a situation here.",112,parent=11,data={"loc":"d","answer":"I get that, but if you want my help I require certain aids.","audio":"bc_112"})
        # I get that, but if you want my help I require certain aids.
        c.create_node("Fine. I will try again.",1121,parent=112,data={"loc":"u","answer":"Thanks! There should be a note around here about proper brewing","audio":"bc_111"})

        return c

    def goodCoffee(self):
        c = Tree()
        # root
        c.create_node("Waltz Ingman",1,data={"loc":"u","answer":"Hey","audio":"bc_1"})

        c.create_node("Here's you coffee.",11,parent=1,data={"loc":"u","answer":"Excellent! Oh, this is nice and strong. Thanks!","audio":"gc_11"})
        # Excellent! Oh, that is nice and strong. Thanks!
        c.create_node("You're welcome!",111,parent=11,data={"loc":"u","answer":"Alright, now what do we do about this situation?","audio":"gc_111"})
        c.create_node("Now do you remember anything before waking up here?",112,parent=11,data={"loc":"d","answer":"I just remember working late in my office and then BAM! Woke up here. What about you?","audio":"gc_112"}) # need recording
        # Alright, now what do we do about this situation?
        c.create_node("I looked around, but didn't find anything. I am having trouble focusing though.",1111,parent=111,data={"loc":"u","answer":"Hmm yeah you don't look so good. They must've drugged you pretty badly. Why don't you go lay down in that room behind you? I can explore a bit once I finish my coffee.","audio":"gc_1111"})
        # Hmm yeah you don't look so good. They must've drugged you pretty badly. Why don't you go lay down in that room behind you? I can explore a bit once I finish my coffee.
        c.create_node("That is probably smart. I will lay down for a couple of hours.",11111,parent=1111,data={"loc":"u","answer":"Good plan. Should be morning in a few hours. Just make sure you set an alarm or you might sleep all day!","audio":"gc_11111"}) # need recording
        # I just remember working late in my office and then BAM! Woke up here. What about you?
        c.create_node("I know I ordered food and was just sitting down to eat.",1121,parent=112,data={"loc":"d","answer":"Sounds like someone might've drugged your food. Looks like it still might not be totally out of your system either. Perhaps you should get some rest in the room behind you?","audio":"gc_1121"})  # need recording
        # Sounds like someone might've drugged your food. Looks like it still might not be totally out of your system either. Perhaps you should get some rest in the room behind you?
        c.create_node("That is probably smart. I will lay down for a couple of hours.",11211,parent=1121,data={"loc":"u","answer":"Good plan. Should be morning in a few hours. Just make sure you set an alarm or you might sleep all day!","audio":"gc_11111"}) # need recording

        return c

    def firstMessage(self):
        c = Tree()
        # root
        c.create_node("Waltz Ingman",1,data={"loc":"u","answer":"Yes?","audio":"nu_1"})

        c.create_node("I found a note.",11,parent=1,data={"loc":"u","answer":"A what?","audio":"fm_11"})
        # A what?
        c.create_node("A note. You know...the thing people write to each other?",111,parent=11,data={"loc":"u","answer":"Oh, yes. Sorry, what did it say?","audio":"fm_111"})

        return c

    def noUpdates(self):
        c = Tree()
        # root
        c.create_node("Waltz Ingman",1,data={"loc":"u","answer":"Yes?","audio":"nu_1"})

        c.create_node("Nevermind",12,parent=1,data={"loc":"u","answer":"Seeya","audio":"nu_11"})

        return c



