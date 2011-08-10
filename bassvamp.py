#!/bin/env python

import sys
import os
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication, QMainWindow
from qt_bassvamp import Ui_mainWindow
from oo_bassvamp import BVamp

FX_List = [
["VCF + Flanger", "VCF Mix", "Flanger Mix", "Depth", "Flanger Feedback", "VCF Freq", "VCF Q", "VCF Speed"],
["Delay + Chorus", "Delay Mix", "Chorus Mix", "Feedback", "Feedback LP", "Depth", "Delay Time", "-"],
["Stereo Delay", "Delay Mix", "Feedback", "-", "Feedback LP", "-", "Delay Time", "-"],
["Delay / Loop", "Delay Mix", "Feedback", "-", "-", "-", "Delay Time", "-"],
["Reverb", "Reverb Mix", "Decay", "Damping", "Diffusion", "-", "-", "-"],
["Ambience", "Ambience", "Decay", "Size", "-", "-", "-", "-"],
["Voice Box", "Mix", "Vowel", "Pedal", "-", "-", "-", "Speed"],
["Ultrabass", "SubMix", "Sensitivity", "-", "-", "-", "-", "-"],
["Rotary Cab", "Mix", "Balance", "Split Freq", "-", "-", "-", "Speed"],
["Phaser", "Mix", "Feedback", "Feedback LP", "Stereo Spread", "-", "-", "Speed"],
["Flanger", "Mix", "Depth", "Intensity", "-", "-", "-", "-"],
["Chorus", "Mix", "Depth", "Intensity", "-", "-", "-", "-"],
["Stereo Chorus", "Mix", "Depth", "Intensity", "-", "-", "-", "-"],
["Synth", "Synth Mix", "Variation", "-", "Interval", "Key", "-", "-"],
["MIDI Synth", "Synth Mix", "Variation", "-", "-", "Reverb", "-", "-"],
["No FX", "-", "-", "-", "-", "-", "-", "-"] ]

Split_Steps = [ 41, 49, 58, 70, 84, 101, 121, 145, 174, 209, 251, 301, 362,
		416, 470, 531, 600 ]

class Bass_Vamp(QMainWindow, Ui_mainWindow, BVamp):
	def __init__(self):
		self.path = os.getcwd()
		self.needs_refresh = True
		QMainWindow.__init__(self)
		BVamp.__init__(self)

		# Set up the user interface from Designer.
		self.setupUi(self)

		# Volume dial
		QtCore.QObject.connect(self.Volume_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.Volume_Label_2.setNum) 
		# Gain dial
		QtCore.QObject.connect(self.Gain_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.Gain_Label_2.setNum) 
		# Bass dial
		QtCore.QObject.connect(self.Bass_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.Bass_Label_2.setNum) 
		# Mid dial
		QtCore.QObject.connect(self.Mid_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.Mid_Label_2.setNum) 
		# Treble dial
		QtCore.QObject.connect(self.Treble_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.Treble_Label_2.setNum) 
		# Deep dial
		QtCore.QObject.connect(self.Deep_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.Deep_Label_2.setNum) 
		# Shift dial
		QtCore.QObject.connect(self.Shift_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.Shift_Label_2.setNum) 
		# Presence dial
		QtCore.QObject.connect(self.Presence_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.Presence_Label_2.setNum) 
		# Split dial
		QtCore.QObject.connect(self.Split_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.show_split_freq) 
		# Drive dial
		QtCore.QObject.connect(self.Drive_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.Drive_Label_2.setNum) 
		# Tone dial
		QtCore.QObject.connect(self.Tone_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.Tone_Label_2.setNum) 
		# Boost dial
		QtCore.QObject.connect(self.Boost_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.Boost_Label_2.setNum) 
		# Depth dial
		QtCore.QObject.connect(self.Depth_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.Depth_Label_2.setNum) 
		# Speed dial
		QtCore.QObject.connect(self.Speed_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.Speed_Label_2.setNum) 
		# Base dial
		QtCore.QObject.connect(self.Base_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.Base_Label_2.setNum) 
		# Density dial
		QtCore.QObject.connect(self.Density_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.Density_Label_2.setNum) 
		# Attack dial
		QtCore.QObject.connect(self.Attack_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.Attack_Label_2.setNum) 
		# FX Param1 dial
		QtCore.QObject.connect(self.FXparm1_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.FXparm1_Label_2.setNum) 
		# FX Param2 dial
		QtCore.QObject.connect(self.FXparm2_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.FXparm2_Label_2.setNum) 
		# FX Param3 dial
		QtCore.QObject.connect(self.FXparm3_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.FXparm3_Label_2.setNum) 
		# FX Param4 dial
		QtCore.QObject.connect(self.FXparm4_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.FXparm4_Label_2.setNum) 
		# FX Param5 dial
		QtCore.QObject.connect(self.FXparm5_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.FXparm5_Label_2.setNum) 
		# FX Param6 dial
		QtCore.QObject.connect(self.FXparm6_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.FXparm6_Label_2.setNum) 
		# FX Param7 dial
		QtCore.QObject.connect(self.FXparm7_Dial, \
				QtCore.SIGNAL("valueChanged(int)"), \
				self.FXparm7_Label_2.setNum) 
		# Amp radiobutton 
		QtCore.QObject.connect(self.Amp_Radio, \
				QtCore.SIGNAL("toggled(bool)"), \
				self.manage_amp_simulation)
		# Cabinet radiobutton 
		QtCore.QObject.connect(self.Cabinet_Radio, \
				QtCore.SIGNAL("toggled(bool)"), \
				self.manage_cabinet_simulation)
		# StompBox radiobutton 
		QtCore.QObject.connect(self.Stomp_Radio, \
				QtCore.SIGNAL("toggled(bool)"), \
				self.manage_stomp_simulation)
		# Wah radiobutton 
		QtCore.QObject.connect(self.Wah_Radio, \
				QtCore.SIGNAL("toggled(bool)"), \
				self.manage_wah_simulation)
		# Compressor radiobutton 
		QtCore.QObject.connect(self.Compressor_Radio, \
				QtCore.SIGNAL("toggled(bool)"), \
				self.manage_compressor)
		# FX radiobutton 
		QtCore.QObject.connect(self.FX_Radio, \
				QtCore.SIGNAL("toggled(bool)"), \
				self.manage_fx)
		# FX combo 
		QtCore.QObject.connect(self.FX_Combo, \
				QtCore.SIGNAL("currentIndexChanged(const QString&)"), \
				self.enable_all_fx_params) 
		# Preset lineEdit 
		QtCore.QObject.connect(self.Preset_lineEdit, \
				QtCore.SIGNAL("editingFinished()"), \
				self.change_preset_name) 
		# Load From File action
		QtCore.QObject.connect(self.actionLoad_From_File, \
				QtCore.SIGNAL("triggered()"), \
				self.select_file_to_open) 
		# Load From Device action
		QtCore.QObject.connect(self.actionLoad_From_Device, \
				QtCore.SIGNAL("triggered()"), \
				self.read_vamp_preset) 
		# Save To File action 
		QtCore.QObject.connect(self.actionSave_To_File, \
				QtCore.SIGNAL("triggered()"), \
				self.select_file_to_save) 
		# Save To Device action 
		QtCore.QObject.connect(self.actionSave_To_Device, \
				QtCore.SIGNAL("triggered()"), \
				self.write_vamp_preset) 
		# Select MIDI Device action 
		QtCore.QObject.connect(self.actionSelect_MIDI_device, \
				QtCore.SIGNAL("triggered()"), \
				self.config_midi_interface)
		# Quit action 
		QtCore.QObject.connect(self.actionQuit, \
				QtCore.SIGNAL("triggered()"), \
				sys.exit) 
		QtCore.QMetaObject.connectSlotsByName(self) 


	def select_midi_device(self, devlist, index):
		aux = QtGui.QInputDialog()
		aux.setOption(aux.UseListViewForComboBoxItems, False)
		aux.adjustSize()
		device, ok = aux.getItem(self, "Select MIDI Device", \
				"Devices:", devlist, index, False) 
		if ok == 0: # cancel was pressed
			ret = None
		else:
			ret = str(device.toAscii())
		return ret

	def config_midi_interface(self):
		devlist = self.list_midi_devices()
		if devlist == []:
			self.warning_msg("No MIDI devices found!")
			return
		index = 0
		# if midi was already configured, point to the current device
		if self.midi:
			# find current index and highlight it
			try:
				index = devlist.index(self.midi)
			except(ValueError):
				index = 0

		mididevice = self.select_midi_device(devlist, index)
		self.print_msg(mididevice + "\n")
		if mididevice == None:
			self.warning_msg("No MIDI device selected!")
			return

		text, self.midi = self.setup_midi(mididevice)
		self.print_msg(text)

	def write_vamp_preset(self):
		if not self.midi:
			self.config_midi_interface()
		if not self.midi:
			self.warning_msg("No midi device selected\n")
			return
		self.needs_refresh = True
		#before = self.convert_preset_to_ascii()
		self.apply_changes_to_preset()
		#after = self.convert_preset_to_ascii()
		#self.print_msg("Original: %s\n" % before)
		#self.print_msg("Modified: %s\n" % after)
		msg = "Writing %s\n" % self.get_preset_name(self.data)
		self.print_msg(msg)
		self.write_current_preset()

	def read_vamp_preset(self):
		if not self.midi:
			self.config_midi_interface()
		if not self.midi:
			self.warning_msg("No midi device selected\n")
			return
		index = self.prepare_preset_list()
		if index < 0:
			self.print_msg("No Preset selected!\n")
			return
		self.get_preset_from_data(index)
		self.get_values_from_preset()

	def print_msg(self, msg):
		text = QtCore.QString(msg)
		self.textBrowser.insertPlainText(text)
		self.textBrowser.update()

	def warning_msg(self, msg):
        	QtGui.QMessageBox.warning(self,
                            "Warning", msg)

	def critical_msg(self, msg):
        	QtGui.QMessageBox.critical(self,
                            "Error", msg)

	def get_values_from_preset(self):
		# Preset Label
		name = "%s" % self.get_preset_name(self.data)
		self.print_msg("%s\n" % name)
		self.Preset_lineEdit.setText(QtCore.QString(name))
		# Dials
		self.Volume_Dial.setValue(self.read_volume(self.data))
		self.Gain_Dial.setValue(self.read_gain(self.data))
		self.Bass_Dial.setValue(self.read_bass(self.data))
		self.Mid_Dial.setValue(self.read_mid(self.data))
		self.Treble_Dial.setValue(self.read_treble(self.data))
		self.Deep_Dial.setValue(self.read_deep(self.data))
		self.Shift_Dial.setValue(self.read_shift(self.data))
		self.Presence_Dial.setValue(self.read_presence(self.data))
		# Combo Boxes
		self.Amp_Combo.setCurrentIndex(self.read_amp(self.data))
		self.Cabinet_Combo.setCurrentIndex(self.read_cabinet(self.data))
		# composite values
		self.get_stomp_values()
		self.get_wah_values()
		self.get_compressor_values()
		self.get_fx_values()
		if self.Amp_Combo.currentIndex() == 32:
			self.Amp_Radio.setChecked(False)
		else:
			self.Amp_Radio.setChecked(True)

		if self.Cabinet_Combo.currentIndex() == 0:
			self.Cabinet_Radio.setChecked(False)
		else:
			self.Cabinet_Radio.setChecked(True)

		if self.Stomp_Combo.currentIndex() == 0:
			self.Stomp_Radio.setChecked(False)
		else:
			self.Stomp_Radio.setChecked(True)

		if (self.Wah_Combo.currentIndex() == 0) and \
				(self.Depth_Dial.value() == 0):
			self.Wah_Radio.setChecked(False)
		else:
			self.Wah_Radio.setChecked(True)

		if self.Density_Dial.value() == 0:
			self.Compressor_Radio.setChecked(False)
		else:
			self.Compressor_Radio.setChecked(True)

		if self.read_fxtype(self.data) == 15:
			self.FX_Radio.setChecked(False)
		else:
			self.FX_Radio.setChecked(True)

		self.manage_amp_simulation()
		self.manage_cabinet_simulation()
		self.manage_stomp_simulation()
		self.manage_wah_simulation()
		self.manage_compressor()
		self.manage_fx()

	def apply_changes_to_preset(self):
		self.set_preset_name(self.Preset_lineEdit.text().toAscii())
		self.set_volume(self.Volume_Dial.value())
		self.set_gain(self.Gain_Dial.value())
		self.set_bass(self.Bass_Dial.value())
		self.set_mid(self.Mid_Dial.value())
		self.set_treble(self.Treble_Dial.value())
		self.set_deep(self.Deep_Dial.value())
		self.set_shift(self.Shift_Dial.value())
		self.set_presence(self.Presence_Dial.value())
		self.set_depth(self.Depth_Dial.value())
		self.set_speed(self.Speed_Dial.value())
		self.set_base(self.Base_Dial.value())
		self.set_split(self.Split_Dial.value())
		self.set_drive(self.Drive_Dial.value())
		self.set_tone(self.Tone_Dial.value())
		self.set_boost(self.Boost_Dial.value())
		self.set_density(self.Density_Dial.value())
		self.set_attack(self.Attack_Dial.value())
		# Combo boxes
		self.set_amp(self.Amp_Combo.currentIndex())
		self.set_cabinet(self.Cabinet_Combo.currentIndex())
		self.set_stomp(self.Stomp_Combo.currentIndex())
		self.set_wah(self.Wah_Combo.currentIndex())
		# FX
		if self.FX_Radio.isChecked():
			self.set_fx(0x7F)
		else:
			self.set_fx(0)
		self.set_fxtype(self.FX_Combo.currentIndex())
		self.set_fxparm1(self.FXparm1_Dial.value())
		self.set_fxparm2(self.FXparm2_Dial.value())
		self.set_fxparm3(self.FXparm3_Dial.value())
		self.set_fxparm4(self.FXparm4_Dial.value())
		self.set_fxparm5(self.FXparm5_Dial.value())
		self.set_fxparm6(self.FXparm6_Dial.value())
		self.set_fxparm7(self.FXparm7_Dial.value())
		# self.set_(self._Dial.value()))

	def load_preset_file(self, fname):
		text = QtCore.QString(fname.split('/')[-1])
		self.print_msg("loading from  %s \n" % fname)
		self.Preset_lineEdit.setText(text)
		self.load_preset_from_file(fname)
		self.get_values_from_preset()

	def manage_amp_simulation(self):
		if self.Amp_Radio.isChecked():
			self.Amp_Combo.setEnabled(True)
		else:
			self.Amp_Combo.setCurrentIndex(32)
			self.Amp_Combo.setEnabled(False)

	def manage_cabinet_simulation(self):
		if self.Cabinet_Radio.isChecked():
			self.Cabinet_Combo.setEnabled(True)
		else:
			self.Cabinet_Combo.setCurrentIndex(0)
			self.Cabinet_Combo.setEnabled(False)

	def manage_stomp_simulation(self):
		if self.Stomp_Radio.isChecked():
			self.enable_stomp()
			self.get_stomp_values()
		else:
			self.disable_stomp()

	def manage_wah_simulation(self):
		if self.Wah_Radio.isChecked():
			self.enable_wah()
			self.get_wah_values()
		else:
			self.disable_wah()

	def manage_compressor(self):
		if self.Compressor_Radio.isChecked():
			self.enable_compressor()
			self.get_compressor_values()
		else:
			self.disable_compressor()

	def manage_fx(self):
		if self.FX_Radio.isChecked():
			self.enable_fx()
			self.get_fx_values()
		else:
			self.disable_fx()

	def enable_stomp(self):
		self.Split_Dial.setEnabled(True)
		self.Split_Label.setEnabled(True)
		self.Split_Label_2.setEnabled(True)
		self.Drive_Dial.setEnabled(True)
		self.Drive_Label.setEnabled(True)
		self.Drive_Label_2.setEnabled(True)
		self.Tone_Dial.setEnabled(True)
		self.Tone_Label.setEnabled(True)
		self.Tone_Label_2.setEnabled(True)
		self.Boost_Dial.setEnabled(True)
		self.Boost_Label.setEnabled(True)
		self.Boost_Label_2.setEnabled(True)
		self.Stomp_Combo.setEnabled(True)

	def enable_wah(self):
		self.Depth_Dial.setEnabled(True)
		self.Depth_Label.setEnabled(True)
		self.Depth_Label_2.setEnabled(True)
		self.Speed_Dial.setEnabled(True)
		self.Speed_Label.setEnabled(True)
		self.Speed_Label_2.setEnabled(True)
		self.Base_Dial.setEnabled(True)
		self.Base_Label.setEnabled(True)
		self.Base_Label_2.setEnabled(True)
		self.Wah_Combo.setEnabled(True)

	def enable_compressor(self):
		self.Density_Dial.setEnabled(True)
		self.Density_Label.setEnabled(True)
		self.Density_Label_2.setEnabled(True)
		self.Attack_Dial.setEnabled(True)
		self.Attack_Label.setEnabled(True)
		self.Attack_Label_2.setEnabled(True)

	def enable_fx(self):
		self.FX_Combo.setEnabled(True)
		self.enable_all_fx_params()

	def enable_all_fx_params(self):
		self.enable_fx_param1()
		self.enable_fx_param2()
		self.enable_fx_param3()
		self.enable_fx_param4()
		self.enable_fx_param5()
		self.enable_fx_param6()
		self.enable_fx_param7()

	def enable_fx_param1(self):
		text = self.get_fx_param_name(1)
		self.FXparm1_Label.setText(QtCore.QString(text))
		if text == "-":
			self.disable_fx_param1()
			return
		self.FXparm1_Dial.setEnabled(True)
		self.FXparm1_Label.setEnabled(True)
		self.FXparm1_Label_2.setEnabled(True)

	def enable_fx_param2(self):
		text = self.get_fx_param_name(2)
		self.FXparm2_Label.setText(QtCore.QString(text))
		if text == "-":
			self.disable_fx_param2()
			return
		self.FXparm2_Dial.setEnabled(True)
		self.FXparm2_Label.setEnabled(True)
		self.FXparm2_Label_2.setEnabled(True)

	def enable_fx_param3(self):
		text = self.get_fx_param_name(3)
		self.FXparm3_Label.setText(QtCore.QString(text))
		if text == "-":
			self.disable_fx_param3()
			return
		self.FXparm3_Dial.setEnabled(True)
		self.FXparm3_Label.setEnabled(True)
		self.FXparm3_Label_2.setEnabled(True)

	def enable_fx_param4(self):
		text = self.get_fx_param_name(4)
		self.FXparm4_Label.setText(QtCore.QString(text))
		if text == "-":
			self.disable_fx_param4()
			return
		self.FXparm4_Dial.setEnabled(True)
		self.FXparm4_Label.setEnabled(True)
		self.FXparm4_Label_2.setEnabled(True)

	def enable_fx_param5(self):
		text = self.get_fx_param_name(5)
		self.FXparm5_Label.setText(QtCore.QString(text))
		if text == "-":
			self.disable_fx_param5()
			return
		self.FXparm5_Dial.setEnabled(True)
		self.FXparm5_Label.setEnabled(True)
		self.FXparm5_Label_2.setEnabled(True)

	def enable_fx_param6(self):
		text = self.get_fx_param_name(6)
		self.FXparm6_Label.setText(QtCore.QString(text))
		if text == "-":
			self.disable_fx_param6()
			return
		self.FXparm6_Dial.setEnabled(True)
		self.FXparm6_Label.setEnabled(True)
		self.FXparm6_Label_2.setEnabled(True)

	def enable_fx_param7(self):
		idx = self.FX_Combo.currentIndex()
		text = FX_List[idx][7]
		self.FXparm7_Label.setText(QtCore.QString(text))
		if text == "-":
			self.disable_fx_param7()
			return
		self.FXparm7_Dial.setEnabled(True)
		self.FXparm7_Label.setEnabled(True)
		self.FXparm7_Label_2.setEnabled(True)

	def get_fx_param_name(self, num):
		idx = self.FX_Combo.currentIndex()
		return FX_List[idx][num]

	def disable_stomp(self):
		self.Stomp_Combo.setCurrentIndex(0)
		self.Split_Dial.setEnabled(False)
		self.Split_Label.setEnabled(False)
		self.Split_Label_2.setEnabled(False)
		self.Drive_Dial.setEnabled(False)
		self.Drive_Label.setEnabled(False)
		self.Drive_Label_2.setEnabled(False)
		self.Tone_Dial.setEnabled(False)
		self.Tone_Label.setEnabled(False)
		self.Tone_Label_2.setEnabled(False)
		self.Boost_Dial.setEnabled(False)
		self.Boost_Label.setEnabled(False)
		self.Boost_Label_2.setEnabled(False)
		self.Stomp_Combo.setEnabled(False)

	def disable_wah(self):
		# Wah Wah disabled is Midi Wah + Depth = 0 
		self.Wah_Combo.setCurrentIndex(0)
		self.Depth_Dial.setValue(0)
		self.Depth_Dial.setEnabled(False)
		self.Depth_Label.setEnabled(False)
		self.Depth_Label_2.setEnabled(False)
		self.Speed_Dial.setEnabled(False)
		self.Speed_Label.setEnabled(False)
		self.Speed_Label_2.setEnabled(False)
		self.Base_Dial.setEnabled(False)
		self.Base_Label.setEnabled(False)
		self.Base_Label_2.setEnabled(False)
		self.Wah_Combo.setEnabled(False)

	def disable_compressor(self):
		# Compressor disabled is Density = 0 
		self.Density_Dial.setValue(0)
		self.Density_Dial.setEnabled(False)
		self.Density_Label.setEnabled(False)
		self.Density_Label_2.setEnabled(False)
		self.Attack_Dial.setEnabled(False)
		self.Attack_Label.setEnabled(False)
		self.Attack_Label_2.setEnabled(False)

	def disable_fx(self):
		self.disable_all_fx_params()
		self.FX_Combo.setCurrentIndex(15)
		self.FX_Combo.setEnabled(False)

	def disable_all_fx_params(self):
		self.disable_fx_param1()
		self.disable_fx_param2()
		self.disable_fx_param3()
		self.disable_fx_param4()
		self.disable_fx_param5()
		self.disable_fx_param6()
		self.disable_fx_param7()

	def disable_fx_param1(self):
		self.FXparm1_Dial.setEnabled(False)
		self.FXparm1_Label.setEnabled(False)
		self.FXparm1_Label_2.setEnabled(False)

	def disable_fx_param2(self):
		self.FXparm2_Dial.setEnabled(False)
		self.FXparm2_Label.setEnabled(False)
		self.FXparm2_Label_2.setEnabled(False)

	def disable_fx_param3(self):
		self.FXparm3_Dial.setEnabled(False)
		self.FXparm3_Label.setEnabled(False)
		self.FXparm3_Label_2.setEnabled(False)

	def disable_fx_param4(self):
		self.FXparm4_Dial.setEnabled(False)
		self.FXparm4_Label.setEnabled(False)
		self.FXparm4_Label_2.setEnabled(False)

	def disable_fx_param5(self):
		self.FXparm5_Dial.setEnabled(False)
		self.FXparm5_Label.setEnabled(False)
		self.FXparm5_Label_2.setEnabled(False)

	def disable_fx_param6(self):
		self.FXparm6_Dial.setEnabled(False)
		self.FXparm6_Label.setEnabled(False)
		self.FXparm6_Label_2.setEnabled(False)

	def disable_fx_param7(self):
		self.FXparm7_Dial.setEnabled(False)
		self.FXparm7_Label.setEnabled(False)
		self.FXparm7_Label_2.setEnabled(False)

	def get_stomp_values(self):
		self.Stomp_Combo.setCurrentIndex(self.read_stomp(self.data))
		self.Split_Dial.setValue(self.read_split(self.data))
		self.Drive_Dial.setValue(self.read_drive(self.data))
		self.Tone_Dial.setValue(self.read_tone(self.data))
		self.Boost_Dial.setValue(self.read_boost(self.data))

	def get_wah_values(self):
		self.Wah_Combo.setCurrentIndex(self.read_wah(self.data))
		self.Depth_Dial.setValue(self.read_depth(self.data))
		self.Speed_Dial.setValue(self.read_speed(self.data))
		self.Base_Dial.setValue(self.read_base(self.data))

	def get_compressor_values(self):
		self.Density_Dial.setValue(self.read_density(self.data))
		self.Attack_Dial.setValue(self.read_attack(self.data))

	def get_fx_values(self):
		self.FX_Combo.setCurrentIndex(self.read_fxtype(self.data))
		self.FXparm1_Dial.setValue(self.read_fxparm1(self.data))
		self.FXparm2_Dial.setValue(self.read_fxparm2(self.data))
		self.FXparm3_Dial.setValue(self.read_fxparm3(self.data))
		self.FXparm4_Dial.setValue(self.read_fxparm4(self.data))
		self.FXparm5_Dial.setValue(self.read_fxparm5(self.data))
		self.FXparm6_Dial.setValue(self.read_fxparm6(self.data))
		self.FXparm7_Dial.setValue(self.read_fxparm7(self.data))

	def show_split_freq(self):
		idx = self.Split_Dial.value()
		freq = "%d Hz" % Split_Steps[idx]
		self.Split_Label_2.setText(QtCore.QString(freq))

	def change_preset_name(self):
		self.set_preset_name(self.Preset_lineEdit.text().toAscii())

	def select_file_to_open(self):
		filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File',
				self.path, '*.syx')
		if filename == '':
			return
		fname = filename.split('/')[-1]
		self.path = filename[:-(len(fname))]
		self.load_preset_file(filename)
		self.remove_modified_flag()

	def select_file_to_save(self):
		filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File',
				self.path, '*.syx')
		if filename == '':
			return
		self.apply_changes_to_preset()
		fname = filename.split('/')[-1]
		self.path = filename[:-(len(fname))]
		self.save_preset_to_file(filename)
		self.remove_modified_flag()

	def set_modified_flag(self):
		self.modified = 1
		palette = QtGui.QPalette()
		brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Active, \
				 QtGui.QPalette.WindowText, brush)
		self.Preset_Label.setPalette(palette)

	def remove_modified_flag(self):
		self.modified = 0
		palette = QtGui.QPalette()
		brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
		brush.setStyle(QtCore.Qt.SolidPattern)
		palette.setBrush(QtGui.QPalette.Active, \
				 QtGui.QPalette.WindowText, brush)
		self.Preset_Label.setPalette(palette)

	def prepare_preset_list(self):
		dialog = QtGui.QDialog()
		dialog.setObjectName("dialog")
		dialog.resize(810, 630)

		buttonBox = QtGui.QDialogButtonBox(dialog)
		buttonBox.setGeometry(QtCore.QRect(450, 580, 341, 32))
		buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel| \
						QtGui.QDialogButtonBox.Ok)
		buttonBox.setObjectName("buttonBox")
		QtCore.QMetaObject.connectSlotsByName(dialog)
		table = QtGui.QTableWidget(25,5, dialog)
		table.setGeometry(QtCore.QRect(70, 50, 661, 501))
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, \
						 QtGui.QSizePolicy.Maximum)
		sizePolicy.setHorizontalStretch(1)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(table.sizePolicy().hasHeightForWidth())
		table.setSizePolicy(sizePolicy)
		table.setShowGrid(True)
		table.setGridStyle(QtCore.Qt.SolidLine)
		table.setCornerButtonEnabled(True)
		table.setHorizontalHeaderLabels(["A","B","C","D","E"])
		QtCore.QObject.connect(buttonBox, QtCore.SIGNAL("accepted()"), \
					dialog.accept)
		QtCore.QObject.connect(buttonBox, QtCore.SIGNAL("rejected()"), \
					dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(dialog)

		presets = self.get_preset_list()
		for i in range(0, 5):
			for j in range(0, 25):
				item = QtGui.QTableWidgetItem()
				item.setText(presets[j*5+i])
				table.setItem(j, i, item)
		dialog.exec_()
		if dialog.result() == dialog.Accepted:
			index = table.currentRow() * 5 + table.currentColumn()
		else:
			index = -1
		return index
		


# main
app = QApplication(sys.argv)
window = Bass_Vamp()

window.show()
sys.exit(app.exec_())

