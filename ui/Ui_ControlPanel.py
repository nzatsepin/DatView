# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ControlPanel.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ControlPanel(object):
    def setupUi(self, ControlPanel):
        ControlPanel.setObjectName(_fromUtf8("ControlPanel"))
        ControlPanel.resize(343, 480)
        self.gridLayout = QtGui.QGridLayout(ControlPanel)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(ControlPanel)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 326, 1266))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.sortGroupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.sortGroupBox.setObjectName(_fromUtf8("sortGroupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.sortGroupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.sortGroupBox)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.sortAscendingCheckBox = QtGui.QCheckBox(self.sortGroupBox)
        self.sortAscendingCheckBox.setChecked(True)
        self.sortAscendingCheckBox.setObjectName(_fromUtf8("sortAscendingCheckBox"))
        self.verticalLayout_2.addWidget(self.sortAscendingCheckBox)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.addSortField = QtGui.QToolButton(self.sortGroupBox)
        self.addSortField.setPopupMode(QtGui.QToolButton.InstantPopup)
        self.addSortField.setObjectName(_fromUtf8("addSortField"))
        self.horizontalLayout_2.addWidget(self.addSortField)
        self.removeSortField = QtGui.QToolButton(self.sortGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeSortField.sizePolicy().hasHeightForWidth())
        self.removeSortField.setSizePolicy(sizePolicy)
        self.removeSortField.setObjectName(_fromUtf8("removeSortField"))
        self.horizontalLayout_2.addWidget(self.removeSortField)
        self.moveSortField = QtGui.QToolButton(self.sortGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.moveSortField.sizePolicy().hasHeightForWidth())
        self.moveSortField.setSizePolicy(sizePolicy)
        self.moveSortField.setObjectName(_fromUtf8("moveSortField"))
        self.horizontalLayout_2.addWidget(self.moveSortField)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.sortByListWidget = QtGui.QListWidget(self.sortGroupBox)
        self.sortByListWidget.setObjectName(_fromUtf8("sortByListWidget"))
        self.verticalLayout_2.addWidget(self.sortByListWidget)
        self.verticalLayout_7.addWidget(self.sortGroupBox)
        self.flaggedBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.flaggedBox.setObjectName(_fromUtf8("flaggedBox"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.flaggedBox)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_12 = QtGui.QLabel(self.flaggedBox)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_5.addWidget(self.label_12)
        self.flagExclude = QtGui.QRadioButton(self.flaggedBox)
        self.flagExclude.setObjectName(_fromUtf8("flagExclude"))
        self.verticalLayout_5.addWidget(self.flagExclude)
        self.flagKeep = QtGui.QRadioButton(self.flaggedBox)
        self.flagKeep.setObjectName(_fromUtf8("flagKeep"))
        self.verticalLayout_5.addWidget(self.flagKeep)
        self.flagIgnore = QtGui.QRadioButton(self.flaggedBox)
        self.flagIgnore.setChecked(True)
        self.flagIgnore.setObjectName(_fromUtf8("flagIgnore"))
        self.verticalLayout_5.addWidget(self.flagIgnore)
        self.label_11 = QtGui.QLabel(self.flaggedBox)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_5.addWidget(self.label_11)
        self.flaggedList = QtGui.QListView(self.flaggedBox)
        self.flaggedList.setObjectName(_fromUtf8("flaggedList"))
        self.verticalLayout_5.addWidget(self.flaggedList)
        self.verticalLayout_7.addWidget(self.flaggedBox)
        self.limitCheckBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.limitCheckBox.setCheckable(True)
        self.limitCheckBox.setChecked(False)
        self.limitCheckBox.setObjectName(_fromUtf8("limitCheckBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.limitCheckBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.limitCheckBox)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.limitSpinBox = QtGui.QSpinBox(self.limitCheckBox)
        self.limitSpinBox.setProperty("showGroupSeparator", True)
        self.limitSpinBox.setMaximum(999999)
        self.limitSpinBox.setSingleStep(100)
        self.limitSpinBox.setProperty("value", 20000)
        self.limitSpinBox.setObjectName(_fromUtf8("limitSpinBox"))
        self.verticalLayout.addWidget(self.limitSpinBox)
        self.limRandomButton = QtGui.QRadioButton(self.limitCheckBox)
        self.limRandomButton.setChecked(True)
        self.limRandomButton.setObjectName(_fromUtf8("limRandomButton"))
        self.verticalLayout.addWidget(self.limRandomButton)
        self.limTopButton = QtGui.QRadioButton(self.limitCheckBox)
        self.limTopButton.setObjectName(_fromUtf8("limTopButton"))
        self.verticalLayout.addWidget(self.limTopButton)
        self.verticalLayout_7.addWidget(self.limitCheckBox)
        self.filtersBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.filtersBox.setObjectName(_fromUtf8("filtersBox"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.filtersBox)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_13 = QtGui.QLabel(self.filtersBox)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_6.addWidget(self.label_13)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.saveFiltersButton = QtGui.QPushButton(self.filtersBox)
        self.saveFiltersButton.setObjectName(_fromUtf8("saveFiltersButton"))
        self.horizontalLayout_11.addWidget(self.saveFiltersButton)
        self.loadFiltersButton = QtGui.QPushButton(self.filtersBox)
        self.loadFiltersButton.setObjectName(_fromUtf8("loadFiltersButton"))
        self.horizontalLayout_11.addWidget(self.loadFiltersButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.filterTreeView = QtGui.QTreeView(self.filtersBox)
        self.filterTreeView.setObjectName(_fromUtf8("filterTreeView"))
        self.filterTreeView.header().setVisible(False)
        self.verticalLayout_6.addWidget(self.filterTreeView)
        self.verticalLayout_7.addWidget(self.filtersBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(ControlPanel)
        QtCore.QMetaObject.connectSlotsByName(ControlPanel)

    def retranslateUi(self, ControlPanel):
        ControlPanel.setWindowTitle(_translate("ControlPanel", "Controls", None))
        self.sortGroupBox.setTitle(_translate("ControlPanel", "Sort", None))
        self.label.setText(_translate("ControlPanel", "Changes current sort order field and output sort order. Use ^ to move selected field up.", None))
        self.sortAscendingCheckBox.setText(_translate("ControlPanel", "Ascending", None))
        self.addSortField.setToolTip(_translate("ControlPanel", "Add Field", None))
        self.addSortField.setText(_translate("ControlPanel", "+", None))
        self.removeSortField.setToolTip(_translate("ControlPanel", "Remove selected field", None))
        self.removeSortField.setText(_translate("ControlPanel", "-", None))
        self.moveSortField.setToolTip(_translate("ControlPanel", "Move selected field up", None))
        self.moveSortField.setText(_translate("ControlPanel", "^", None))
        self.flaggedBox.setTitle(_translate("ControlPanel", "Flagged Items", None))
        self.label_12.setText(_translate("ControlPanel", "Items are flagged in the item viewer. Use radio buttons to control how flagged items change current selection. Select flagged items from the list to jump to that item in the viewer.", None))
        self.flagExclude.setText(_translate("ControlPanel", "Exclude From Selection", None))
        self.flagKeep.setText(_translate("ControlPanel", "Keep Only Flagged Items", None))
        self.flagIgnore.setText(_translate("ControlPanel", "Ignore", None))
        self.label_11.setText(_translate("ControlPanel", "Currently Flagged:", None))
        self.limitCheckBox.setTitle(_translate("ControlPanel", "Limit Output", None))
        self.label_2.setText(_translate("ControlPanel", "Limit number output. Take either random subset of selection or the first (top) N patterns", None))
        self.limRandomButton.setText(_translate("ControlPanel", "Random Subset", None))
        self.limTopButton.setText(_translate("ControlPanel", "Top", None))
        self.filtersBox.setTitle(_translate("ControlPanel", "Filters", None))
        self.label_13.setText(_translate("ControlPanel", "Filters controlling current selection. Checked filters are active. Click to edit values.", None))
        self.saveFiltersButton.setText(_translate("ControlPanel", "Save", None))
        self.loadFiltersButton.setText(_translate("ControlPanel", "Load", None))
