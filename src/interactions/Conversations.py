import sys

from treelib import Node, Tree

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

    def firstMessage(self):
        c = Tree()
        # root
        c.create_node("Waltz Ingman",1,data={"loc":"u","answer":"...","audio":"fc_1"})

        return c


