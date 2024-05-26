# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\VADIM\Python\SFedU\diploma\ECG-monitoring-system\ui\ecg_simulator_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ecg_simulator_window(object):
    def setupUi(self, ecg_simulator_window):
        ecg_simulator_window.setObjectName("ecg_simulator_window")
        ecg_simulator_window.resize(908, 676)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ecg_simulator_window.sizePolicy().hasHeightForWidth())
        ecg_simulator_window.setSizePolicy(sizePolicy)
        ecg_simulator_window.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        ecg_simulator_window.setFont(font)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(ecg_simulator_window)
        self.verticalLayout_6.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_4 = QtWidgets.QGroupBox(ecg_simulator_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.button_samples = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_samples.sizePolicy().hasHeightForWidth())
        self.button_samples.setSizePolicy(sizePolicy)
        self.button_samples.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_samples.setFont(font)
        self.button_samples.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_samples.setIconSize(QtCore.QSize(24, 24))
        self.button_samples.setObjectName("button_samples")
        self.horizontalLayout_10.addWidget(self.button_samples)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.button_save = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_save.sizePolicy().hasHeightForWidth())
        self.button_save.setSizePolicy(sizePolicy)
        self.button_save.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_save.setFont(font)
        self.button_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_save.setIconSize(QtCore.QSize(24, 24))
        self.button_save.setObjectName("button_save")
        self.horizontalLayout_10.addWidget(self.button_save)
        self.button_exit = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_exit.sizePolicy().hasHeightForWidth())
        self.button_exit.setSizePolicy(sizePolicy)
        self.button_exit.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_exit.setFont(font)
        self.button_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_exit.setIconSize(QtCore.QSize(24, 24))
        self.button_exit.setObjectName("button_exit")
        self.horizontalLayout_10.addWidget(self.button_exit)
        self.verticalLayout_6.addWidget(self.groupBox_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_3 = QtWidgets.QGroupBox(ecg_simulator_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(450, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setSpacing(5)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_19 = QtWidgets.QLabel(self.groupBox_3)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_26.addWidget(self.label_19)
        self.list_ecg_leads = QtWidgets.QListWidget(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_ecg_leads.sizePolicy().hasHeightForWidth())
        self.list_ecg_leads.setSizePolicy(sizePolicy)
        self.list_ecg_leads.setMinimumSize(QtCore.QSize(0, 0))
        self.list_ecg_leads.setMaximumSize(QtCore.QSize(80, 16777215))
        self.list_ecg_leads.setObjectName("list_ecg_leads")
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_leads.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_leads.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_leads.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_leads.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_leads.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_leads.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_leads.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_leads.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_leads.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_leads.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_leads.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_leads.addItem(item)
        self.verticalLayout_26.addWidget(self.list_ecg_leads)
        self.horizontalLayout_3.addLayout(self.verticalLayout_26)
        self.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.verticalLayout_27.setSpacing(5)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.label_20 = QtWidgets.QLabel(self.groupBox_3)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_27.addWidget(self.label_20)
        self.list_ecg_content = QtWidgets.QListWidget(self.groupBox_3)
        self.list_ecg_content.setMinimumSize(QtCore.QSize(250, 0))
        self.list_ecg_content.setObjectName("list_ecg_content")
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_content.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_content.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_content.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_content.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_content.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_content.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_content.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_content.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_content.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_content.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_content.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_content.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_content.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_content.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_content.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_ecg_content.addItem(item)
        self.verticalLayout_27.addWidget(self.list_ecg_content)
        self.horizontalLayout_3.addLayout(self.verticalLayout_27)
        self.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.verticalLayout_28.setSpacing(5)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.verticalLayout_30.setSpacing(5)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_30.addWidget(self.label_23)
        self.list_ecg_info = QtWidgets.QListWidget(self.groupBox_3)
        self.list_ecg_info.setMinimumSize(QtCore.QSize(0, 0))
        self.list_ecg_info.setObjectName("list_ecg_info")
        self.verticalLayout_30.addWidget(self.list_ecg_info)
        self.verticalLayout_28.addLayout(self.verticalLayout_30)
        self.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.verticalLayout_29.setSpacing(5)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_29.addWidget(self.label_22)
        self.edit_average_ecg_info = QtWidgets.QLineEdit(self.groupBox_3)
        self.edit_average_ecg_info.setMinimumSize(QtCore.QSize(0, 21))
        self.edit_average_ecg_info.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.edit_average_ecg_info.setReadOnly(True)
        self.edit_average_ecg_info.setObjectName("edit_average_ecg_info")
        self.verticalLayout_29.addWidget(self.edit_average_ecg_info)
        self.verticalLayout_28.addLayout(self.verticalLayout_29)
        self.horizontalLayout_3.addLayout(self.verticalLayout_28)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(ecg_simulator_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(450, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setSpacing(5)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setSpacing(5)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_23.addWidget(self.label_17)
        self.edit_heart_rhythm = QtWidgets.QLineEdit(self.groupBox)
        self.edit_heart_rhythm.setMinimumSize(QtCore.QSize(0, 21))
        self.edit_heart_rhythm.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.edit_heart_rhythm.setReadOnly(True)
        self.edit_heart_rhythm.setObjectName("edit_heart_rhythm")
        self.verticalLayout_23.addWidget(self.edit_heart_rhythm)
        self.verticalLayout_21.addLayout(self.verticalLayout_23)
        self.verticalLayout.addLayout(self.verticalLayout_21)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setSpacing(5)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_24.addWidget(self.label_18)
        self.edit_heart_rate = QtWidgets.QLineEdit(self.groupBox)
        self.edit_heart_rate.setMinimumSize(QtCore.QSize(0, 21))
        self.edit_heart_rate.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.edit_heart_rate.setReadOnly(True)
        self.edit_heart_rate.setObjectName("edit_heart_rate")
        self.verticalLayout_24.addWidget(self.edit_heart_rate)
        self.verticalLayout.addLayout(self.verticalLayout_24)
        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setSpacing(5)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_25.addWidget(self.label_16)
        self.edit_heart_axis = QtWidgets.QLineEdit(self.groupBox)
        self.edit_heart_axis.setMinimumSize(QtCore.QSize(0, 21))
        self.edit_heart_axis.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.edit_heart_axis.setReadOnly(True)
        self.edit_heart_axis.setObjectName("edit_heart_axis")
        self.verticalLayout_25.addWidget(self.edit_heart_axis)
        self.verticalLayout.addLayout(self.verticalLayout_25)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(ecg_simulator_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_plot = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_plot.sizePolicy().hasHeightForWidth())
        self.label_plot.setSizePolicy(sizePolicy)
        self.label_plot.setMinimumSize(QtCore.QSize(0, 0))
        self.label_plot.setText("")
        self.label_plot.setScaledContents(True)
        self.label_plot.setAlignment(QtCore.Qt.AlignCenter)
        self.label_plot.setWordWrap(False)
        self.label_plot.setObjectName("label_plot")
        self.horizontalLayout_4.addWidget(self.label_plot)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ecg_simulator_window)
        QtCore.QMetaObject.connectSlotsByName(ecg_simulator_window)

    def retranslateUi(self, ecg_simulator_window):
        _translate = QtCore.QCoreApplication.translate
        ecg_simulator_window.setWindowTitle(_translate("ecg_simulator_window", "Симулятор данных ЭКГ"))
        self.groupBox_4.setTitle(_translate("ecg_simulator_window", "Панель управления"))
        self.button_samples.setText(_translate("ecg_simulator_window", "Образцы"))
        self.button_save.setText(_translate("ecg_simulator_window", "Сохранить"))
        self.button_exit.setText(_translate("ecg_simulator_window", "Закрыть"))
        self.groupBox_3.setTitle(_translate("ecg_simulator_window", "Состав ЭКГ"))
        self.label_19.setText(_translate("ecg_simulator_window", "Отведение"))
        __sortingEnabled = self.list_ecg_leads.isSortingEnabled()
        self.list_ecg_leads.setSortingEnabled(False)
        item = self.list_ecg_leads.item(0)
        item.setText(_translate("ecg_simulator_window", "I"))
        item = self.list_ecg_leads.item(1)
        item.setText(_translate("ecg_simulator_window", "II"))
        item = self.list_ecg_leads.item(2)
        item.setText(_translate("ecg_simulator_window", "III"))
        item = self.list_ecg_leads.item(3)
        item.setText(_translate("ecg_simulator_window", "aVR"))
        item = self.list_ecg_leads.item(4)
        item.setText(_translate("ecg_simulator_window", "aVL"))
        item = self.list_ecg_leads.item(5)
        item.setText(_translate("ecg_simulator_window", "aVF"))
        item = self.list_ecg_leads.item(6)
        item.setText(_translate("ecg_simulator_window", "V1"))
        item = self.list_ecg_leads.item(7)
        item.setText(_translate("ecg_simulator_window", "V2"))
        item = self.list_ecg_leads.item(8)
        item.setText(_translate("ecg_simulator_window", "V3"))
        item = self.list_ecg_leads.item(9)
        item.setText(_translate("ecg_simulator_window", "V4"))
        item = self.list_ecg_leads.item(10)
        item.setText(_translate("ecg_simulator_window", "V5"))
        item = self.list_ecg_leads.item(11)
        item.setText(_translate("ecg_simulator_window", "V6"))
        self.list_ecg_leads.setSortingEnabled(__sortingEnabled)
        self.label_20.setText(_translate("ecg_simulator_window", "Элемент"))
        __sortingEnabled = self.list_ecg_content.isSortingEnabled()
        self.list_ecg_content.setSortingEnabled(False)
        item = self.list_ecg_content.item(0)
        item.setText(_translate("ecg_simulator_window", "Зубец P [продолжительность]"))
        item = self.list_ecg_content.item(1)
        item.setText(_translate("ecg_simulator_window", "Зубец P [амплитуда]"))
        item = self.list_ecg_content.item(2)
        item.setText(_translate("ecg_simulator_window", "Зубец Q [продолжительность]"))
        item = self.list_ecg_content.item(3)
        item.setText(_translate("ecg_simulator_window", "Зубец Q [амплитуда]"))
        item = self.list_ecg_content.item(4)
        item.setText(_translate("ecg_simulator_window", "Зубец R [продолжительность]"))
        item = self.list_ecg_content.item(5)
        item.setText(_translate("ecg_simulator_window", "Зубец R [амплитуда]"))
        item = self.list_ecg_content.item(6)
        item.setText(_translate("ecg_simulator_window", "Зубец S [продолжительность]"))
        item = self.list_ecg_content.item(7)
        item.setText(_translate("ecg_simulator_window", "Зубец S [амплитуда]"))
        item = self.list_ecg_content.item(8)
        item.setText(_translate("ecg_simulator_window", "Зубец T [продолжительность]"))
        item = self.list_ecg_content.item(9)
        item.setText(_translate("ecg_simulator_window", "Зубец T [амплитуда]"))
        item = self.list_ecg_content.item(10)
        item.setText(_translate("ecg_simulator_window", "Сегмент PQ(R) [продолжительность]"))
        item = self.list_ecg_content.item(11)
        item.setText(_translate("ecg_simulator_window", "Сегмент (R)ST [продолжительность]"))
        item = self.list_ecg_content.item(12)
        item.setText(_translate("ecg_simulator_window", "Сегмент (R)ST [смещение]"))
        item = self.list_ecg_content.item(13)
        item.setText(_translate("ecg_simulator_window", "Интервал P-Q(R) [продолжительность]"))
        item = self.list_ecg_content.item(14)
        item.setText(_translate("ecg_simulator_window", "Интервал Q-T [продолжительность]"))
        item = self.list_ecg_content.item(15)
        item.setText(_translate("ecg_simulator_window", "Комплекс QRS [продолжительность]"))
        self.list_ecg_content.setSortingEnabled(__sortingEnabled)
        self.label_23.setText(_translate("ecg_simulator_window", "Значение"))
        self.label_22.setText(_translate("ecg_simulator_window", "Среднее"))
        self.groupBox.setTitle(_translate("ecg_simulator_window", "Результаты"))
        self.label_17.setText(_translate("ecg_simulator_window", "Сердечный ритм"))
        self.label_18.setText(_translate("ecg_simulator_window", "ЧСС"))
        self.label_16.setText(_translate("ecg_simulator_window", "ЭОС"))
        self.groupBox_2.setTitle(_translate("ecg_simulator_window", "График"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ecg_simulator_window = QtWidgets.QWidget()
    ui = Ui_ecg_simulator_window()
    ui.setupUi(ecg_simulator_window)
    ecg_simulator_window.show()
    sys.exit(app.exec_())
