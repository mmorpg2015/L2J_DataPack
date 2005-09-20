# Maked by Mr. Have fun! Version 0.2
print "importing quests: 102: Fungus Fever"
import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

ALBERRYUS_LETTER_ID = 964
EVERGREEN_AMULET_ID = 965
DRYAD_TEARS_ID = 966
ALBERRYUS_LIST_ID = 746
COBS_MEDICINE1_ID = 1130
COBS_MEDICINE2_ID = 1131
COBS_MEDICINE3_ID = 1132
COBS_MEDICINE4_ID = 1133
COBS_MEDICINE5_ID = 1134
SWORD_OF_SENTINEL_ID = 743
STAFF_OF_SENTINEL_ID = 744

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st) :
    htmltext = event
    if event == "1" :
        st.set("id","0")
        htmltext = "7284-02.htm"
        st.giveItems(ALBERRYUS_LETTER_ID,1)
        st.set("cond","1")
        st.setState(STARTED)
        st.playSound("ItemSound.quest_accept")
    return htmltext


 def onTalk (Self,npcId,st):
   htmltext = "<html><head><body>I have nothing to say you</body></html>"
   id = st.getState()
   if id == CREATED :
     st.setState(STARTING)
     st.set("cond","0")
     st.set("onlyone","0")
     st.set("id","0")
   if npcId == 7284 and int(st.get("cond"))==0 and int(st.get("onlyone"))==0 :
        if int(st.get("cond"))<15 :
          if st.getPlayer().getRace().ordinal() != 1 :
            htmltext = "7284-00.htm"
          elif st.getPlayer().getLevel() >= 12 :
            htmltext = "7284-07.htm"
            return htmltext
          else:
            htmltext = "7284-08.htm"
        else:
          htmltext = "7284-08.htm"
   elif npcId == 7284 and int(st.get("cond"))==0 and int(st.get("onlyone"))==1 :
        htmltext = "<html><head><body>This quest have already been completed.</body></html>"
   elif npcId == 7284 and int(st.get("cond"))==1 and st.getQuestItemsCount(ALBERRYUS_LETTER_ID)==1 :
        htmltext = "7284-03.htm"
   elif npcId == 7284 and int(st.get("cond"))==1 and st.getQuestItemsCount(EVERGREEN_AMULET_ID)==1 :
        htmltext = "7284-09.htm"
   elif npcId == 7156 and int(st.get("cond"))==1 and st.getQuestItemsCount(ALBERRYUS_LETTER_ID)==1 :
        if st.getQuestItemsCount(ALBERRYUS_LETTER_ID)>0 :
          if int(st.get("id")) != 102 :
            st.set("id","102")
            st.giveItems(EVERGREEN_AMULET_ID,1)
            st.takeItems(ALBERRYUS_LETTER_ID,1)
            htmltext = "7156-03.htm"
   elif npcId == 7156 and int(st.get("cond"))==1 and st.getQuestItemsCount(EVERGREEN_AMULET_ID)>0 and st.getQuestItemsCount(DRYAD_TEARS_ID)<10 :
        htmltext = "7156-04.htm"
   elif npcId == 7156 and int(st.get("cond"))==1 and st.getQuestItemsCount(ALBERRYUS_LIST_ID)>0 :
        htmltext = "7156-07.htm"
   elif npcId == 7156 and int(st.get("cond"))==1 and st.getQuestItemsCount(EVERGREEN_AMULET_ID)>0 and st.getQuestItemsCount(DRYAD_TEARS_ID)>=10 :
        st.takeItems(EVERGREEN_AMULET_ID,1)
        st.takeItems(DRYAD_TEARS_ID,st.getQuestItemsCount(DRYAD_TEARS_ID))
        st.giveItems(COBS_MEDICINE1_ID,1)
        st.giveItems(COBS_MEDICINE2_ID,1)
        st.giveItems(COBS_MEDICINE3_ID,1)
        st.giveItems(COBS_MEDICINE4_ID,1)
        st.giveItems(COBS_MEDICINE5_ID,1)
        htmltext = "7156-05.htm"
   elif npcId == 7156 and int(st.get("cond"))==1 and st.getQuestItemsCount(ALBERRYUS_LIST_ID)==0 and (st.getQuestItemsCount(COBS_MEDICINE1_ID)==1 or st.getQuestItemsCount(COBS_MEDICINE2_ID)==1 or st.getQuestItemsCount(COBS_MEDICINE3_ID)==1 or st.getQuestItemsCount(COBS_MEDICINE4_ID)==1 or st.getQuestItemsCount(COBS_MEDICINE5_ID)==1) :
        htmltext = "7156-06.htm"
   elif npcId == 7284 and int(st.get("cond"))==1 and st.getQuestItemsCount(ALBERRYUS_LIST_ID)==0 and st.getQuestItemsCount(COBS_MEDICINE1_ID)==1 :
        st.takeItems(COBS_MEDICINE1_ID,1)
        st.giveItems(ALBERRYUS_LIST_ID,1)
        htmltext = "7284-04.htm"
   elif npcId == 7284 and int(st.get("cond"))==1 and st.getQuestItemsCount(ALBERRYUS_LIST_ID)==1 and (st.getQuestItemsCount(COBS_MEDICINE1_ID)==1 or st.getQuestItemsCount(COBS_MEDICINE2_ID)==1 or st.getQuestItemsCount(COBS_MEDICINE3_ID)==1 or st.getQuestItemsCount(COBS_MEDICINE4_ID)==1 or st.getQuestItemsCount(COBS_MEDICINE5_ID)==1) :
        htmltext = "7284-05.htm"
   elif npcId == 7217 and int(st.get("cond"))==1 and st.getQuestItemsCount(ALBERRYUS_LIST_ID)==1 and st.getQuestItemsCount(COBS_MEDICINE2_ID)==1 :
        st.set("cond",str(st.getQuestItemsCount(COBS_MEDICINE1_ID)+st.getQuestItemsCount(COBS_MEDICINE2_ID)+st.getQuestItemsCount(COBS_MEDICINE3_ID)+st.getQuestItemsCount(COBS_MEDICINE4_ID)+st.getQuestItemsCount(COBS_MEDICINE5_ID)))
        st.takeItems(COBS_MEDICINE2_ID,1)
        htmltext = "7217-01.htm"
   elif npcId == 7219 and int(st.get("cond"))==1 and st.getQuestItemsCount(ALBERRYUS_LIST_ID)==1 and st.getQuestItemsCount(COBS_MEDICINE3_ID)==1 :
        st.set("cond",str(st.getQuestItemsCount(COBS_MEDICINE1_ID)+st.getQuestItemsCount(COBS_MEDICINE2_ID)+st.getQuestItemsCount(COBS_MEDICINE3_ID)+st.getQuestItemsCount(COBS_MEDICINE4_ID)+st.getQuestItemsCount(COBS_MEDICINE5_ID)))
        st.takeItems(COBS_MEDICINE3_ID,1)
        htmltext = "7219-01.htm"
   elif npcId == 7221 and int(st.get("cond"))==1 and st.getQuestItemsCount(ALBERRYUS_LIST_ID)==1 and st.getQuestItemsCount(COBS_MEDICINE4_ID)==1 :
        st.set("cond",str(st.getQuestItemsCount(COBS_MEDICINE1_ID)+st.getQuestItemsCount(COBS_MEDICINE2_ID)+st.getQuestItemsCount(COBS_MEDICINE3_ID)+st.getQuestItemsCount(COBS_MEDICINE4_ID)+st.getQuestItemsCount(COBS_MEDICINE5_ID)))
        st.takeItems(COBS_MEDICINE4_ID,1)
        htmltext = "7221-01.htm"
   elif npcId == 7285 and int(st.get("cond"))==1 and st.getQuestItemsCount(ALBERRYUS_LIST_ID)==1 and st.getQuestItemsCount(COBS_MEDICINE5_ID)==1 :
        st.set("cond",str(st.getQuestItemsCount(COBS_MEDICINE1_ID)+st.getQuestItemsCount(COBS_MEDICINE2_ID)+st.getQuestItemsCount(COBS_MEDICINE3_ID)+st.getQuestItemsCount(COBS_MEDICINE4_ID)+st.getQuestItemsCount(COBS_MEDICINE5_ID)))
        st.takeItems(COBS_MEDICINE5_ID,1)
        htmltext = "7285-01.htm"
   elif npcId == 7284 and int(st.get("cond"))==1 and st.getQuestItemsCount(ALBERRYUS_LIST_ID)==1 and st.getQuestItemsCount(COBS_MEDICINE1_ID)==0 and st.getQuestItemsCount(COBS_MEDICINE2_ID)==0 and st.getQuestItemsCount(COBS_MEDICINE3_ID)==0 and st.getQuestItemsCount(COBS_MEDICINE4_ID)==0 and st.getQuestItemsCount(COBS_MEDICINE5_ID)==0 and int(st.get("onlyone"))==0 :
        st.takeItems(ALBERRYUS_LIST_ID,1)
        st.set("cond","0")
        st.setState(COMPLETED)
        st.playSound("ItemSound.quest_finish")
        htmltext = "7284-06.htm"
        st.set("onlyone","1")
        if st.getPlayer().getClassId().getId() == 0x00 or st.getPlayer().getClassId().getId() == 0x12 or st.getPlayer().getClassId().getId() == 0x1f or st.getPlayer().getClassId().getId() == 0x07 or st.getPlayer().getClassId().getId() == 0x01 or st.getPlayer().getClassId().getId() == 0x13 or st.getPlayer().getClassId().getId() == 0x16 or st.getPlayer().getClassId().getId() == 0x23 or st.getPlayer().getClassId().getId() == 0x04 or st.getPlayer().getClassId().getId() == 0x20 or st.getPlayer().getClassId().getId() == 0x2c or st.getPlayer().getClassId().getId() == 0x2f or st.getPlayer().getClassId().getId() == 0x35 or st.getPlayer().getClassId().getId() == 0x36 or st.getPlayer().getClassId().getId() == 0x38 or st.getPlayer().getClassId().getId() == 0x2d :
          st.giveItems(SWORD_OF_SENTINEL_ID,1)
        else:
          st.giveItems(STAFF_OF_SENTINEL_ID,1)
   return htmltext

 def onKill (self,npcId,st):
   if npcId == 13 :
        st.set("id","0")
        if st.getQuestItemsCount(EVERGREEN_AMULET_ID)>0 and st.getQuestItemsCount(DRYAD_TEARS_ID)<10 :
          if st.getRandom(10)<3 :
            st.giveItems(DRYAD_TEARS_ID,1)
            if st.getQuestItemsCount(DRYAD_TEARS_ID) == 10 :
              st.playSound("ItemSound.quest_middle")
            else:
              st.playSound("ItemSound.quest_itemget")
   elif npcId == 19 :
        st.set("id","0")
        if st.getQuestItemsCount(EVERGREEN_AMULET_ID)>0 and st.getQuestItemsCount(DRYAD_TEARS_ID)<10 :
          if st.getRandom(10)<3 :
            st.giveItems(DRYAD_TEARS_ID,1)
            if st.getQuestItemsCount(DRYAD_TEARS_ID) == 10 :
              st.playSound("ItemSound.quest_middle")
            else:
              st.playSound("ItemSound.quest_itemget")
   return

QUEST       = Quest(102,"102_FungusFever","Fungus Fever")
CREATED     = State('Start', QUEST)
STARTING     = State('Starting', QUEST)
STARTED     = State('Started', QUEST)
COMPLETED   = State('Completed', QUEST)


QUEST.setInitialState(CREATED)
QUEST.addStartNpc(7284)

STARTING.addTalkId(7284)

STARTED.addTalkId(7156)
STARTED.addTalkId(7217)
STARTED.addTalkId(7219)
STARTED.addTalkId(7221)
STARTED.addTalkId(7284)
STARTED.addTalkId(7285)

STARTED.addKillId(13)
STARTED.addKillId(19)

STARTED.addQuestDrop(7284,ALBERRYUS_LETTER_ID,1)
STARTED.addQuestDrop(7156,EVERGREEN_AMULET_ID,1)
STARTED.addQuestDrop(13,DRYAD_TEARS_ID,1)
STARTED.addQuestDrop(19,DRYAD_TEARS_ID,1)
STARTED.addQuestDrop(7156,COBS_MEDICINE1_ID,1)
STARTED.addQuestDrop(7156,COBS_MEDICINE2_ID,1)
STARTED.addQuestDrop(7156,COBS_MEDICINE3_ID,1)
STARTED.addQuestDrop(7156,COBS_MEDICINE4_ID,1)
STARTED.addQuestDrop(7156,COBS_MEDICINE5_ID,1)
STARTED.addQuestDrop(7284,ALBERRYUS_LIST_ID,1)
