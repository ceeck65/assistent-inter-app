# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 15:08:46 2023

@author: alesp
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 02:42:38 2023

@author: alesp
"""

from PyQt5.QtWidgets import (
    QDialog,
)

from modules.Dashboard.dashboard_ui import Ui_Dialog
from modules.Data.data import setChat, getChat, resetChat, setChatTransfer, getChatTransfer, resetChatTransfer


class Dashboard(QDialog):
    def __init__(self):
        super(Dashboard, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.add_chats.clicked.connect(self.addChat)
        self.ui.clear_chats.clicked.connect(self.removeChat)
        self.ui.clear_chats_all.clicked.connect(self.clearChats)
        self.ui.transfers_chats.clicked.connect(self.addChatTransfer)
        self.ui.clear_transfers_chats.clicked.connect(self.clearChatsTransfer)
        self.ui.chats.setText(str(getChat()))
        self.ui.chats_tranfers.setText(str(getChatTransfer()))
        
    def addChat(self):
        chat = getChat()
        chat = chat + 1
        setChat(chat)
        self.ui.chats.setText(str(getChat()))
    
    def removeChat(self):
        chat = getChat()
        chat = chat - 1
        setChat(chat)
        self.ui.chats.setText(str(getChat()))

    def clearChats(self):
        resetChat()
        self.ui.chats.setText(str(getChat()))

    def addChatTransfer(self):
        chat = getChatTransfer()
        chat = chat + 1
        setChatTransfer(chat)
        self.ui.chats_tranfers.setText(str(getChatTransfer()))
    
    def clearChatsTransfer(self):
        resetChatTransfer()
        self.ui.chats_tranfers.setText(str(getChat()))

        
