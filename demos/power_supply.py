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

    def gui_set_ch1_volt(self):
        new_v = self._get_qdial_value(self.ui.ch1_volt_dial)
        self.ui.ch1_volt_lcdNumber.display(new_v)

        self.ps_logic.set_ch1_v(new_v)

    def gui_set_ch1_amps(self):
        new_amps = self._get_qdial_value(self.ui.ch1_amps_dial)
        self.ui.ch1_amps_lcdNumber.display(new_amps)

        self.ps_logic.set_ch1_i(new_amps)

    def gui_set_ch2_volt(self):
        new_v = self._get_qdial_value(self.ui.ch2_volt_dial)
        self.ui.ch2_volt_lcdNumber.display(new_v)

        self.ps_logic.set_ch2_v(new_v)

    def gui_set_ch2_amps(self):
        new_amps = self._get_qdial_value(self.ui.ch2_amps_dial)
        self.ui.ch2_amps_lcdNumber.display(new_amps)

        self.ps_logic.set_ch2_i(new_amps)

    def gui_activate_ch1(self):
        if self.ui.ch1_activate_pushButton.isChecked():
            self.ps_logic.set_ch1_active(True)

        else:
            self.ps_logic.set_ch1_active(False)

    def _get_qdial_value(self, qdial_obj):
        """ Return QDial value divided by 10 give decimal place precision.
        """
        return qdial_obj.value() / 10


class PowerSupplyLogic():

    def __init__(self):
        self.load_1 = 0
        self.load_2 = 10

        self.v_1 = 0
        self.i_1 = 0

        self.v_2 = 0
        self.i_2 = 0

    def set_ch1_v(self, new_v):
        self.v_1 = new_v

    def set_ch1_i(self, new_i):
        self.i_1 = new_i

    def set_ch2_v(self, new_v):
        self.v_2 = new_v

    def set_ch2_i(self, new_i):
        self.i_2 = new_i

    def set_ch1_active(self, state):
        if state is True:
            out_v, out_i = self._get_output(self.v_1, self.i_1, self.load_1)

        else:
            out_v, out_i = self.v_1, self.i_1

        print(out_v, out_i)

    def _get_output(self, v_set, i_set, load):
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
