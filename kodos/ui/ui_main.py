# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created: Wed Oct  6 18:14:32 2010
#      by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(698, 660)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.regexText = QtGui.QPlainTextEdit(self.groupBox)
        self.regexText.setObjectName("regexText")
        self.verticalLayout_3.addWidget(self.regexText)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ignoreCaseFlag = QtGui.QCheckBox(self.groupBox_2)
        self.ignoreCaseFlag.setObjectName("ignoreCaseFlag")
        self.horizontalLayout_2.addWidget(self.ignoreCaseFlag)
        self.multiLineFlag = QtGui.QCheckBox(self.groupBox_2)
        self.multiLineFlag.setObjectName("multiLineFlag")
        self.horizontalLayout_2.addWidget(self.multiLineFlag)
        self.dotAllFlag = QtGui.QCheckBox(self.groupBox_2)
        self.dotAllFlag.setObjectName("dotAllFlag")
        self.horizontalLayout_2.addWidget(self.dotAllFlag)
        self.verboseFlag = QtGui.QCheckBox(self.groupBox_2)
        self.verboseFlag.setObjectName("verboseFlag")
        self.horizontalLayout_2.addWidget(self.verboseFlag)
        self.localeFlag = QtGui.QCheckBox(self.groupBox_2)
        self.localeFlag.setObjectName("localeFlag")
        self.horizontalLayout_2.addWidget(self.localeFlag)
        self.unicodeFlag = QtGui.QCheckBox(self.groupBox_2)
        self.unicodeFlag.setObjectName("unicodeFlag")
        self.horizontalLayout_2.addWidget(self.unicodeFlag)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.tabWidget_2 = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.tab_6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.searchText = QtGui.QPlainTextEdit(self.tab_6)
        self.searchText.setObjectName("searchText")
        self.verticalLayout_11.addWidget(self.searchText)
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.tab_7)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.replaceText = QtGui.QPlainTextEdit(self.tab_7)
        self.replaceText.setObjectName("replaceText")
        self.verticalLayout_12.addWidget(self.replaceText)
        self.tabWidget_2.addTab(self.tab_7, "")
        self.verticalLayout.addWidget(self.tabWidget_2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.matchNumberBox = QtGui.QSpinBox(self.centralwidget)
        self.matchNumberBox.setObjectName("matchNumberBox")
        self.horizontalLayout.addWidget(self.matchNumberBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupsView = QtGui.QTableView(self.tab)
        self.groupsView.setObjectName("groupsView")
        self.verticalLayout_6.addWidget(self.groupsView)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.matchText = QtGui.QPlainTextEdit(self.tab_2)
        self.matchText.setReadOnly(True)
        self.matchText.setObjectName("matchText")
        self.verticalLayout_7.addWidget(self.matchText)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.matchAllText = QtGui.QPlainTextEdit(self.tab_3)
        self.matchAllText.setReadOnly(True)
        self.matchAllText.setObjectName("matchAllText")
        self.verticalLayout_8.addWidget(self.matchAllText)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.replaceResultText = QtGui.QPlainTextEdit(self.tab_4)
        self.replaceResultText.setReadOnly(True)
        self.replaceResultText.setObjectName("replaceResultText")
        self.verticalLayout_9.addWidget(self.replaceResultText)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.tab_5)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.sampleText = QtGui.QPlainTextEdit(self.tab_5)
        self.sampleText.setReadOnly(True)
        self.sampleText.setObjectName("sampleText")
        self.verticalLayout_10.addWidget(self.sampleText)
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 698, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self._statusbar = QtGui.QStatusBar(MainWindow)
        self._statusbar.setObjectName("_statusbar")
        MainWindow.setStatusBar(self._statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.action_New = QtGui.QAction(MainWindow)
        self.action_New.setObjectName("action_New")
        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Save = QtGui.QAction(MainWindow)
        self.action_Save.setObjectName("action_Save")
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionRevert_Kodos_File = QtGui.QAction(MainWindow)
        self.actionRevert_Kodos_File.setObjectName("actionRevert_Kodos_File")
        self.actionImport_File = QtGui.QAction(MainWindow)
        self.actionImport_File.setObjectName("actionImport_File")
        self.actionIport_URL = QtGui.QAction(MainWindow)
        self.actionIport_URL.setObjectName("actionIport_URL")
        self.action_Exit = QtGui.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.action_Undo = QtGui.QAction(MainWindow)
        self.action_Undo.setObjectName("action_Undo")
        self.action_Redo = QtGui.QAction(MainWindow)
        self.action_Redo.setObjectName("action_Redo")
        self.action_Cut = QtGui.QAction(MainWindow)
        self.action_Cut.setObjectName("action_Cut")
        self.actionC_opy = QtGui.QAction(MainWindow)
        self.actionC_opy.setObjectName("actionC_opy")
        self.action_Paste = QtGui.QAction(MainWindow)
        self.action_Paste.setObjectName("action_Paste")
        self.action_Examine_Regex = QtGui.QAction(MainWindow)
        self.action_Examine_Regex.setObjectName("action_Examine_Regex")
        self.action_Pause_Processing = QtGui.QAction(MainWindow)
        self.action_Pause_Processing.setObjectName("action_Pause_Processing")
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionPython_Regex_Help = QtGui.QAction(MainWindow)
        self.actionPython_Regex_Help.setObjectName("actionPython_Regex_Help")
        self.actionRegex_Reference_Guide = QtGui.QAction(MainWindow)
        self.actionRegex_Reference_Guide.setObjectName("actionRegex_Reference_Guide")
        self.actionRegex_Library = QtGui.QAction(MainWindow)
        self.actionRegex_Library.setObjectName("actionRegex_Library")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menu_File.addAction(self.action_New)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.actionSave_As)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionRevert_Kodos_File)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionImport_File)
        self.menu_File.addAction(self.actionIport_URL)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)
        self.menu_Edit.addAction(self.action_Undo)
        self.menu_Edit.addAction(self.action_Redo)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_Cut)
        self.menu_Edit.addAction(self.actionC_opy)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_Examine_Regex)
        self.menu_Edit.addAction(self.action_Pause_Processing)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.actionPreferences)
        self.menu_Help.addAction(self.actionHelp)
        self.menu_Help.addAction(self.actionPython_Regex_Help)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.actionRegex_Reference_Guide)
        self.menu_Help.addAction(self.actionRegex_Library)
        self.menu_Help.addSeparator()
        self.menu_Help.addAction(self.actionAbout)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.action_Open)
        self.toolBar.addAction(self.action_Save)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Cut)
        self.toolBar.addAction(self.actionC_opy)
        self.toolBar.addAction(self.action_Paste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_Pause_Processing)
        self.toolBar.addAction(self.action_Examine_Regex)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRegex_Reference_Guide)
        self.toolBar.addAction(self.actionRegex_Library)

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Regular Expression Pattern", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Flags", None, QtGui.QApplication.UnicodeUTF8))
        self.ignoreCaseFlag.setText(QtGui.QApplication.translate("MainWindow", "Ignore Case", None, QtGui.QApplication.UnicodeUTF8))
        self.multiLineFlag.setText(QtGui.QApplication.translate("MainWindow", "Multi Line", None, QtGui.QApplication.UnicodeUTF8))
        self.dotAllFlag.setText(QtGui.QApplication.translate("MainWindow", "Dot All", None, QtGui.QApplication.UnicodeUTF8))
        self.verboseFlag.setText(QtGui.QApplication.translate("MainWindow", "Verbose", None, QtGui.QApplication.UnicodeUTF8))
        self.localeFlag.setText(QtGui.QApplication.translate("MainWindow", "Locale", None, QtGui.QApplication.UnicodeUTF8))
        self.unicodeFlag.setText(QtGui.QApplication.translate("MainWindow", "Unicode", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QtGui.QApplication.translate("MainWindow", "Search String", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QtGui.QApplication.translate("MainWindow", "Replace String", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Match Number", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Group", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Match", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Match All", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("MainWindow", "Sample Code", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Save.setText(QtGui.QApplication.translate("MainWindow", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setText(QtGui.QApplication.translate("MainWindow", "Save &As...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRevert_Kodos_File.setText(QtGui.QApplication.translate("MainWindow", "&Revert Kodos File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport_File.setText(QtGui.QApplication.translate("MainWindow", "Import &File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIport_URL.setText(QtGui.QApplication.translate("MainWindow", "Import &URL", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Exit.setText(QtGui.QApplication.translate("MainWindow", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Undo.setText(QtGui.QApplication.translate("MainWindow", "&Undo", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Redo.setText(QtGui.QApplication.translate("MainWindow", "&Redo", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Cut.setText(QtGui.QApplication.translate("MainWindow", "&Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionC_opy.setText(QtGui.QApplication.translate("MainWindow", "C&opy", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Paste.setText(QtGui.QApplication.translate("MainWindow", "&Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Examine_Regex.setText(QtGui.QApplication.translate("MainWindow", "&Examine Regex", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Pause_Processing.setText(QtGui.QApplication.translate("MainWindow", "Pause Processing", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPython_Regex_Help.setText(QtGui.QApplication.translate("MainWindow", "&Python Regex Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRegex_Reference_Guide.setText(QtGui.QApplication.translate("MainWindow", "&Regex Reference Guide", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRegex_Library.setText(QtGui.QApplication.translate("MainWindow", "Regex &Library", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))

