# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ControlPanel.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ControlPanel(object):
    def setupUi(self, ControlPanel):
        ControlPanel.setObjectName("ControlPanel")
        ControlPanel.resize(343, 480)
        self.gridLayout = QtWidgets.QGridLayout(ControlPanel)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(ControlPanel)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 326, 1266))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.sortGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.sortGroupBox.setObjectName("sortGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.sortGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.sortGroupBox)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.sortAscendingCheckBox = QtWidgets.QCheckBox(self.sortGroupBox)
        self.sortAscendingCheckBox.setChecked(True)
        self.sortAscendingCheckBox.setObjectName("sortAscendingCheckBox")
        self.verticalLayout_2.addWidget(self.sortAscendingCheckBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addSortField = QtWidgets.QToolButton(self.sortGroupBox)
        self.addSortField.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.addSortField.setObjectName("addSortField")
        self.horizontalLayout_2.addWidget(self.addSortField)
        self.removeSortField = QtWidgets.QToolButton(self.sortGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeSortField.sizePolicy().hasHeightForWidth())
        self.removeSortField.setSizePolicy(sizePolicy)
        self.removeSortField.setObjectName("removeSortField")
        self.horizontalLayout_2.addWidget(self.removeSortField)
        self.moveSortField = QtWidgets.QToolButton(self.sortGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.moveSortField.sizePolicy().hasHeightForWidth())
        self.moveSortField.setSizePolicy(sizePolicy)
        self.moveSortField.setObjectName("moveSortField")
        self.horizontalLayout_2.addWidget(self.moveSortField)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.sortByListWidget = QtWidgets.QListWidget(self.sortGroupBox)
        self.sortByListWidget.setObjectName("sortByListWidget")
        self.verticalLayout_2.addWidget(self.sortByListWidget)
        self.verticalLayout_7.addWidget(self.sortGroupBox)
        self.flaggedBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.flaggedBox.setObjectName("flaggedBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.flaggedBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_12 = QtWidgets.QLabel(self.flaggedBox)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_5.addWidget(self.label_12)
        self.flagExclude = QtWidgets.QRadioButton(self.flaggedBox)
        self.flagExclude.setObjectName("flagExclude")
        self.verticalLayout_5.addWidget(self.flagExclude)
        self.flagKeep = QtWidgets.QRadioButton(self.flaggedBox)
        self.flagKeep.setObjectName("flagKeep")
        self.verticalLayout_5.addWidget(self.flagKeep)
        self.flagIgnore = QtWidgets.QRadioButton(self.flaggedBox)
        self.flagIgnore.setChecked(True)
        self.flagIgnore.setObjectName("flagIgnore")
        self.verticalLayout_5.addWidget(self.flagIgnore)
        self.label_11 = QtWidgets.QLabel(self.flaggedBox)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_5.addWidget(self.label_11)
        self.flaggedList = QtWidgets.QListView(self.flaggedBox)
        self.flaggedList.setObjectName("flaggedList")
        self.verticalLayout_5.addWidget(self.flaggedList)
        self.verticalLayout_7.addWidget(self.flaggedBox)
        self.limitCheckBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.limitCheckBox.setCheckable(True)
        self.limitCheckBox.setChecked(False)
        self.limitCheckBox.setObjectName("limitCheckBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.limitCheckBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.limitCheckBox)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.limitSpinBox = QtWidgets.QSpinBox(self.limitCheckBox)
        self.limitSpinBox.setProperty("showGroupSeparator", True)
        self.limitSpinBox.setMaximum(999999)
        self.limitSpinBox.setSingleStep(100)
        self.limitSpinBox.setProperty("value", 20000)
        self.limitSpinBox.setObjectName("limitSpinBox")
        self.verticalLayout.addWidget(self.limitSpinBox)
        self.limRandomButton = QtWidgets.QRadioButton(self.limitCheckBox)
        self.limRandomButton.setChecked(True)
        self.limRandomButton.setObjectName("limRandomButton")
        self.verticalLayout.addWidget(self.limRandomButton)
        self.limTopButton = QtWidgets.QRadioButton(self.limitCheckBox)
        self.limTopButton.setObjectName("limTopButton")
        self.verticalLayout.addWidget(self.limTopButton)
        self.verticalLayout_7.addWidget(self.limitCheckBox)
        self.filtersBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.filtersBox.setObjectName("filtersBox")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.filtersBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_13 = QtWidgets.QLabel(self.filtersBox)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_6.addWidget(self.label_13)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.saveFiltersButton = QtWidgets.QPushButton(self.filtersBox)
        self.saveFiltersButton.setObjectName("saveFiltersButton")
        self.horizontalLayout_11.addWidget(self.saveFiltersButton)
        self.loadFiltersButton = QtWidgets.QPushButton(self.filtersBox)
        self.loadFiltersButton.setObjectName("loadFiltersButton")
        self.horizontalLayout_11.addWidget(self.loadFiltersButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.filterTreeView = QtWidgets.QTreeView(self.filtersBox)
        self.filterTreeView.setObjectName("filterTreeView")
        self.filterTreeView.header().setVisible(False)
        self.verticalLayout_6.addWidget(self.filterTreeView)
        self.verticalLayout_7.addWidget(self.filtersBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(ControlPanel)
        QtCore.QMetaObject.connectSlotsByName(ControlPanel)

    def retranslateUi(self, ControlPanel):
        _translate = QtCore.QCoreApplication.translate
        ControlPanel.setWindowTitle(_translate("ControlPanel", "Controls"))
        self.sortGroupBox.setTitle(_translate("ControlPanel", "Sort"))
        self.label.setText(_translate("ControlPanel", "Changes current sort order field and output sort order. Use ^ to move selected field up."))
        self.sortAscendingCheckBox.setText(_translate("ControlPanel", "Ascending"))
        self.addSortField.setToolTip(_translate("ControlPanel", "Add Field"))
        self.addSortField.setText(_translate("ControlPanel", "+"))
        self.removeSortField.setToolTip(_translate("ControlPanel", "Remove selected field"))
        self.removeSortField.setText(_translate("ControlPanel", "-"))
        self.moveSortField.setToolTip(_translate("ControlPanel", "Move selected field up"))
        self.moveSortField.setText(_translate("ControlPanel", "^"))
        self.flaggedBox.setTitle(_translate("ControlPanel", "Flagged Items"))
        self.label_12.setText(_translate("ControlPanel", "Items are flagged in the item viewer. Use radio buttons to control how flagged items change current selection. Select flagged items from the list to jump to that item in the viewer."))
        self.flagExclude.setText(_translate("ControlPanel", "Exclude From Selection"))
        self.flagKeep.setText(_translate("ControlPanel", "Keep Only Flagged Items"))
        self.flagIgnore.setText(_translate("ControlPanel", "Ignore"))
        self.label_11.setText(_translate("ControlPanel", "Currently Flagged:"))
        self.limitCheckBox.setTitle(_translate("ControlPanel", "Limit Output"))
        self.label_2.setText(_translate("ControlPanel", "Limit number output. Take either random subset of selection or the first (top) N patterns"))
        self.limRandomButton.setText(_translate("ControlPanel", "Random Subset"))
        self.limTopButton.setText(_translate("ControlPanel", "Top"))
        self.filtersBox.setTitle(_translate("ControlPanel", "Filters"))
        self.label_13.setText(_translate("ControlPanel", "Filters controlling current selection. Checked filters are active. Click to edit values."))
        self.saveFiltersButton.setText(_translate("ControlPanel", "Save"))
        self.loadFiltersButton.setText(_translate("ControlPanel", "Load"))

