import math

import matplotlib.axes
import matplotlib.pyplot as plt
import pandas as pd
import pandas.core.frame

import ecg_simulator_window
from settings import *
from objects import LP, PP, Dictionary, FuzzyProject
from functions import create_plot

DICTIONARY = Dictionary()

CURRENT_LP: LP | None = None
CURRENT_PP: PP | None = None
CURRENT_PROJECT: FuzzyProject | None = None


class AlertWindow(QWidget, alert_window_form.Ui_alert_window):
    def __init__(self):
        super(AlertWindow, self).__init__()
        self.setupUi(self)

        self.source_window: QWidget | None = None
        self.button_exit.clicked.connect(self.close)

    def show(self, source_window: QWidget = None, message: str = None):
        super(AlertWindow, self).show()
        self.source_window = source_window
        self.source_window.setEnabled(False)
        self.label_message.setText(message)

    def closeEvent(self, a0):
        super(AlertWindow, self).closeEvent(a0)
        self.source_window.setEnabled(True)


class MenuWindow(QWidget, menu_window_form.Ui_menu_window):
    def __init__(self):
        super(MenuWindow, self).__init__()
        self.setupUi(self)

        self.button_add_project.clicked.connect(self.on_clicked_button_add_project)

        self.button_add_lp.clicked.connect(self.on_clicked_button_add_lp)
        self.button_dict_lp.clicked.connect(self.on_clicked_button_dict_lp)

        self.button_add_pp.clicked.connect(self.on_clicked_button_add_pp)
        self.button_dict_pp.clicked.connect(self.on_clicked_button_dict_pp)

        self.button_exit.clicked.connect(app.closeAllWindows)

    def on_clicked_button_add_project(self):
        self.hide()
        controller_window.show()

    def on_clicked_button_add_lp(self):
        global CURRENT_LP
        CURRENT_LP = None
        self.hide()
        lp_editor_window.show()

    def on_clicked_button_dict_lp(self):
        self.hide()
        dictionary_window.show(0)

    def on_clicked_button_add_pp(self):
        global CURRENT_PP
        CURRENT_PP = None
        self.hide()
        pp_editor_window.show()

    def on_clicked_button_dict_pp(self):
        self.hide()
        dictionary_window.show(1)

    def show(self):
        super(MenuWindow, self).show()
        DICTIONARY.load_LPs()
        DICTIONARY.load_PPs()


class DictionaryWindow(QWidget, dictionary_window_form.Ui_dictionary_window):
    def __init__(self):
        super(DictionaryWindow, self).__init__()
        self.setupUi(self)

        self.current_tab = 0

        self.button_open.clicked.connect(self.on_clicked_button_open)
        self.button_delete.clicked.connect(self.on_clicked_button_delete)
        self.button_exit.clicked.connect(self.close)

        self.list_lp.doubleClicked.connect(self.on_clicked_button_open)
        self.list_pp.doubleClicked.connect(self.on_clicked_button_open)
        self.tabWidget.tabBar().currentChanged.connect(self.on_tab_current_changed)

    def on_tab_current_changed(self):
        self.current_tab = self.tabWidget.tabBar().currentIndex()
        self.update_lists()

    def on_clicked_button_open(self):
        global CURRENT_LP, CURRENT_PP

        if self.current_tab == 0:
            i = self.list_lp.currentRow()
            if i > -1:
                CURRENT_LP = DICTIONARY.LP(i)
                self.hide()
                lp_editor_window.show()
        elif self.current_tab == 1:
            i = self.list_pp.currentRow()
            if i > -1:
                CURRENT_PP = DICTIONARY.PP(i)
                self.hide()
                pp_editor_window.show()

    def on_clicked_button_delete(self):
        if self.current_tab == 0:
            i = self.list_lp.currentRow()
            if i > -1:
                DICTIONARY.discard_LP(i)
        elif self.current_tab == 1:
            i = self.list_pp.currentRow()
            if i > -1:
                DICTIONARY.discard_PP(i)

        self.update_lists()

    def update_lists(self):
        if self.current_tab == 0:
            DICTIONARY.load_LPs()
            self.list_lp.clear()
            self.list_lp.addItems(DICTIONARY.LP_titles())
        elif self.current_tab == 1:
            DICTIONARY.load_PPs()
            self.list_pp.clear()
            self.list_pp.addItems(DICTIONARY.PP_titles())

        self.button_exit.setFocus()

    def show(self, current_tab=0):
        super(DictionaryWindow, self).show()

        self.current_tab = current_tab
        self.tabWidget.tabBar().setCurrentIndex(self.current_tab)
        self.update_lists()

    def closeEvent(self, a0):
        super(DictionaryWindow, self).closeEvent(a0)
        menu_window.show()


class LPEditorWindow(QWidget, lp_editor_window_form.Ui_lp_editor_window):
    def __init__(self):
        super(LPEditorWindow, self).__init__()
        self.setupUi(self)

        self.slider_x_axis_top, self.slider_x_axis_bottom = self.__create_sliders()
        for i in range(1, 7):
            self.findChild(QCheckBox, f"check_err_{i}").setEnabled(False)

        self.splitter.restoreState(SETTINGS.value("splitterSizes"))
        self.splitter_3.restoreState(SETTINGS.value("splitterSizes"))

        self.button_save.clicked.connect(self.on_clicked_button_save)
        self.button_exit.clicked.connect(self.close)

        self.list_terms.itemClicked.connect(self.on_item_clicked_list_terms)
        self.list_terms.doubleClicked.connect(self.on_double_clicked_list_terms)
        self.slider_x_axis_bottom.valueChanged.connect(self.on_value_changed_slider_x_axis_bottom)
        self.slider_x_axis_top.valueChanged.connect(self.on_value_changed_slider_x_axis_top)
        self.edit_title.textChanged.connect(self.on_text_changed_edit_title)
        self.edit_x_start.textChanged.connect(self.on_text_changed_edit_x)
        self.edit_x_stop.textChanged.connect(self.on_text_changed_edit_x)
        self.edit_add_term.returnPressed.connect(self.on_return_pressed_edit_add_term)

    def on_clicked_button_save(self):
        if CURRENT_LP.is_fullness() and all(CURRENT_LP.limits()):
            CURRENT_LP.save()
            DICTIONARY.load_LPs()
            alert_window.show(self, "Сохранение прошло успешно!")
        else:
            alert_window.show(self, "Сохранение не удалось!")

    def on_item_clicked_list_terms(self):
        i = self.list_terms.currentRow()
        self.slider_x_axis_bottom.setValue(CURRENT_LP.terms[i].x_axis_bottom())
        self.slider_x_axis_top.setValue(CURRENT_LP.terms[i].x_axis_top())

    def on_double_clicked_list_terms(self):
        i = self.list_terms.currentRow()
        CURRENT_LP.discard_term(i)
        self.add_terms_to_list()
        self.change_sliders_range()
        self.draw_plot()

    def on_value_changed_slider_x_axis_bottom(self):
        i = self.list_terms.currentRow()
        if i > -1:
            x_pair = self.slider_x_axis_bottom.value()
            CURRENT_LP.terms[i].set_x_axis_bottom(*x_pair)
            self.groupBox_5.setTitle(f"Редактирование нижных координат терма {x_pair}")
            self.draw_plot()

    def on_value_changed_slider_x_axis_top(self):
        i = self.list_terms.currentRow()
        if i > -1:
            x_pair = self.slider_x_axis_top.value()
            CURRENT_LP.terms[i].set_x_axis_top(*x_pair)
            self.groupBox_7.setTitle(f"Редактирование верхних координат терма {x_pair}")
            self.draw_plot()

    def on_text_changed_edit_title(self):
        title = self.edit_title.text()
        if title.strip():
            CURRENT_LP.set_title(title)

    def on_text_changed_edit_x(self):
        x_start, x_stop = self.edit_x_start.text(), self.edit_x_stop.text()
        try:
            x_start, x_stop = int(x_start), int(x_stop)
            if x_start < x_stop:
                CURRENT_LP.set_x_start(x_start)
                CURRENT_LP.set_x_stop(x_stop)
                # CURRENT_LP.update_terms()
                # self.add_terms_to_list()
                # self.change_sliders_range()
                self.draw_plot()
                self.edit_add_term.setEnabled(True)
            else:
                raise ValueError
        except ValueError:
            self.label_plot.clear()
            self.edit_add_term.setEnabled(False)

    def on_return_pressed_edit_add_term(self):
        term_title = self.edit_add_term.text().strip()
        self.edit_add_term.clear()
        if term_title:
            CURRENT_LP.add_term(term_title)
            self.add_terms_to_list()
            self.change_sliders_range()
            self.draw_plot()

    def add_terms_to_list(self):
        self.list_terms.clear()
        self.list_terms.addItems(CURRENT_LP.term_titles())

    def change_sliders_range(self):
        if CURRENT_LP.is_fullness():
            x_start, x_stop = CURRENT_LP.x_start, CURRENT_LP.x_stop
        else:
            x_start, x_stop = 0, 1

        self.slider_x_axis_bottom.setRange(x_start, x_stop)
        self.slider_x_axis_bottom.setValue([x_start, x_stop])
        self.groupBox_5.setTitle(f"Редактирование нижных координат терма ( ... )")

        self.slider_x_axis_top.setRange(x_start, x_stop)
        self.slider_x_axis_top.setValue([x_start, x_stop])
        self.groupBox_7.setTitle(f"Редактирование верхних координат терма ( ... )")

    def update_limits(self):
        for i, state in enumerate(CURRENT_LP.limits(), 1):
            self.findChild(QCheckBox, f"check_err_{i}").setChecked(state)

    def draw_plot(self):
        self.label_plot.clear()
        self.label_plot.setPixmap(QPixmap(create_plot(CURRENT_LP)))
        self.update_limits()

    def show(self):
        global CURRENT_LP
        super(LPEditorWindow, self).show()
        self.showMaximized()

        self.edit_title.clear()
        self.edit_x_start.clear()
        self.edit_x_stop.clear()
        self.edit_add_term.clear()
        self.list_terms.clear()
        self.label_plot.clear()

        if CURRENT_LP is None:
            CURRENT_LP = LP()
            CURRENT_LP.load()
            self.edit_add_term.setEnabled(False)
        else:
            self.edit_title.setText(CURRENT_LP.title)
            self.edit_x_start.setText(str(CURRENT_LP.x_start))
            self.edit_x_stop.setText(str(CURRENT_LP.x_stop))
            self.add_terms_to_list()

        self.change_sliders_range()
        if CURRENT_LP.is_fullness():
            self.draw_plot()

    def closeEvent(self, a0):
        super(LPEditorWindow, self).closeEvent(a0)

        SETTINGS.setValue("splitterSizes", self.splitter.saveState())
        SETTINGS.setValue("splitterSizes", self.splitter_3.saveState())

        menu_window.show()

    def __create_sliders(self) -> tuple[QRangeSlider, QRangeSlider]:
        for splitter, slider_name in ((self.splitter_3, "slider_x_axis_top"), (self.splitter, "slider_x_axis_bottom")):
            left_frame = QtWidgets.QFrame(splitter)

            slider_x_axis = QRangeSlider(QtCore.Qt.Horizontal)
            slider_x_axis.setValue((0, 1))
            slider_x_axis.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            slider_x_axis.setObjectName(slider_name)
            splitter.addWidget(slider_x_axis)

            right_frame = QtWidgets.QFrame(splitter)
        return self.findChild(QRangeSlider, "slider_x_axis_top"), self.findChild(QRangeSlider, "slider_x_axis_bottom")


class PPEditorWindow(QWidget, pp_editor_window_form.Ui_pp_editor_window):
    def __init__(self):
        super(PPEditorWindow, self).__init__()
        self.setupUi(self)

        self.button_add_attribute.clicked.connect(self.on_clicked_button_add_attribute)
        self.button_save.clicked.connect(self.on_clicked_button_save)
        self.button_exit.clicked.connect(self.close)

    def on_clicked_button_add_attribute(self):
        CURRENT_PP.add_attribute()
        self.layout_scroll_attribute.addWidget(CURRENT_PP.attributes[-1].widget)

    def on_clicked_button_save(self):
        if CURRENT_PP.is_attributes_fullness():
            CURRENT_PP.save()
            DICTIONARY.load_PPs()
            self.edit_expression.setText(CURRENT_PP.words_expression)
            alert_window.show(self, "Сохранение прошло успешно!")
        else:
            alert_window.show(self, "Сохранение не удалось!")

    def show(self):
        global CURRENT_PP
        super(PPEditorWindow, self).show()
        self.showMaximized()

        self.edit_expression.clear()

        if CURRENT_PP is None:
            CURRENT_PP = PP(DICTIONARY)
            CURRENT_PP.add_attribute(is_output=True)
            self.layout_output_attribute.addWidget(CURRENT_PP.output_attribute.widget)
        else:
            self.edit_expression.setText(CURRENT_PP.words_expression)
            for attr in CURRENT_PP.attributes:
                self.layout_scroll_attribute.addWidget(attr.widget)
                attr.set_combo_indices()
            self.layout_output_attribute.addWidget(CURRENT_PP.output_attribute.widget)
            CURRENT_PP.output_attribute.set_combo_indices()

    def closeEvent(self, a0):
        super(PPEditorWindow, self).closeEvent(a0)
        CURRENT_PP.clear()
        menu_window.show()


class ControllerWindow(QWidget, controller_window_form.Ui_controller_window):
    def __init__(self):
        super(ControllerWindow, self).__init__()
        self.setupUi(self)

        self.is_loaded: bool | None = None

        self.button_calculate.clicked.connect(self.on_clicked_button_calculate)
        self.button_ecg_simulator.clicked.connect(lambda: ecg_simulator_window.show())
        self.button_save.clicked.connect(self.on_clicked_button_save)
        self.button_exit.clicked.connect(self.close)

        self.combo_add_attribute.currentIndexChanged.connect(self.on_index_changed_combo_add_attribute)
        self.combo_add_output_attribute.currentIndexChanged.connect(self.on_index_changed_combo_add_output_attribute)

    def on_clicked_button_save(self):
        pass

    def on_clicked_button_calculate(self):
        CURRENT_PROJECT.show()

    def on_index_changed_combo_add_attribute(self):
        i = self.combo_add_attribute.currentIndex()
        if i > -1 and self.is_loaded:
            CURRENT_PROJECT.add_attribute(DICTIONARY.LP(i))
            attribute = CURRENT_PROJECT.attributes[-1]
            widget = attribute.widget
            self.layout_scroll_attribute.addWidget(widget)
            self.combo_add_attribute.setCurrentIndex(-1)

    def on_index_changed_combo_add_output_attribute(self):
        i = self.combo_add_output_attribute.currentIndex()
        if i > -1 and self.is_loaded:
            CURRENT_PROJECT.add_attribute(DICTIONARY.LP(i), is_output=True)
            attribute = CURRENT_PROJECT.output_attribute
            widget = attribute.widget
            self.layout_scroll_output_attribute.addWidget(widget)
            self.combo_add_output_attribute.setCurrentIndex(-1)

    def show(self):
        global CURRENT_PROJECT
        super(ControllerWindow, self).show()
        self.showMaximized()

        CURRENT_PROJECT = FuzzyProject(DICTIONARY)
        CURRENT_PROJECT.set_text_log_widget(self.text_log)
        self.is_loaded = False

        self.text_log.clear()

        self.combo_add_attribute.clear()
        self.combo_add_attribute.addItems(DICTIONARY.LP_titles())
        self.combo_add_attribute.setCurrentIndex(-1)

        self.combo_add_output_attribute.clear()
        self.combo_add_output_attribute.addItems(DICTIONARY.LP_titles())
        self.combo_add_output_attribute.setCurrentIndex(-1)

        self.is_loaded = True

    def closeEvent(self, a0):
        super(ControllerWindow, self).closeEvent(a0)
        CURRENT_PROJECT.clear()
        menu_window.show()


class ECGSimulatorWindow(QWidget, ecg_simulator_window.Ui_ecg_simulator_window):
    def __init__(self):
        super(ECGSimulatorWindow, self).__init__()
        self.setupUi(self)

        self.button_generate.clicked.connect(self.on_clicked_button_generate)
        self.button_exit.clicked.connect(self.close)

        self.list_ecg_leads.itemClicked.connect(self.on_item_clicked_list_leads)
        self.list_ecg_content.itemClicked.connect(self.on_item_clicked_list_content)
        self.list_ecg_info.itemClicked.connect(self.on_item_clicked_list_ecg_info)

        self.sampling_rate = 1000
        self.duration = 10
        self.ecg_signal = pd.DataFrame()
        self.ecg_info = pd.DataFrame()
        self.lead = None
        self.content_item = -1

    def on_item_clicked_list_leads(self):
        self.lead = self.list_ecg_leads.currentItem().text()
        self.ecg_process()

    def on_item_clicked_list_content(self):
        self.content_item = self.list_ecg_content.currentRow()
        self.ecg_process()

    def on_item_clicked_list_ecg_info(self):
        labels = "PPQQRRSSTT"
        item = self.content_item
        i = self.list_ecg_info.currentRow()
        info = self.ecg_info
        vertical_borders = ()

        if item in (0, 4, 8):
            vertical_borders = (info[f"ECG_{labels[item]}_Onsets"][i], info[f"ECG_{labels[item]}_Offsets"][i])
        elif item in (1, 3, 5, 7, 9):
            vertical_borders = (info[f"ECG_{labels[item]}_Peaks"][i],)
        elif item == 10:
            vertical_borders = (info["ECG_P_Offsets"][i], info["ECG_Q_Peaks"][i])
        elif item == (11, 12):
            vertical_borders = (info["ECG_S_Peaks"][i], info["ECG_T_Onsets"][i])
        elif item == 13:
            vertical_borders = (info["ECG_P_Onsets"][i], info["ECG_R_Onsets"][i])
        elif item == 14:
            vertical_borders = (info["ECG_R_Offsets"][i], info["ECG_T_Offsets"][i])
        elif item == 15:
            left = tuple(r if pd.isna(q) else q for q, r in zip(info["ECG_Q_Peaks"], info["ECG_R_Onsets"]))
            right = tuple(r if pd.isna(s) else s for s, r in zip(info["ECG_S_Peaks"], info["ECG_R_Offsets"]))
            vertical_borders = (left[i], right[i])

        self.plot(map(lambda x: x / self.sampling_rate, vertical_borders))

    def on_clicked_button_generate(self):
        self.load_ecg_data()

    def load_ecg_data(self):
        try:
            # # number = np.random.randint(0, 4999)
            # # print(f"sample # {number}...")
            # # data = np.load("sim_ecg_data.npy")
            # # leads = ("I", "II", "III", "aVR", "aVL", "aVF", *(f"V{i}" for i in range(1, 7)))
            # # ecg_mV = data[number]
            # #
            # #
            # # for lead, lead_data in zip(leads, ecg_mV):
            # #     self.ecg_signal[lead] = pd.Series(value * 10 for value in lead_data)
            # #
            # # print(self.ecg_signal)
            #
            # # Normal parameters (used by default)
            # # ===================================
            # # t, the starting position along the circle of each interval in radius
            # ti = np.array((-70, -15, 0, 15, 100))
            # # a, the amplitude of each spike
            # ai = np.array((1.2, -5, 30, -7.5, 0.75))
            # # b, the width of each spike
            # bi = np.array((0.25, 0.1, 0.1, 0.1, 0.4))
            #
            # # Add noise
            # # ===============
            # ti = np.random.normal(ti, np.ones(5) * 3)
            # ai = np.random.normal(ai, np.abs(ai / 5))
            # bi = np.random.normal(bi, np.abs(bi / 5))
            #
            # ecg_mV = nk.ecg_simulate(duration=self.duration, method="multileads", sampling_rate=self.sampling_rate, ti=ti, ai=ai, bi=bi)
            ecg_mV = nk.ecg_simulate(duration=self.duration, method="multileads", sampling_rate=self.sampling_rate)
            self.ecg_signal = pd.DataFrame()

            for lead, lead_data in ecg_mV.items():
                self.ecg_signal[lead] = pd.Series(value * 10 for value in lead_data)

            self.calculate_heart_rhythm()
            self.calculate_heart_rate()
            # self.calculate_heart_axis()

            self.list_ecg_leads.setCurrentRow(-1)
            self.list_ecg_content.setCurrentRow(-1)
            self.list_ecg_info.clear()

            self.plot()
        except Exception:
            self.load_ecg_data()

    def plot(self, vertical_borders=()):
        nk.signal_plot(self.ecg_signal, subplots=True, sampling_rate=self.sampling_rate)
        plt.gca().set_xlabel("")

        if vertical_borders:
            for x in vertical_borders:
                plt.gcf().get_axes()[self.list_ecg_leads.currentRow()].axvline(x=x, c="red")

        fig = plt.gcf()
        fig.set_size_inches(20, 12, forward=True)
        fig.savefig("ECG_plot.png", transparent=True, bbox_inches="tight")

        self.label_plot.clear()
        self.label_plot.setPixmap(QPixmap("ECG_plot.png"))

    def ecg_process(self):
        if isinstance(self.lead, str) and self.content_item > -1:
            _, self.ecg_info = nk.ecg_process(self.ecg_signal[self.lead], sampling_rate=self.sampling_rate)

            self.list_ecg_info.clear()
            self.list_ecg_info.addItems(map(str, self.interpret_ecg()))

    def interpret_ecg(self):
        """
           Items
        0  Зубец P [продолжительность]
        1  Зубец P [амплитуда]
        2  Зубец Q [продолжительность]
        3  Зубец Q [амплитуда]
        4  Зубец R [продолжительность]
        5  Зубец R [амплитуда]
        6  Зубец S [продолжительность]
        7  Зубец S [амплитуда]
        8  Зубец T [продолжительность]
        9  Зубец T [амплитуда]
        10 Сегмент PQ(R) [продолжительность]
        11 Сегмент (R)ST [продолжительность]
        12 Сегмент (R)ST [смещение]
        13 Интервал P-Q(R) [продолжительность]
        14 Интервал Q-T [продолжительность]
        15 Комплекс QRS [продолжительность]
        """

        labels = "PPQQRRSSTT"
        item = self.content_item
        lead_signal = self.ecg_signal[self.lead]
        info = self.ecg_info

        Hz_to_sec = lambda Hz: Hz / self.sampling_rate
        nan_to_zero = lambda value: 0 if pd.isna(value) else round(value, 2)

        if item in (0, 4, 8):
            source = zip(info[f"ECG_{labels[item]}_Onsets"], info[f"ECG_{labels[item]}_Offsets"])
            return (nan_to_zero(Hz_to_sec(end - begin)) for begin, end in source)
        elif item in (1, 3, 5, 7, 9):
            source = info[f"ECG_{labels[item]}_Peaks"]
            return (0 if pd.isna(peak) else round(lead_signal[peak], 2) for peak in source)
        elif item == 10:
            source = zip(info["ECG_P_Offsets"], info["ECG_Q_Peaks"])
            return (nan_to_zero(Hz_to_sec(end - begin)) for begin, end in source)
        elif item == 11:
            source = zip(info["ECG_S_Peaks"], info["ECG_T_Onsets"])
            return (nan_to_zero(Hz_to_sec(end - begin)) for begin, end in source)
        elif item == 12:
            left = (0 if pd.isna(begin) else lead_signal[begin] for begin in info["ECG_R_Offsets"])
            right = (0 if pd.isna(end) else lead_signal[end] for end in info["ECG_T_Onsets"])
            return (round((begin + end) / 2, 2) for begin, end in zip(left, right))
        elif item == 13:
            source = zip(info["ECG_P_Onsets"], info["ECG_R_Onsets"])
            return (nan_to_zero(Hz_to_sec(end - begin)) for begin, end in source)
        elif item == 14:
            source = zip(info["ECG_R_Offsets"], info["ECG_T_Offsets"])
            return (nan_to_zero(Hz_to_sec(end - begin)) for begin, end in source)
        elif item == 15:
            left = (r if pd.isna(q) else q for q, r in zip(info["ECG_Q_Peaks"], info["ECG_R_Onsets"]))
            right = (r if pd.isna(s) else s for s, r in zip(info["ECG_S_Peaks"], info["ECG_R_Offsets"]))
            return (nan_to_zero(Hz_to_sec(end - begin)) for begin, end in zip(left, right))

        return ("Нет данных.",)

    def calculate_heart_rhythm(self):
        _, ecg_info = nk.ecg_process(self.ecg_signal["II"], sampling_rate=self.sampling_rate)

        r_peaks = ecg_info["ECG_R_Peaks"]
        rr = [r_peaks[r - 1] + r_peaks[r] for r in range(1, len(r_peaks))]
        average_rr = sum(rr) / len(rr)
        part_from_min = 1 - (average_rr - min(rr)) / average_rr
        part_from_max = 1 - (max(rr) - average_rr) / average_rr
        if part_from_min <= 0.1 or part_from_max <= 0.1:
            self.edit_heart_rhythm.setText("Регулярный")
        else:
            self.edit_heart_rhythm.setText("Нерегулярный")

    def calculate_heart_rate(self):
        _, ecg_info = nk.ecg_process(self.ecg_signal["II"], sampling_rate=self.sampling_rate)
        rr = nk.ecg_rate(ecg_info["ECG_R_Peaks"], self.sampling_rate)
        self.edit_heart_rate.setText(str(int(sum(rr) / len(rr))))

    def calculate_heart_axis(self):
        u = []
        for lead in ("III", "I"):
            _, ecg_info = nk.ecg_process(self.ecg_signal[lead], sampling_rate=self.sampling_rate)
            r_peaks = [r for r in ecg_info["ECG_R_Peaks"] if not pd.isna(r)]
            u.append(sum(self.ecg_signal[lead][r] for r in r_peaks) / len(r_peaks))
        u_3, u_1 = map(lambda value: value / 10, u)

        print(u)
        print(math.degrees(math.tan(1 / (math.sqrt(3) * (2 * u_3 / u_1 + 1)))))

    def show(self):
        super(ECGSimulatorWindow, self).show()
        self.showMaximized()

    def closeEvent(self, a0):
        super(ECGSimulatorWindow, self).closeEvent(a0)


app = QApplication(sys.argv)
app.setStyle("fusion")
app.setPalette(palette())
#app.setWindowIcon(QIcon(":/logos/icons/program.png"))

alert_window = AlertWindow()
menu_window = MenuWindow()
dictionary_window = DictionaryWindow()
lp_editor_window = LPEditorWindow()
pp_editor_window = PPEditorWindow()
controller_window = ControllerWindow()
ecg_simulator_window = ECGSimulatorWindow()

menu_window.show()
app.exec_()
