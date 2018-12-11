# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 516)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plotScrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.plotScrollArea.setWidgetResizable(True)
        self.plotScrollArea.setObjectName("plotScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 774, 447))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.plotScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.plotScrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSave_Selections_As_2 = QtWidgets.QMenu(self.menuFile)
        self.menuSave_Selections_As_2.setObjectName("menuSave_Selections_As_2")
        self.menuPlot = QtWidgets.QMenu(self.menubar)
        self.menuPlot.setObjectName("menuPlot")
        self.menuHistogram_Bar = QtWidgets.QMenu(self.menuPlot)
        self.menuHistogram_Bar.setObjectName("menuHistogram_Bar")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_List = QtWidgets.QAction(MainWindow)
        self.actionSave_List.setObjectName("actionSave_List")
        self.actionSave_Stream = QtWidgets.QAction(MainWindow)
        self.actionSave_Stream.setObjectName("actionSave_Stream")
        self.actionSave_Dat = QtWidgets.QAction(MainWindow)
        self.actionSave_Dat.setObjectName("actionSave_Dat")
        self.actionSave_Plot = QtWidgets.QAction(MainWindow)
        self.actionSave_Plot.setObjectName("actionSave_Plot")
        self.actionScatter = QtWidgets.QAction(MainWindow)
        self.actionScatter.setObjectName("actionScatter")
        self.action2D_Histogram = QtWidgets.QAction(MainWindow)
        self.action2D_Histogram.setObjectName("action2D_Histogram")
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionSave_Filters = QtWidgets.QAction(MainWindow)
        self.actionSave_Filters.setObjectName("actionSave_Filters")
        self.actionSave_Numpy = QtWidgets.QAction(MainWindow)
        self.actionSave_Numpy.setObjectName("actionSave_Numpy")
        self.actionItem_Viewer = QtWidgets.QAction(MainWindow)
        self.actionItem_Viewer.setObjectName("actionItem_Viewer")
        self.actionPixel = QtWidgets.QAction(MainWindow)
        self.actionPixel.setObjectName("actionPixel")
        self.actionViewControls = QtWidgets.QAction(MainWindow)
        self.actionViewControls.setObjectName("actionViewControls")
        self.actionAggregated_Plot = QtWidgets.QAction(MainWindow)
        self.actionAggregated_Plot.setObjectName("actionAggregated_Plot")
        self.actionComparison_Scatter = QtWidgets.QAction(MainWindow)
        self.actionComparison_Scatter.setObjectName("actionComparison_Scatter")
        self.actionComparison_2D_Histogram = QtWidgets.QAction(MainWindow)
        self.actionComparison_2D_Histogram.setObjectName("actionComparison_2D_Histogram")
        self.menuSave_Selections_As_2.addAction(self.actionSave_List)
        self.menuSave_Selections_As_2.addAction(self.actionSave_Stream)
        self.menuSave_Selections_As_2.addAction(self.actionSave_Dat)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuSave_Selections_As_2.menuAction())
        self.menuFile.addAction(self.actionSave_Numpy)
        self.menuFile.addAction(self.actionSave_Plot)
        self.menuFile.addAction(self.actionSave_Filters)
        self.menuHistogram_Bar.addAction(self.actionReset)
        self.menuPlot.addAction(self.menuHistogram_Bar.menuAction())
        self.menuPlot.addAction(self.actionScatter)
        self.menuPlot.addAction(self.actionComparison_Scatter)
        self.menuPlot.addAction(self.action2D_Histogram)
        self.menuPlot.addAction(self.actionComparison_2D_Histogram)
        self.menuPlot.addAction(self.actionPixel)
        self.menuPlot.addAction(self.actionAggregated_Plot)
        self.menuView.addAction(self.actionItem_Viewer)
        self.menuView.addAction(self.actionViewControls)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPlot.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Viewer"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSave_Selections_As_2.setTitle(_translate("MainWindow", "Save Selections As"))
        self.menuPlot.setTitle(_translate("MainWindow", "Plot"))
        self.menuHistogram_Bar.setTitle(_translate("MainWindow", "Histogram / Bar"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_List.setText(_translate("MainWindow", "CrystFEL List"))
        self.actionSave_Stream.setText(_translate("MainWindow", "Stream File"))
        self.actionSave_Dat.setText(_translate("MainWindow", "Dat File"))
        self.actionSave_Plot.setText(_translate("MainWindow", "Save Plot"))
        self.actionScatter.setText(_translate("MainWindow", "Scatter"))
        self.action2D_Histogram.setText(_translate("MainWindow", "2D Histogram"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionSave_Filters.setText(_translate("MainWindow", "Save Filters"))
        self.actionSave_Numpy.setText(_translate("MainWindow", "Save Numpy"))
        self.actionSave_Numpy.setToolTip(_translate("MainWindow", "Save all data into compressed npz file"))
        self.actionItem_Viewer.setText(_translate("MainWindow", "Item Viewer"))
        self.actionPixel.setText(_translate("MainWindow", "Pixel Plot"))
        self.actionPixel.setWhatsThis(_translate("MainWindow", "Also called chip plot. Color pixels by field value, pixels by real space coordinates."))
        self.actionViewControls.setText(_translate("MainWindow", "Controls"))
        self.actionAggregated_Plot.setText(_translate("MainWindow", "Aggregated Plot"))
        self.actionComparison_Scatter.setText(_translate("MainWindow", "Comparison Scatter"))
        self.actionComparison_2D_Histogram.setText(_translate("MainWindow", "Comparison 2D Histogram"))

