# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manuskript/ui/exporters/exportersManager_ui.ui'
#
# Created: Fri Apr  8 12:47:11 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ExportersManager(object):
    def setupUi(self, ExportersManager):
        ExportersManager.setObjectName("ExportersManager")
        ExportersManager.resize(720, 548)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(ExportersManager)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lstExporters = QtWidgets.QListWidget(ExportersManager)
        self.lstExporters.setObjectName("lstExporters")
        item = QtWidgets.QListWidgetItem()
        self.lstExporters.addItem(item)
        self.horizontalLayout_8.addWidget(self.lstExporters)
        self.stack = QtWidgets.QWidget(ExportersManager)
        self.stack.setObjectName("stack")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.stack)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.lblExporterName = QtWidgets.QLabel(self.stack)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblExporterName.sizePolicy().hasHeightForWidth())
        self.lblExporterName.setSizePolicy(sizePolicy)
        self.lblExporterName.setStyleSheet("background-color:lightBlue;\n"
"border:none;\n"
"padding:10px;\n"
"color:darkBlue;\n"
"font-size:16px;\n"
"font-weight:bold;\n"
"text-align:center;")
        self.lblExporterName.setText("{Exporter Name}")
        self.lblExporterName.setAlignment(QtCore.Qt.AlignCenter)
        self.lblExporterName.setObjectName("lblExporterName")
        self.verticalLayout_7.addWidget(self.lblExporterName)
        self.grpDescription = QtWidgets.QGroupBox(self.stack)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.grpDescription.setFont(font)
        self.grpDescription.setObjectName("grpDescription")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.grpDescription)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lblExporterDescription = QtWidgets.QLabel(self.grpDescription)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lblExporterDescription.setFont(font)
        self.lblExporterDescription.setText("{ExporterDescription}")
        self.lblExporterDescription.setWordWrap(True)
        self.lblExporterDescription.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lblExporterDescription.setObjectName("lblExporterDescription")
        self.verticalLayout_5.addWidget(self.lblExporterDescription)
        self.verticalLayout_7.addWidget(self.grpDescription)
        self.grpExportTo = QtWidgets.QGroupBox(self.stack)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.grpExportTo.setFont(font)
        self.grpExportTo.setObjectName("grpExportTo")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.grpExportTo)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lstExportTo = QtWidgets.QListWidget(self.grpExportTo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lstExportTo.sizePolicy().hasHeightForWidth())
        self.lstExportTo.setSizePolicy(sizePolicy)
        self.lstExportTo.setObjectName("lstExportTo")
        self.horizontalLayout.addWidget(self.lstExportTo)
        self.frame = QtWidgets.QFrame(self.grpExportTo)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblExportToDescription = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lblExportToDescription.setFont(font)
        self.lblExportToDescription.setText("{FormatDescription}")
        self.lblExportToDescription.setWordWrap(True)
        self.lblExportToDescription.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lblExportToDescription.setObjectName("lblExportToDescription")
        self.verticalLayout.addWidget(self.lblExportToDescription)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_7.addWidget(self.grpExportTo)
        self.grpPath = QtWidgets.QGroupBox(self.stack)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.grpPath.setFont(font)
        self.grpPath.setObjectName("grpPath")
        self.formLayout = QtWidgets.QFormLayout(self.grpPath)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.grpPath)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lblStatus = QtWidgets.QLabel(self.grpPath)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lblStatus.setFont(font)
        self.lblStatus.setText("{ExporterStatus}")
        self.lblStatus.setObjectName("lblStatus")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lblStatus)
        self.lblVersionName = QtWidgets.QLabel(self.grpPath)
        self.lblVersionName.setObjectName("lblVersionName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblVersionName)
        self.lblVersion = QtWidgets.QLabel(self.grpPath)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lblVersion.setFont(font)
        self.lblVersion.setText("{ExporterVersion}")
        self.lblVersion.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lblVersion.setObjectName("lblVersion")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lblVersion)
        self.label = QtWidgets.QLabel(self.grpPath)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.txtPath = QtWidgets.QLineEdit(self.grpPath)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.txtPath.setFont(font)
        self.txtPath.setObjectName("txtPath")
        self.horizontalLayout_2.addWidget(self.txtPath)
        self.btnSetPath = QtWidgets.QPushButton(self.grpPath)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btnSetPath.setFont(font)
        self.btnSetPath.setObjectName("btnSetPath")
        self.horizontalLayout_2.addWidget(self.btnSetPath)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.lblHelpText = QtWidgets.QLabel(self.grpPath)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lblHelpText.setFont(font)
        self.lblHelpText.setWordWrap(True)
        self.lblHelpText.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lblHelpText.setObjectName("lblHelpText")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.lblHelpText)
        self.verticalLayout_7.addWidget(self.grpPath)
        self.horizontalLayout_8.addWidget(self.stack)

        self.retranslateUi(ExportersManager)
        QtCore.QMetaObject.connectSlotsByName(ExportersManager)

    def retranslateUi(self, ExportersManager):
        _translate = QtCore.QCoreApplication.translate
        ExportersManager.setWindowTitle(_translate("ExportersManager", "Manage Exporters"))
        __sortingEnabled = self.lstExporters.isSortingEnabled()
        self.lstExporters.setSortingEnabled(False)
        item = self.lstExporters.item(0)
        item.setText(_translate("ExportersManager", "Manuskript"))
        self.lstExporters.setSortingEnabled(__sortingEnabled)
        self.grpDescription.setTitle(_translate("ExportersManager", "Description"))
        self.grpExportTo.setTitle(_translate("ExportersManager", "Offers export to"))
        self.grpPath.setTitle(_translate("ExportersManager", "Status"))
        self.label_2.setText(_translate("ExportersManager", "Status:"))
        self.lblVersionName.setText(_translate("ExportersManager", "Version:"))
        self.label.setText(_translate("ExportersManager", "Path:"))
        self.btnSetPath.setText(_translate("ExportersManager", "..."))
        self.lblHelpText.setText(_translate("ExportersManager", "{HelpText}"))

