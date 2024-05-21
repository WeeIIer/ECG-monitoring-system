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

menu_window.show()
app.exec_()
