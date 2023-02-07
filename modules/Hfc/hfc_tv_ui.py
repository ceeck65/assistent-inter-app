# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hfc_tv.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1355, 650)
        self.tabWidgetTicketsHfcTv = QtWidgets.QTabWidget(Dialog)
        self.tabWidgetTicketsHfcTv.setGeometry(QtCore.QRect(10, 10, 1329, 651))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidgetTicketsHfcTv.setFont(font)
        self.tabWidgetTicketsHfcTv.setIconSize(QtCore.QSize(24, 24))
        self.tabWidgetTicketsHfcTv.setElideMode(QtCore.Qt.ElideLeft)
        self.tabWidgetTicketsHfcTv.setUsesScrollButtons(True)
        self.tabWidgetTicketsHfcTv.setObjectName("tabWidgetTicketsHfcTv")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBoxPremiumTVHfc = QtWidgets.QGroupBox(self.tab)
        self.groupBoxPremiumTVHfc.setGeometry(QtCore.QRect(20, 60, 280, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBoxPremiumTVHfc.setFont(font)
        self.groupBoxPremiumTVHfc.setObjectName("groupBoxPremiumTVHfc")
        self.groupBoxAditionalTVHfc = QtWidgets.QGroupBox(self.tab)
        self.groupBoxAditionalTVHfc.setGeometry(QtCore.QRect(330, 300, 311, 100))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBoxAditionalTVHfc.setFont(font)
        self.groupBoxAditionalTVHfc.setObjectName("groupBoxAditionalTVHfc")
        self.lbl_total_dth = QtWidgets.QLabel(self.tab)
        self.lbl_total_dth.setGeometry(QtCore.QRect(330, 10, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_total_dth.setFont(font)
        self.lbl_total_dth.setObjectName("lbl_total_dth")
        self.btn_ticket_hfc_tv = QtWidgets.QPushButton(self.tab)
        self.btn_ticket_hfc_tv.setGeometry(QtCore.QRect(810, 470, 160, 60))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_ticket_hfc_tv.setIcon(icon)
        self.btn_ticket_hfc_tv.setObjectName("btn_ticket_hfc_tv")
        self.btn_clear_hfc_tv = QtWidgets.QPushButton(self.tab)
        self.btn_clear_hfc_tv.setGeometry(QtCore.QRect(1000, 470, 160, 60))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_clear_hfc_tv.setIcon(icon1)
        self.btn_clear_hfc_tv.setObjectName("btn_clear_hfc_tv")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(810, 40, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(810, 252, 80, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_8.setGeometry(QtCore.QRect(330, 60, 311, 231))
        self.groupBox_8.setObjectName("groupBox_8")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_8)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 170, 281, 46))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_2.setEnabled(False)
        self.comboBox_2.setMaximumSize(QtCore.QSize(300, 500))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.verticalLayout_6.addWidget(self.comboBox_2)
        self.is_internet_hfc = QtWidgets.QCheckBox(self.groupBox_8)
        self.is_internet_hfc.setGeometry(QtCore.QRect(10, 40, 211, 21))
        self.is_internet_hfc.setObjectName("is_internet_hfc")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_8)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 140, 211, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_8)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 81, 281, 46))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.combo_internet_hfc = QtWidgets.QComboBox(self.layoutWidget1)
        self.combo_internet_hfc.setEnabled(False)
        self.combo_internet_hfc.setMaximumSize(QtCore.QSize(300, 500))
        self.combo_internet_hfc.setObjectName("combo_internet_hfc")
        self.combo_internet_hfc.addItem("")
        self.verticalLayout_2.addWidget(self.combo_internet_hfc)
        self.ticket_ab_hfc_tv = QtWidgets.QTextEdit(self.tab)
        self.ticket_ab_hfc_tv.setGeometry(QtCore.QRect(810, 60, 450, 160))
        self.ticket_ab_hfc_tv.setObjectName("ticket_ab_hfc_tv")
        self.ticket_k2b_hfc_tv = QtWidgets.QTextEdit(self.tab)
        self.ticket_k2b_hfc_tv.setGeometry(QtCore.QRect(810, 270, 450, 160))
        self.ticket_k2b_hfc_tv.setObjectName("ticket_k2b_hfc_tv")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/images/icons/tv.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidgetTicketsHfcTv.addTab(self.tab, icon2, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.btn_ticket_hfc_tv_support = QtWidgets.QPushButton(self.tab_2)
        self.btn_ticket_hfc_tv_support.setGeometry(QtCore.QRect(810, 470, 161, 61))
        self.btn_ticket_hfc_tv_support.setIcon(icon)
        self.btn_ticket_hfc_tv_support.setObjectName("btn_ticket_hfc_tv_support")
        self.btn_clear_hfc_tv_support = QtWidgets.QPushButton(self.tab_2)
        self.btn_clear_hfc_tv_support.setGeometry(QtCore.QRect(1000, 470, 161, 61))
        self.btn_clear_hfc_tv_support.setIcon(icon1)
        self.btn_clear_hfc_tv_support.setObjectName("btn_clear_hfc_tv_support")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(810, 40, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(810, 250, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 60, 261, 81))
        self.groupBox_6.setObjectName("groupBox_6")
        self.hfc_tv_cable_failure = QtWidgets.QComboBox(self.groupBox_6)
        self.hfc_tv_cable_failure.setGeometry(QtCore.QRect(10, 30, 241, 22))
        self.hfc_tv_cable_failure.setObjectName("hfc_tv_cable_failure")
        self.hfc_tv_cable_failure.addItem("")
        self.hfc_tv_cable_failure.addItem("")
        self.hfc_tv_cable_failure.addItem("")
        self.hfc_tv_cable_failure.addItem("")
        self.hfc_tv_cable_failure.addItem("")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_7.setGeometry(QtCore.QRect(20, 390, 741, 161))
        self.groupBox_7.setObjectName("groupBox_7")
        self.hfc_tv_motive = QtWidgets.QTextEdit(self.groupBox_7)
        self.hfc_tv_motive.setGeometry(QtCore.QRect(10, 30, 711, 111))
        self.hfc_tv_motive.setReadOnly(True)
        self.hfc_tv_motive.setObjectName("hfc_tv_motive")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_9.setGeometry(QtCore.QRect(20, 150, 261, 211))
        self.groupBox_9.setObjectName("groupBox_9")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_9)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 35, 231, 151))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.hfc_tv_successful_support = QtWidgets.QRadioButton(self.layoutWidget2)
        self.hfc_tv_successful_support.setObjectName("hfc_tv_successful_support")
        self.verticalLayout_5.addWidget(self.hfc_tv_successful_support)
        self.hfc_tv_unsuccessful_support = QtWidgets.QRadioButton(self.layoutWidget2)
        self.hfc_tv_unsuccessful_support.setObjectName("hfc_tv_unsuccessful_support")
        self.verticalLayout_5.addWidget(self.hfc_tv_unsuccessful_support)
        self.hfc_tv_connect_disconect = QtWidgets.QCheckBox(self.layoutWidget2)
        self.hfc_tv_connect_disconect.setObjectName("hfc_tv_connect_disconect")
        self.verticalLayout_5.addWidget(self.hfc_tv_connect_disconect)
        self.hfc_tv_connections_ok = QtWidgets.QCheckBox(self.layoutWidget2)
        self.hfc_tv_connections_ok.setObjectName("hfc_tv_connections_ok")
        self.verticalLayout_5.addWidget(self.hfc_tv_connections_ok)
        self.hfc_tv__ticket_ab_support = QtWidgets.QTextEdit(self.tab_2)
        self.hfc_tv__ticket_ab_support.setGeometry(QtCore.QRect(810, 60, 450, 160))
        self.hfc_tv__ticket_ab_support.setObjectName("hfc_tv__ticket_ab_support")
        self.hfc_tv__ticket_k2b_support = QtWidgets.QTextEdit(self.tab_2)
        self.hfc_tv__ticket_k2b_support.setGeometry(QtCore.QRect(810, 270, 450, 160))
        self.hfc_tv__ticket_k2b_support.setObjectName("hfc_tv__ticket_k2b_support")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/images/icons/support.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidgetTicketsHfcTv.addTab(self.tab_2, icon3, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_4.setGeometry(QtCore.QRect(410, 150, 341, 151))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_4)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 30, 321, 98))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.dth_coomand_not_send = QtWidgets.QCheckBox(self.layoutWidget3)
        self.dth_coomand_not_send.setObjectName("dth_coomand_not_send")
        self.verticalLayout_4.addWidget(self.dth_coomand_not_send)
        self.dth_refresh = QtWidgets.QCheckBox(self.layoutWidget3)
        self.dth_refresh.setObjectName("dth_refresh")
        self.verticalLayout_4.addWidget(self.dth_refresh)
        self.label = QtWidgets.QLabel(self.layoutWidget3)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.combo_dth_command = QtWidgets.QComboBox(self.layoutWidget3)
        self.combo_dth_command.setObjectName("combo_dth_command")
        self.combo_dth_command.addItem("")
        self.combo_dth_command.addItem("")
        self.combo_dth_command.addItem("")
        self.combo_dth_command.addItem("")
        self.combo_dth_command.addItem("")
        self.combo_dth_command.addItem("")
        self.combo_dth_command.addItem("")
        self.combo_dth_command.addItem("")
        self.combo_dth_command.addItem("")
        self.combo_dth_command.addItem("")
        self.verticalLayout_4.addWidget(self.combo_dth_command)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 150, 341, 151))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.txt_dth_decoder = QtWidgets.QLineEdit(self.groupBox_5)
        self.txt_dth_decoder.setGeometry(QtCore.QRect(20, 30, 221, 30))
        self.txt_dth_decoder.setObjectName("txt_dth_decoder")
        self.btn_add_decoder_dth = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_add_decoder_dth.setGeometry(QtCore.QRect(250, 30, 32, 32))
        self.btn_add_decoder_dth.setToolTipDuration(2)
        self.btn_add_decoder_dth.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/images/icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_decoder_dth.setIcon(icon4)
        self.btn_add_decoder_dth.setIconSize(QtCore.QSize(24, 24))
        self.btn_add_decoder_dth.setObjectName("btn_add_decoder_dth")
        self.btn_remove_decoder_dth = QtWidgets.QPushButton(self.groupBox_5)
        self.btn_remove_decoder_dth.setGeometry(QtCore.QRect(290, 30, 32, 32))
        self.btn_remove_decoder_dth.setToolTipDuration(2)
        self.btn_remove_decoder_dth.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/images/icons/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_remove_decoder_dth.setIcon(icon5)
        self.btn_remove_decoder_dth.setIconSize(QtCore.QSize(24, 24))
        self.btn_remove_decoder_dth.setObjectName("btn_remove_decoder_dth")
        self.dth_list_decoder = QtWidgets.QListWidget(self.groupBox_5)
        self.dth_list_decoder.setGeometry(QtCore.QRect(20, 70, 301, 61))
        self.dth_list_decoder.setObjectName("dth_list_decoder")
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_10.setGeometry(QtCore.QRect(20, 60, 341, 80))
        self.groupBox_10.setObjectName("groupBox_10")
        self.combo_dth_failure_2 = QtWidgets.QComboBox(self.groupBox_10)
        self.combo_dth_failure_2.setGeometry(QtCore.QRect(10, 30, 321, 22))
        self.combo_dth_failure_2.setObjectName("combo_dth_failure_2")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.combo_dth_failure_2.addItem("")
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_11.setGeometry(QtCore.QRect(430, 430, 351, 161))
        self.groupBox_11.setObjectName("groupBox_11")
        self.hfc_tv_commands_2 = QtWidgets.QTextEdit(self.groupBox_11)
        self.hfc_tv_commands_2.setGeometry(QtCore.QRect(10, 30, 331, 111))
        self.hfc_tv_commands_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.hfc_tv_commands_2.setAutoFillBackground(True)
        self.hfc_tv_commands_2.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.hfc_tv_commands_2.setReadOnly(True)
        self.hfc_tv_commands_2.setObjectName("hfc_tv_commands_2")
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_12.setGeometry(QtCore.QRect(20, 430, 391, 161))
        self.groupBox_12.setObjectName("groupBox_12")
        self.hfc_tv_motive_2 = QtWidgets.QTextEdit(self.groupBox_12)
        self.hfc_tv_motive_2.setGeometry(QtCore.QRect(10, 30, 371, 111))
        self.hfc_tv_motive_2.setReadOnly(True)
        self.hfc_tv_motive_2.setObjectName("hfc_tv_motive_2")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(810, 40, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(810, 250, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.btn_clear_dth__support_2 = QtWidgets.QPushButton(self.tab_3)
        self.btn_clear_dth__support_2.setGeometry(QtCore.QRect(1000, 470, 161, 61))
        self.btn_clear_dth__support_2.setIcon(icon1)
        self.btn_clear_dth__support_2.setObjectName("btn_clear_dth__support_2")
        self.hfc_tv__ticket_k2b_support_2 = QtWidgets.QTextEdit(self.tab_3)
        self.hfc_tv__ticket_k2b_support_2.setGeometry(QtCore.QRect(810, 270, 450, 160))
        self.hfc_tv__ticket_k2b_support_2.setObjectName("hfc_tv__ticket_k2b_support_2")
        self.btn_ticket_dth_support_2 = QtWidgets.QPushButton(self.tab_3)
        self.btn_ticket_dth_support_2.setGeometry(QtCore.QRect(810, 470, 161, 61))
        self.btn_ticket_dth_support_2.setIcon(icon)
        self.btn_ticket_dth_support_2.setObjectName("btn_ticket_dth_support_2")
        self.hfc_tv__ticket_ab_support_2 = QtWidgets.QTextEdit(self.tab_3)
        self.hfc_tv__ticket_ab_support_2.setGeometry(QtCore.QRect(810, 60, 450, 160))
        self.hfc_tv__ticket_ab_support_2.setObjectName("hfc_tv__ticket_ab_support_2")
        self.groupBox_13 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_13.setGeometry(QtCore.QRect(410, 60, 341, 80))
        self.groupBox_13.setObjectName("groupBox_13")
        self.combo_dth_failure_3 = QtWidgets.QComboBox(self.groupBox_13)
        self.combo_dth_failure_3.setGeometry(QtCore.QRect(10, 30, 321, 22))
        self.combo_dth_failure_3.setObjectName("combo_dth_failure_3")
        self.combo_dth_failure_3.addItem("")
        self.combo_dth_failure_3.addItem("")
        self.combo_dth_failure_3.addItem("")
        self.combo_dth_failure_3.addItem("")
        self.combo_dth_failure_3.addItem("")
        self.combo_dth_failure_3.addItem("")
        self.combo_dth_failure_3.addItem("")
        self.combo_dth_failure_3.addItem("")
        self.combo_dth_failure_3.addItem("")
        self.combo_dth_failure_3.addItem("")
        self.combo_dth_failure_3.addItem("")
        self.groupBox_14 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_14.setGeometry(QtCore.QRect(30, 330, 731, 71))
        self.groupBox_14.setObjectName("groupBox_14")
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox_14)
        self.layoutWidget4.setGeometry(QtCore.QRect(11, 27, 711, 31))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dth_successful_support_2 = QtWidgets.QRadioButton(self.layoutWidget4)
        self.dth_successful_support_2.setObjectName("dth_successful_support_2")
        self.horizontalLayout.addWidget(self.dth_successful_support_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.dth_unsuccessful_support_2 = QtWidgets.QRadioButton(self.layoutWidget4)
        self.dth_unsuccessful_support_2.setObjectName("dth_unsuccessful_support_2")
        self.horizontalLayout.addWidget(self.dth_unsuccessful_support_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.dth_connections_ok_2 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.dth_connections_ok_2.setObjectName("dth_connections_ok_2")
        self.horizontalLayout.addWidget(self.dth_connections_ok_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.dth_not_manupulate_ant_2 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.dth_not_manupulate_ant_2.setObjectName("dth_not_manupulate_ant_2")
        self.horizontalLayout.addWidget(self.dth_not_manupulate_ant_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.tabWidgetTicketsHfcTv.addTab(self.tab_3, "")

        self.retranslateUi(Dialog)
        self.tabWidgetTicketsHfcTv.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBoxPremiumTVHfc.setTitle(_translate("Dialog", "TV Cable / Planes / Premiun"))
        self.groupBoxAditionalTVHfc.setTitle(_translate("Dialog", "Deco / Cajas Digitales"))
        self.lbl_total_dth.setText(_translate("Dialog", "Total Bs."))
        self.btn_ticket_hfc_tv.setText(_translate("Dialog", "Generar Ticket"))
        self.btn_clear_hfc_tv.setText(_translate("Dialog", "Limpiar"))
        self.label_3.setText(_translate("Dialog", "Ticket Abonado"))
        self.label_7.setText(_translate("Dialog", "Ticket K2B"))
        self.groupBox_8.setTitle(_translate("Dialog", "Planes de internet y Telefonía"))
        self.label_6.setText(_translate("Dialog", "Plan de Telefonía"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Seleccione"))
        self.is_internet_hfc.setText(_translate("Dialog", "¿Posee Plan de Internet?"))
        self.checkBox_2.setText(_translate("Dialog", "¿Posee Plan de Telefonía?"))
        self.label_2.setText(_translate("Dialog", "Plan de internet"))
        self.combo_internet_hfc.setItemText(0, _translate("Dialog", "Seleccione"))
        self.tabWidgetTicketsHfcTv.setTabText(self.tabWidgetTicketsHfcTv.indexOf(self.tab), _translate("Dialog", "Tickets de ventas"))
        self.btn_ticket_hfc_tv_support.setText(_translate("Dialog", "Generar Ticket"))
        self.btn_clear_hfc_tv_support.setText(_translate("Dialog", "Limpiar"))
        self.label_4.setText(_translate("Dialog", "Ticket Abonado"))
        self.label_9.setText(_translate("Dialog", "Ticket K2B"))
        self.groupBox_6.setTitle(_translate("Dialog", "Falla presentada cable"))
        self.hfc_tv_cable_failure.setItemText(0, _translate("Dialog", "Seleccione la falla"))
        self.hfc_tv_cable_failure.setItemText(1, _translate("Dialog", "Sin señal en todos los canales"))
        self.hfc_tv_cable_failure.setItemText(2, _translate("Dialog", "Señal Pixelada"))
        self.hfc_tv_cable_failure.setItemText(3, _translate("Dialog", "Señal lluviosa "))
        self.hfc_tv_cable_failure.setItemText(4, _translate("Dialog", "Falla algunos canales"))
        self.groupBox_7.setTitle(_translate("Dialog", "Motivos a usar"))
        self.hfc_tv_motive.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox_9.setTitle(_translate("Dialog", "Soporte Brindado"))
        self.hfc_tv_successful_support.setText(_translate("Dialog", "Soporte exitoso"))
        self.hfc_tv_unsuccessful_support.setText(_translate("Dialog", "Soporte sin éxitos (service)"))
        self.hfc_tv_connect_disconect.setText(_translate("Dialog", "Conecta / Desconecta"))
        self.hfc_tv_connections_ok.setText(_translate("Dialog", "Conexiones OK"))
        self.tabWidgetTicketsHfcTv.setTabText(self.tabWidgetTicketsHfcTv.indexOf(self.tab_2), _translate("Dialog", "Tickets de soportes TV Cable"))
        self.groupBox_4.setTitle(_translate("Dialog", "Comandos Enviados"))
        self.dth_coomand_not_send.setText(_translate("Dialog", "No se envian comandos"))
        self.dth_refresh.setText(_translate("Dialog", "Refresh"))
        self.label.setText(_translate("Dialog", "Accion"))
        self.combo_dth_command.setItemText(0, _translate("Dialog", "(Ninguno)"))
        self.combo_dth_command.setItemText(1, _translate("Dialog", "Initialize"))
        self.combo_dth_command.setItemText(2, _translate("Dialog", "Boot Dhct"))
        self.combo_dth_command.setItemText(3, _translate("Dialog", "Cold Initialize"))
        self.combo_dth_command.setItemText(4, _translate("Dialog", "Clear Parental Lock"))
        self.combo_dth_command.setItemText(5, _translate("Dialog", "Clear PIN"))
        self.combo_dth_command.setItemText(6, _translate("Dialog", "Dhct Instant Hit"))
        self.combo_dth_command.setItemText(7, _translate("Dialog", "Reset Client Nvm"))
        self.combo_dth_command.setItemText(8, _translate("Dialog", "Set Default Pin"))
        self.combo_dth_command.setItemText(9, _translate("Dialog", "Admin Status"))
        self.groupBox_5.setTitle(_translate("Dialog", "Decoder"))
        self.btn_add_decoder_dth.setToolTip(_translate("Dialog", "Agregar decodificador"))
        self.btn_remove_decoder_dth.setToolTip(_translate("Dialog", "Eliminar decodificador de la lista"))
        self.groupBox_10.setTitle(_translate("Dialog", "Falla presentada Decodificador"))
        self.combo_dth_failure_2.setItemText(0, _translate("Dialog", "Seleccione Falla"))
        self.combo_dth_failure_2.setItemText(1, _translate("Dialog", "Pantalla negra todos los canales"))
        self.combo_dth_failure_2.setItemText(2, _translate("Dialog", "Pantalla negra algunos canales"))
        self.combo_dth_failure_2.setItemText(3, _translate("Dialog", "Sin Opciones de Menu"))
        self.combo_dth_failure_2.setItemText(4, _translate("Dialog", "NO AUTORIZADO (LLAMAR AL 0-500)TODOS LOS CANALES"))
        self.combo_dth_failure_2.setItemText(5, _translate("Dialog", "NO AUTORIZADO (LLAMAR AL 0-500) ALGUNOS CANALES"))
        self.combo_dth_failure_2.setItemText(6, _translate("Dialog", "LLAMAR AL 0500 TODOS LOS CANALES "))
        self.combo_dth_failure_2.setItemText(7, _translate("Dialog", "LLAMAR AL 0500 ALGUNOS CANALES"))
        self.combo_dth_failure_2.setItemText(8, _translate("Dialog", "ERROR 98"))
        self.combo_dth_failure_2.setItemText(9, _translate("Dialog", "PANTALLA GRIS-BLANCO-VINOTINTO (SERVICIO NO DISPONIBLE)"))
        self.combo_dth_failure_2.setItemText(10, _translate("Dialog", "PANTALLA AZUL"))
        self.combo_dth_failure_2.setItemText(11, _translate("Dialog", "SEÑALES DEBILES O INEXISTENTES"))
        self.combo_dth_failure_2.setItemText(12, _translate("Dialog", "PANTALLA RAYADA"))
        self.combo_dth_failure_2.setItemText(13, _translate("Dialog", "SERVICIO NO DISPONIBLE"))
        self.combo_dth_failure_2.setItemText(14, _translate("Dialog", "SERVICIO INTERRUMPIDO TEMPORALMENTE"))
        self.combo_dth_failure_2.setItemText(15, _translate("Dialog", "New Item"))
        self.combo_dth_failure_2.setItemText(16, _translate("Dialog", "SALTO DE CANALES (CAJAS DTA / iDTA)"))
        self.combo_dth_failure_2.setItemText(17, _translate("Dialog", "PIN BLOQUEADO"))
        self.combo_dth_failure_2.setItemText(18, _translate("Dialog", "REINICIO CONSTANTE"))
        self.combo_dth_failure_2.setItemText(19, _translate("Dialog", "NO DATA Barra Informativa"))
        self.combo_dth_failure_2.setItemText(20, _translate("Dialog", "CISCO SIN SEÑAL"))
        self.combo_dth_failure_2.setItemText(21, _translate("Dialog", "NO INICIALIZA"))
        self.combo_dth_failure_2.setItemText(22, _translate("Dialog", "VR-07 (FRONTAL DE CD) PANTALLA EN NEGRO"))
        self.combo_dth_failure_2.setItemText(23, _translate("Dialog", "E11 (FRONTAL DE CD) PANTALLA EN BLANCO"))
        self.groupBox_11.setTitle(_translate("Dialog", "Envio de Comandos"))
        self.hfc_tv_commands_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox_12.setTitle(_translate("Dialog", "Motivos a usar"))
        self.hfc_tv_motive_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "Ticket Abonado"))
        self.label_10.setText(_translate("Dialog", "Ticket K2B"))
        self.btn_clear_dth__support_2.setText(_translate("Dialog", "Limpiar"))
        self.btn_ticket_dth_support_2.setText(_translate("Dialog", "Generar Ticket"))
        self.groupBox_13.setTitle(_translate("Dialog", "Falla presentada Decodificador (Analógico)"))
        self.combo_dth_failure_3.setItemText(0, _translate("Dialog", "Seleccione Falla"))
        self.combo_dth_failure_3.setItemText(1, _translate("Dialog", "PANTALLA NEGRA"))
        self.combo_dth_failure_3.setItemText(2, _translate("Dialog", "PANTALLA AZUL"))
        self.combo_dth_failure_3.setItemText(3, _translate("Dialog", "NO INICIALIZA"))
        self.combo_dth_failure_3.setItemText(4, _translate("Dialog", "SISTEMA DE DECODIFICACIONES CACERAS"))
        self.combo_dth_failure_3.setItemText(5, _translate("Dialog", "CANAL NO AUTORIZADO"))
        self.combo_dth_failure_3.setItemText(6, _translate("Dialog", "CANALES BLOQUEADOS POR SEGURIDAD"))
        self.combo_dth_failure_3.setItemText(7, _translate("Dialog", "CAJA BLOQUEADA FUE ABIERTA SIN AUTORIZACION"))
        self.combo_dth_failure_3.setItemText(8, _translate("Dialog", "HOME TERMINAL RECIEVE DATA"))
        self.combo_dth_failure_3.setItemText(9, _translate("Dialog", "L-01"))
        self.combo_dth_failure_3.setItemText(10, _translate("Dialog", "CANALES BLOQUEADOS POR SEGURIDAD"))
        self.groupBox_14.setTitle(_translate("Dialog", "Soporte Brindado"))
        self.dth_successful_support_2.setText(_translate("Dialog", "Soporte exitoso"))
        self.dth_unsuccessful_support_2.setText(_translate("Dialog", "Soporte sin éxitos (service)"))
        self.dth_connections_ok_2.setText(_translate("Dialog", "Conexiones OK"))
        self.dth_not_manupulate_ant_2.setText(_translate("Dialog", "Conecta / Desconecta"))
        self.tabWidgetTicketsHfcTv.setTabText(self.tabWidgetTicketsHfcTv.indexOf(self.tab_3), _translate("Dialog", "Tickets Soportes Cajas Digitales / Decodificadores"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
