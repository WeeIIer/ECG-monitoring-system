# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\VADIM\Python\SFedU\diploma\ECG-monitoring-system\ui\controller_import_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_controller_import_window(object):
    def setupUi(self, controller_import_window):
        controller_import_window.setObjectName("controller_import_window")
        controller_import_window.resize(772, 449)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(controller_import_window.sizePolicy().hasHeightForWidth())
        controller_import_window.setSizePolicy(sizePolicy)
        controller_import_window.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        controller_import_window.setFont(font)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(controller_import_window)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(controller_import_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(340, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setSpacing(5)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_19 = QtWidgets.QLabel(self.groupBox_3)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_26.addWidget(self.label_19)
        self.table_input_attributes = QtWidgets.QTableWidget(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_input_attributes.sizePolicy().hasHeightForWidth())
        self.table_input_attributes.setSizePolicy(sizePolicy)
        self.table_input_attributes.setMinimumSize(QtCore.QSize(0, 0))
        self.table_input_attributes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_input_attributes.setTabKeyNavigation(True)
        self.table_input_attributes.setAlternatingRowColors(True)
        self.table_input_attributes.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_input_attributes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_input_attributes.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table_input_attributes.setRowCount(0)
        self.table_input_attributes.setObjectName("table_input_attributes")
        self.table_input_attributes.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.table_input_attributes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_input_attributes.setHorizontalHeaderItem(1, item)
        self.table_input_attributes.horizontalHeader().setVisible(True)
        self.table_input_attributes.verticalHeader().setVisible(False)
        self.verticalLayout_26.addWidget(self.table_input_attributes)
        self.horizontalLayout_3.addLayout(self.verticalLayout_26)
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setSpacing(5)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.label_20 = QtWidgets.QLabel(self.groupBox_3)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_27.addWidget(self.label_20)
        self.button_apply = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_apply.sizePolicy().hasHeightForWidth())
        self.button_apply.setSizePolicy(sizePolicy)
        self.button_apply.setMinimumSize(QtCore.QSize(40, 40))
        self.button_apply.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_apply.setFont(font)
        self.button_apply.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_apply.setIconSize(QtCore.QSize(24, 24))
        self.button_apply.setObjectName("button_apply")
        self.verticalLayout_27.addWidget(self.button_apply)
        self.horizontalLayout_3.addLayout(self.verticalLayout_27)
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setSpacing(5)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.label_21 = QtWidgets.QLabel(self.groupBox_3)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_28.addWidget(self.label_21)
        self.table_import = QtWidgets.QTableWidget(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_import.sizePolicy().hasHeightForWidth())
        self.table_import.setSizePolicy(sizePolicy)
        self.table_import.setMinimumSize(QtCore.QSize(0, 0))
        self.table_import.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_import.setTabKeyNavigation(True)
        self.table_import.setAlternatingRowColors(True)
        self.table_import.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_import.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_import.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.table_import.setRowCount(0)
        self.table_import.setObjectName("table_import")
        self.table_import.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.table_import.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_import.setHorizontalHeaderItem(1, item)
        self.table_import.horizontalHeader().setVisible(True)
        self.table_import.verticalHeader().setVisible(False)
        self.verticalLayout_28.addWidget(self.table_import)
        self.horizontalLayout_3.addLayout(self.verticalLayout_28)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_open = QtWidgets.QPushButton(controller_import_window)
        self.button_open.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_open.setFont(font)
        self.button_open.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_open.setIconSize(QtCore.QSize(24, 24))
        self.button_open.setObjectName("button_open")
        self.horizontalLayout.addWidget(self.button_open)
        self.button_exit = QtWidgets.QPushButton(controller_import_window)
        self.button_exit.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_exit.setFont(font)
        self.button_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_exit.setIconSize(QtCore.QSize(24, 24))
        self.button_exit.setObjectName("button_exit")
        self.horizontalLayout.addWidget(self.button_exit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.retranslateUi(controller_import_window)
        QtCore.QMetaObject.connectSlotsByName(controller_import_window)

    def retranslateUi(self, controller_import_window):
        _translate = QtCore.QCoreApplication.translate
        controller_import_window.setWindowTitle(_translate("controller_import_window", "Импорт данных"))
        self.groupBox_3.setTitle(_translate("controller_import_window", "Панель управления"))
        self.label_19.setText(_translate("controller_import_window", "Входные атрибуты"))
        self.table_input_attributes.setSortingEnabled(False)
        item = self.table_input_attributes.horizontalHeaderItem(0)
        item.setText(_translate("controller_import_window", "Название"))
        item = self.table_input_attributes.horizontalHeaderItem(1)
        item.setText(_translate("controller_import_window", "Значение"))
        self.label_20.setText(_translate("controller_import_window", " "))
        self.button_apply.setText(_translate("controller_import_window", "<<"))
        self.label_21.setText(_translate("controller_import_window", "Загруженные данные"))
        self.table_import.setSortingEnabled(False)
        item = self.table_import.horizontalHeaderItem(0)
        item.setText(_translate("controller_import_window", "Название"))
        item = self.table_import.horizontalHeaderItem(1)
        item.setText(_translate("controller_import_window", "Значение"))
        self.button_open.setText(_translate("controller_import_window", "Выбрать файл"))
        self.button_exit.setText(_translate("controller_import_window", "Закрыть"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller_import_window = QtWidgets.QWidget()
    ui = Ui_controller_import_window()
    ui.setupUi(controller_import_window)
    controller_import_window.show()
    sys.exit(app.exec_())
