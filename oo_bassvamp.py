# -*- coding: utf-8 -*-

# class BVamp implements the opeations regarding
# reading and writing to Behringer Bass V-Amp2

import os


BEHRINGER_SIGNATURE = "\x00\x20\x32"
CMD_load_current_preset = "F0 00 20 32 00 13 60 7F F7"
CMD_load_all_presets = "F0 00 20 32 00 13 61 F7"
CMD_write_current_preset = "F0 00 20 32 00 13 20 7F"
CMD_write_all_presets = "F0 00 20 32 00 13 21"
CMD_identify_device = "F0 00 20 32 7F 7F 01 F7"
Empty_Preset = CMD_write_current_preset + ' 00' * 57 + ' F7'

class BVamp():
	def __init__(self):
		self.data = self.convert_ascii_to_data(Empty_Preset)
		self.midi = None
		self.modified = 0
		self.device = 0

	def load_current_preset(self):
		cmd = 'amidi -p hw:%s -S "%s" -r /dev/stdout -t 1' % \
				(self.midi, CMD_load_current_preset)
		aux = os.popen(cmd)
		result = aux.read(66)
		aux.close()
		self.data = result

	def write_current_preset(self):
		if not self.data:
			# this is wrong, need to be able to crete from scratch
			self.print_msg("No data available, reading current preset\n")
			self.load_current_preset()
			return 
		s = self.convert_preset_to_ascii()
		cmd = 'amidi -p hw:%s -S "%s%s" -r /dev/stdout -t 1' % \
					(self.midi, CMD_write_current_preset, s)
		print cmd
		aux = os.popen(cmd)
		result = aux.readlines()
		aux.close()
		print self.convert_data_to_ascii(result)

	def list_midi_devices(self):
		aux = os.popen("amidi -l")
		self.mididevice_list = aux.readlines()[1:]
		aux.close()
		return self.mididevice_list

	# hardcoded to use the 'UM-1G MIDI' midi device
	def setup_midi(self, device):
		self.midi = device.split()[1][3:]
		text = self.identify_vamp_device()
		return text, self.midi

	def identify_vamp_device(self):
		cmd = 'amidi -p hw:%s -S "%s" -r /dev/stdout -t 1' % \
					(self.midi, CMD_identify_device)
		aux = os.popen(cmd)
		result = aux.readlines()
		aux.close()
		if result == []:
			return "No Bass V-Amp found!\n"

		data = result[0]
		# if it is a Behringer device...
		if data[1:4] == BEHRINGER_SIGNATURE:
			self.device = data[5:6]
			text = data[7:-1] + "\n"
		else:
			text = "Not a Behringer device!\n"

		return text

	def read_volume(self):
		return ord(self.data[13])

	def read_gain(self):
		return ord(self.data[9])

	def read_bass(self):
		return ord(self.data[12])

	def read_mid(self):
		return ord(self.data[11])

	def read_treble(self):
		return ord(self.data[10])

	def read_deep(self):
		return ord(self.data[19])

	def read_shift(self):
		return ord(self.data[18])

	def read_presence(self):
		return ord(self.data[14])

	def read_amp(self):
		return ord(self.data[16])

	def read_cabinet(self):
		return ord(self.data[24])

	def read_wah(self):
		return ord(self.data[36])

	def read_depth(self):
		return ord(self.data[37])

	def read_speed(self):
		return ord(self.data[38])

	def read_base(self):
		return ord(self.data[39])

	def read_stomp(self):
		return ord(self.data[30])

	def read_split(self):
		return ord(self.data[34])

	def read_drive(self):
		return ord(self.data[31])

	def read_tone(self):
		return ord(self.data[32])

	def read_boost(self):
		return ord(self.data[33])

	def read_density(self):
		return ord(self.data[15])

	def read_attack(self):
		return ord(self.data[20])

	def read_fx(self):
		return ord(self.data[17])

	def read_fxtype(self):
		return ord(self.data[40])

	def read_fxparm1(self):
		return ord(self.data[41])

	def read_fxparm2(self):
		return ord(self.data[42])

	def read_fxparm3(self):
		return ord(self.data[43])

	def read_fxparm4(self):
		return ord(self.data[44])

	def read_fxparm5(self):
		return ord(self.data[45])

	def read_fxparm6(self):
		return ord(self.data[46])

	def read_fxparm7(self):
		return ord(self.data[47])

	def set_volume(self, value):
		self.set_preset_item(13, value)

	def set_gain(self, value):
		self.set_preset_item(9, value)

	def set_bass(self, value):
		self.set_preset_item(12, value)

	def set_mid(self, value):
		self.set_preset_item(11, value)

	def set_treble(self, value):
		self.set_preset_item(10, value)

	def set_deep(self, value):
		self.set_preset_item(19, value)

	def set_shift(self, value):
		self.set_preset_item(18, value)

	def set_presence(self, value):
		self.set_preset_item(14, value)

	def set_amp(self, value):
		self.set_preset_item(16, value)

	def set_cabinet(self, value):
		self.set_preset_item(24, value)

	def set_wah(self, value):
		self.set_preset_item(36, value)

	def set_depth(self, value):
		self.set_preset_item(37, value)

	def set_speed(self, value):
		self.set_preset_item(38, value)

	def set_base(self, value):
		self.set_preset_item(39, value)

	def set_stomp(self, value):
		self.set_preset_item(30, value)

	def set_split(self, value):
		self.set_preset_item(34, value)

	def set_drive(self, value):
		self.set_preset_item(31, value)

	def set_tone(self, value):
		self.set_preset_item(32, value)

	def set_boost(self, value):
		self.set_preset_item(33, value)

	def set_density(self, value):
		self.set_preset_item(15, value)

	def set_attack(self, value):
		self.set_preset_item(20, value)

	def set_fx(self, value):
		self.set_preset_item(17, value)

	def set_fxtype(self, value):
		self.set_preset_item(40, value)

	def set_fxparm1(self, value):
		self.set_preset_item(41, value)

	def set_fxparm2(self, value):
		self.set_preset_item(42, value)

	def set_fxparm3(self, value):
		self.set_preset_item(43, value)

	def set_fxparm4(self, value):
		self.set_preset_item(44, value)

	def set_fxparm5(self, value):
		self.set_preset_item(45, value)

	def set_fxparm6(self, value):
		self.set_preset_item(46, value)

	def set_fxparm7(self, value):
		self.set_preset_item(47, value)

	def set_preset_item(self, pos, value):
		self.data = self.data[:pos] + chr(value) + self.data[pos+1:]

	def get_preset_name(self):
		return self.data[-17:-1]

	def set_preset_name(self, value):
		if len(value) >= 16:
			nameaux = value[:16]
		else:
			nameaux = value + ' ' * (16 - len(value))
		aux = self.data[:-17] + nameaux + chr(0xF7)
		self.data = aux

	def convert_preset_to_ascii(self):
		return self.convert_data_to_ascii(self.data)

	def convert_data_to_ascii(self, data):
		s = ""
		for i in data[8:]:
			s += " %02X" % ord(i)
		print s
		return s

	def convert_ascii_to_data(self, text):
		aux = ""
		for i in text.split():
			aux += chr(int("0x%s" % i, 16))
		return aux

	def save_preset_to_file(self, fname):
		aux = open(fname, "wb")
		aux.write(self.data)
		aux.flush()
		aux.close()

	def load_preset_from_file(self, fname):
		aux = open(fname, "rb")
		self.data = aux.read(66)
		aux.close()
