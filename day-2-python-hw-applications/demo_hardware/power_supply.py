import sys
import socket
import traceback
import time
import numpy as np

from PyQt5 import QtWidgets, QtCore
from ui_power_supply import Ui_MainWindow


class PowerSupplyGui(QtWidgets.QMainWindow):

    def __init__(self):

        super(PowerSupplyGui, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ps_logic = PowerSupplyLogic()

        # Populate ch1 load combobox
        self.ui.ch1_load_comboBox.addItem('0')
        self.ui.ch1_load_comboBox.addItem('10')
        self.ui.ch1_load_comboBox.addItem('18.5')
        self.ui.ch1_load_comboBox.addItem('inf')

        self.load_dict = {
            '0' : 0,
            '10' : 10,
            '18.5' : 18.5,
            'inf' : np.inf
        }

        # Connect GUI input events
        self.ui.ch1_volt_dial.valueChanged.connect(self.gui_set_ch1_volt)
        self.ui.ch1_amps_dial.valueChanged.connect(self.gui_set_ch1_amps)
        self.ui.ch2_volt_dial.valueChanged.connect(self.gui_set_ch2_volt)
        self.ui.ch2_amps_dial.valueChanged.connect(self.gui_set_ch2_amps)

        self.ui.ch1_activate_radioButton.clicked.connect(self.gui_activate_ch1)
        self.ui.ch2_activate_radioButton.clicked.connect(self.gui_activate_ch2)

        self.ui.ch1_load_comboBox.currentIndexChanged.connect(self.set_ch1_load)

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
        if self.ui.ch1_activate_radioButton.isChecked():
            self.ps_logic.activate_output(0, True)

        else:
            self.ps_logic.activate_output(0, False)

    def gui_activate_ch2(self):
        if self.ui.ch2_activate_radioButton.isChecked():
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
        volt_dial = [self.ui.ch1_volt_dial, self.ui.ch2_volt_dial]
        amps_lcd = [self.ui.ch1_amps_lcdNumber, self.ui.ch2_amps_lcdNumber]
        amps_dial = [self.ui.ch1_amps_dial, self.ui.ch2_amps_dial]
        v_limit_led = [self.ui.ch1_v_limited_led_label, self.ui.ch2_v_limited_led_label]
        amps_limit_led = [self.ui.ch1_amps_limited_led_label, self.ui.ch2_amps_limited_led_label]
        active_button = [self.ui.ch1_activate_radioButton, self.ui.ch2_activate_radioButton]
        
        # Update dial, but block signals while doing so to prevent signal looping.
        volt_dial[channel].blockSignals(True)
        volt_dial[channel].setValue(self.ps_logic.get_v_set(channel)*10)  # value is 1/10 of slider pos to get pseudo float
        volt_dial[channel].blockSignals(False)

        if self.ps_logic.get_active_state(channel):
            active_button[channel].setChecked(True)
            volt_lcd[channel].display(self.ps_logic.get_v_act(channel))
            amps_lcd[channel].display(self.ps_logic.get_i_act(channel))

            if channel == 1:
                self.set_filament_colour(self.ps_logic.get_v_act(channel), self.ps_logic.get_i_act(channel))

            if self.ps_logic.get_v_act(channel) == self.ps_logic.get_v_set(channel):
                v_limit_led[channel].setStyleSheet(self.led_on_style)
                amps_limit_led[channel].setStyleSheet("")
            elif self.ps_logic.get_i_act(channel) == self.ps_logic.get_i_set(channel):
                amps_limit_led[channel].setStyleSheet(self.led_on_style)
                v_limit_led[channel].setStyleSheet("")

        # Otherwise channel is not active, so display set values.
        else:
            active_button[channel].setChecked(False)
            volt_lcd[channel].display(self.ps_logic.get_v_set(channel))
            amps_lcd[channel].display(self.ps_logic.get_i_set(channel))
            v_limit_led[channel].setStyleSheet("")
            amps_limit_led[channel].setStyleSheet("")

            if channel == 1:
                self.set_filament_colour(0, 0)

    def set_ch1_load(self):
        """ Respond to ch1 load combobox selection changing.
        """
        selection = self.ui.ch1_load_comboBox.currentText()
        newload = self.load_dict[selection]
        self.ps_logic.set_load(0, newload)

    def set_filament_colour(self, v, i):
        """ Set the drawn filament colour to correspond to the electrical output.
        """
        # Temp is proportional to power dissipated by filament
        power = v * i  
        
        # max power at 24 V is 96 W, corresponding to temperature of 4000 K
        temperature = 4000.0 * power / 96

        red = 255
        green = 190 * (np.sqrt(temperature/4000)) / (1 + np.exp(-0.005 * (temperature-800)))
        blue = 160 * (temperature/4000) / (1 + np.exp(-0.004 * (temperature-2000)))

        # Let the low colour temperatures be also less bright
        brightness = 1 / (1 + np.exp(-0.001 * (temperature-700)))

        red = red * brightness
        green = green * brightness
        blue = blue * brightness

        if red > 255:
            red = 255
        if green > 255:
            green = 255
        if blue > 255:
            blue = 255

        filament_style = ("QLabel { background-color: rgba(0, 0, 0, 255); "
                         + "color:rgba(" + str(int(red)) + ", " + str(int(green)) + ", " + str(int(blue)) + ", 255); }")
        
        self.ui.ch2_filament_label.setStyleSheet(filament_style)

    def shutdown(self):
        print("I'm shutting down")
        self.ps_logic.shutdown()


class PowerSupplyLogic(QtCore.QObject):
    """ Provides the logic associated with the virtual power supply.
    """

    # Signals for the GUI to listen to for changes to power supply settings.
    outputs_updated_signal = QtCore.pyqtSignal(int)

    start_tcp_server_signal = QtCore.pyqtSignal()

    def __init__(self):
        super(PowerSupplyLogic, self).__init__()

        self.load = [0, 6]

        self._v_set = [0, 0]
        self._i_set = [0, 0]

        self._v_act = [0, 0]
        self._i_act = [0, 0]

        self._active = [False, False]

        # Start TCP server to listen for remote commands
        self.socket_thread = QtCore.QThread()
        self.rc_server = RemoteControlServer()
        self.rc_server.moveToThread(self.socket_thread)
        self.socket_thread.started.connect(self.rc_server.startup)
        self.rc_server.new_command.connect(self.handle_remote_command)
        self.socket_thread.start()

        # Dictionary of allowable arguments 
        self.arg_parser = {
            'True': True,
            'T': True,
            'true': True,
            'False': False,
            'F': False,
            'false': False,
            True : True,
            False : False,
        }

        for i in np.linspace(0,30, 301):
            self.arg_parser[str(i)] = i

        # Define command set
        self.command_dict = {'setactive': self.activate_output,
                             'v_set': self.set_voltage,
                             'i_set': self.set_current,
                             'v_set?' : self.get_v_set,
                             'i_set?' : self.get_i_set,
                             'v_act?' : self.get_v_act,
                             'i_set?' : self.get_i_act,
                             '*IDN?' : self.get_dev_id
        }
    
    def get_dev_id(self, rc=False):
        """ Get the device ID

            Parameters
            -------
                rc: bool, optional
                    Flag that decides whether or not to send a reply
                    via the remove server
            
            Returns
            -------
                none

            If the rc flag is set to True, this function sends a
            string containing a device identifier via the remote server.
        """
        if rc:
            self.rc_server.send('EQUS PY19 Power Supply')

    def set_voltage(self, channel, new_v, rc=False):
        """ Set a new output voltage on a given channel

            Parameters
            -------
                channel : int
                    The channel of the power supply. Can be 0 or 1

                new_v : float
                    The desired output voltage for the given channel

                rc: bool, optional
                    Flag that decides whether or not to send a reply
                    via the remove server
            
            Returns
            -------
                none

            If the rc flag is set to True, this function sends a
            string containing the new voltage via the remote server.
        """
        self._v_set[channel] = new_v
        self._update_output(channel)

        if rc:
            self.rc_server.send('{}'.format(new_v))

    def set_current(self, channel, new_i, rc=False):
        """ Set a new output current on a given channel

            Parameters
            -------
                channel : int
                    The channel of the power supply. Can be 0 or 1

                new_i : float
                    The desired output current for the given channel

                rc: bool, optional
                    Flag that decides whether or not to send a reply
                    via the remove server
            
            Returns
            -------
                none

            If the rc flag is set to True, this function sends a
            string containing the new current via the remote server.
        """
        self._i_set[channel] = new_i
        self._update_output(channel)

        if rc:
            self.rc_server.send('{}'.format(new_i))

    def get_v_act(self, channel, rc=False):
        """ Gets the output voltage on a given channel

            Parameters
            -------
                channel : int
                    The channel of the power supply. Can be 0 or 1

                rc: bool, optional
                    Flag that decides whether or not to send a reply
                    via the remove server
            
            Returns
            -------
                float
                    The output voltage on the given channel

            If the rc flag is set to True, this function sends a
            string containing the current voltage via the remote server.
        """
        if rc:
            self.rc_server.send('{}'.format(self._v_act[channel]))

        return self._v_act[channel]

    def get_i_act(self, channel, rc=False):
        """ Gets the output current on a given channel

            Parameters
            -------
                channel : int
                    The channel of the power supply. Can be 0 or 1

                rc: bool, optional
                    Flag that decides whether or not to send a reply
                    via the remove server
            
            Returns
            -------
                float
                    The output current on the given channel

            If the rc flag is set to True, this function sends a
            string containing the output current via the remote server.
        """
        if rc:
            self.rc_server.send('{}'.format(self._i_act[channel]))

        return self._i_act[channel]

    def get_v_set(self, channel, rc=False):
        """ Gets the nominal voltage on a given channel

            Parameters
            -------
                channel : int
                    The channel of the power supply. Can be 0 or 1

                rc: bool, optional
                    Flag that decides whether or not to send a reply
                    via the remove server
            
            Returns
            -------
                float
                    The nominal voltage on the given channel

            If the rc flag is set to True, this function sends a
            string containing the nominal voltage via the remote server.
        """
        if rc:
            self.rc_server.send('{}'.format(self._v_set[channel]))

        return self._v_set[channel]

    def get_i_set(self, channel, rc=False):
        """ Gets the nominal output current on a given channel

            Parameters
            -------
                channel : int
                    The channel of the power supply. Can be 0 or 1

                rc: bool, optional
                    Flag that decides whether or not to send a reply
                    via the remove server
            
            Returns
            -------
                float
                    The nominal current on the given channel

            If the rc flag is set to True, this function sends a
            string containing the nominal current via the remote server.
        """
        if rc:
            self.rc_server.send('{}'.format(self._i_set[channel]))

        return self._i_set[channel]

    def get_active_state(self, channel, rc=False):
        """ Gets the output state on a given channel

            Parameters
            -------
                channel : int
                    The channel of the power supply. Can be 0 or 1

                rc: bool, optional
                    Flag that decides whether or not to send a reply
                    via the remove server
            
            Returns
            -------
                int
                    The output state on the given channel

            If the rc flag is set to True, this function sends a
            string containing the output state via the remote server.
        """

        if rc:
            self.rc_server.send('{}'.format(self._active[channel]))

        return self._active[channel]

    def activate_output(self, channel, state, rc=False):
        """ Modifies the output state on a given channel

            Parameters
            -------
                channel : int
                    The channel of the power supply. Can be 0 or 1
                
                state : int
                    The desired output state. Can be 0 (output off)
                    or 1 (output on)

                rc: bool, optional
                    Flag that decides whether or not to send a reply
                    via the remove server
            
            Returns
            -------
                none

            If the rc flag is set to True, this function sends a
            string containing whether the channel has been activated
            or deactivated via the remote server.
        """
        if state is not self._active[channel]:
            self._active[channel] = state
            self._update_output(channel)

        if rc:
            if state:
                self.rc_server.send('activated {}'.format(channel))
            else:
                self.rc_server.send('deactivated {}'.format(channel))
            

    def _update_output(self, channel):
        """ Private method that modifies the output state of a given
            channel. See class method activate_output.
        """
        if self._active[channel] and channel == 0:
            out_v, out_i = self._calc_output(self._v_set[channel],
                                             self._i_set[channel],
                                             self.load[channel]
                                            )

        elif self._active[channel] and channel == 1:
            out_v, out_i = self._calc_filament_output(self._v_set[channel],
                                                      self._i_set[channel]
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
        # If no load, then max current regardless of V setting
        if load == 0:
            return 0, i_set

        # Now we consider Ohm's law
        out_v = i_set * load

        if out_v <= v_set:  # We are current limited
            return out_v, i_set

        # Otherwise we are voltage limited
        else:
            out_i = v_set / load
            return v_set, out_i

    def _calc_filament_output(self, v_set, i_set):
        """Calculate the actual output V and I for a tungsten filament load with varying resistance.
        """
        # We will assume that I as a function of V is a kind of ln(V) shape.
        #
        # Take    I = 1.8 * ln (V + 1)

        # Assume I limited.
        out_v = np.exp(i_set / 1.8) - 1

        if out_v <= v_set:  # current limited is correct
            return out_v, i_set

        # Otherwise we are voltage limited
        else:
            out_i = 1.8 * np.log(v_set + 1)
            return v_set, out_i

    def set_load(self, channel, load):
        """Set a new load resistance on a channel.
        """
        self.load[channel] = load
        self._update_output(channel)

    def handle_remote_command(self, command):
        """Parse the remote command and perform the desired action.

        @param command: bytes-encoded command received over socket.
        """
        cmd = command.decode()

        args = ['']
        try:
            method, args = cmd.split(':')
            args = args.split(';')

            for i, arg in enumerate(args):
                if arg in self.arg_parser:
                    args[i] = self.arg_parser[arg]
                elif arg.isdigit():
                    args[i] = int(arg)
                elif '.' in arg:
                    arg_parts = arg.split('.')
                    if (len(arg_parts) == 2 and not False in [p.isdigit() for p in arg_parts]):
                        args[i] = float(arg)
                    else:
                        print('Found a dot in {} but cannot read it as a float.'.format(arg))
                        self.rc_server.send('-3')
                        return
                else:
                    print('No idea what {} means!'.format(arg))
                    self.rc_server.send('-3')
                    return

        except ValueError:
            method = cmd
            if method != '*IDN?':
                self.rc_server.send('-4')

        args.append(True)

        if method == '*IDN?':
            args = [True]

        if method in self.command_dict.keys():
            handler = self.command_dict[method]
            return handler(*args)
        else:
            self.rc_server.send('-7')
    
    def shutdown(self):
        self.rc_server.stop()


class RemoteControlServer(QtCore.QObject):

    new_command = QtCore.pyqtSignal(str if sys.version_info.major <= 2 else bytes)

    def __init__(self):
        super(RemoteControlServer, self).__init__()

        self.HOST = '127.0.0.1'
        self.PORT = 65431
        self.REPLY_WAIT = 0.1
        self.is_running = False

        self.active = True
        self.connection = None

        self.recv_buffer = bytes()
        self.send_buffer = bytes()

    def startup(self):
        """Start the socket and wait for connection."""
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.settimeout(1.0)
        self.s.bind((self.HOST, self.PORT))
        self.s.listen(0)

        # Cycle through and wait for a connection
        try:
            sys.stdout.flush()
        except:
            pass

        while self.active:
            try:
                connection, address = self.s.accept()
                break
            except socket.timeout as ex:
                print(".", end='')
                try:
                    sys.stdout.flush()
                except:
                    pass

        print('Connected by', address)

        self.loop(connection)

    def loop(self, connection):
        """Message handling loop"""
        while self.active:
            try:
                self.recv_buffer += connection.recv(1024)
            except socket.timeout:
                print('TimeOut')
            except socket.error as ex:
                print(ex)
            else:
                cmd = self.recv_buffer
                self.recv_buffer = bytes()
                self.new_command.emit(cmd)

                    # Give the instrument time to generate a response
                while not self.send_buffer:
                    time.sleep(self.REPLY_WAIT)

                connection.sendall(self.send_buffer)
                self.send_buffer = bytes()

    def send(self, message):
        """Fill send buffer with data to send back to the client."""
        self.send_buffer += message.encode()
        self.send_buffer += '\n'.encode()  # separate messages on new lines

    def stop(self):
        self.s.close()
        sys.exit()


def main():
    app = QtWidgets.QApplication([])
    application = PowerSupplyGui()
    application.show()
    app.aboutToQuit.connect(application.shutdown)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
