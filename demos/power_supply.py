from PyQt5 import QtWidgets, QtCore
from ui_power_supply import Ui_MainWindow
import sys


class PowerSupplyGui(QtWidgets.QMainWindow):

    def __init__(self):

        super(PowerSupplyGui, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ps_logic = PowerSupplyLogic()

        # Connect GUI input events
        self.ui.ch1_volt_dial.valueChanged.connect(self.gui_set_ch1_volt)
        self.ui.ch1_amps_dial.valueChanged.connect(self.gui_set_ch1_amps)
        self.ui.ch2_volt_dial.valueChanged.connect(self.gui_set_ch2_volt)
        self.ui.ch2_amps_dial.valueChanged.connect(self.gui_set_ch2_amps)

        self.ui.ch1_activate_pushButton.clicked.connect(self.gui_activate_ch1)
        self.ui.ch2_activate_pushButton.clicked.connect(self.gui_activate_ch2)

        # Connect signals from Logic
        self.ps_logic.outputs_updated_signal.connect(self.display_updated_outputs)

        # Style for GUI elements that act as LED notifications
        self.led_on_style = "QLabel { background-color: rgba(255, 75, 0, 255); color:rgba(0, 200, 0, 255); }"

    def gui_set_ch1_volt(self):
        new_v = self._get_qdial_value(self.ui.ch1_volt_dial)

        self.ps_logic.set_voltage(0, new_v)

    def gui_set_ch1_amps(self):
        new_amps = self._get_qdial_value(self.ui.ch1_amps_dial)

        self.ps_logic.set_current(0, new_amps)

    def gui_set_ch2_volt(self):
        new_v = self._get_qdial_value(self.ui.ch2_volt_dial)

        self.ps_logic.set_voltage(1, new_v)

    def gui_set_ch2_amps(self):
        new_amps = self._get_qdial_value(self.ui.ch2_amps_dial)

        self.ps_logic.set_current(1, new_amps)

    def gui_activate_ch1(self):
        if self.ui.ch1_activate_pushButton.isChecked():
            self.ps_logic.activate_output(0, True)

        else:
            self.ps_logic.activate_output(0, False)

    def gui_activate_ch2(self):
        if self.ui.ch2_activate_pushButton.isChecked():
            self.ps_logic.activate_output(1, True)

        else:
            self.ps_logic.activate_output(1, False)

    def _get_qdial_value(self, qdial_obj):
        """ Return QDial value divided by 10 give decimal place precision.
        """
        return qdial_obj.value() / 10

    def display_updated_outputs(self, channel):
        """Display any updates to the output values.

        @param int channel: Index of channel. This is passed in the signal from the logic
        """
        volt_lcd = [self.ui.ch1_volt_lcdNumber, self.ui.ch2_volt_lcdNumber]
        amps_lcd = [self.ui.ch1_amps_lcdNumber, self.ui.ch2_amps_lcdNumber]
        v_limit_led = [self.ui.ch1_v_limited_led_label, self.ui.ch2_v_limited_led_label]
        amps_limit_led = [self.ui.ch1_amps_limited_led_label, self.ui.ch2_amps_limited_led_label]

        volt_lcd[channel].display(self.ps_logic.get_v_act(channel))
        amps_lcd[channel].display(self.ps_logic.get_i_act(channel))

        if self.ps_logic.get_v_act(channel) == self.ps_logic.get_v_set(channel):
            v_limit_led[channel].setStyleSheet(self.led_on_style)
            amps_limit_led[channel].setStyleSheet("")
        elif self.ps_logic.get_i_act(channel) == self.ps_logic.get_i_set(channel):
            amps_limit_led[channel].setStyleSheet(self.led_on_style)
            v_limit_led[channel].setStyleSheet("")


class PowerSupplyLogic(QtCore.QObject):

    # Signals for the GUI to listen to for changes to power supply settings.
    outputs_updated_signal = QtCore.pyqtSignal(int)

    def __init__(self):
        super(PowerSupplyLogic, self).__init__()

        self.loads = [0, 10]

        self._v_set = [0, 0]
        self._i_set = [0, 0]

        self._v_act = [0, 0]
        self._i_act = [0, 0]

        self._active = [False, False]

    def set_voltage(self, channel, new_v):
        self._v_set[channel] = new_v

    def set_current(self, channel, new_i):
        self._i_set[channel] = new_i

    def get_v_act(self, channel):
        return self._v_act[channel]

    def get_i_act(self, channel):
        return self._i_act[channel]

    def get_v_set(self, channel):
        return self._v_set[channel]

    def get_i_set(self, channel):
        return self._i_set[channel]

    def activate_output(self, channel, state):
        if state is not self._active[channel]:
            self._active[channel] = state
            self._update_output(channel)

    def _update_output(self, channel):
        """ Update the output of specified channel.
        """
        if self._active[channel]:
            out_v, out_i = self._calc_output(self._v_set[channel],
                                             self._i_set[channel],
                                             self.loads[channel]
                                             )

        # Otherwise the outputs are zero
        else:
            out_v, out_i = 0, 0

        self._v_act[channel] = out_v
        self._i_act[channel] = out_i

        # Signal for anything listening (such as GUI)
        self.outputs_updated_signal.emit(channel)

    def _calc_output(self, v_set, i_set, load):
        """ Use Ohm's law to determine whether we are limited by V or I setting.
        """
        # If no load, then no current regardless of V setting
        if load == 0:
            return v_set, 0

        # Now we consider Ohm's law
        out_v = i_set * load

        if out_v <= v_set:  # We are current limited
            return out_v, i_set

        # Otherwise we are voltage limited
        else:
            out_i = v_set / load
            return v_set, out_i


def main():
    app = QtWidgets.QApplication([])
    application = PowerSupplyGui()
    application.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
