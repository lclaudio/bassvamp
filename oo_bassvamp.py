# -*- coding: utf-8 -*-

# class BVamp implements the opeations regarding
# reading and writing to Behringer Bass V-Amp2

import os


BEHRINGER_SIGNATURE = "\x00\x20\x32"
CMD_load_current_preset = "F0 00 20 32 7F 13 60 7F F7"
CMD_load_specific_preset = "F0 00 20 32 7F 13 60"
CMD_load_all_presets = "F0 00 20 32 7F 13 61 F7"
CMD_write_current_preset = "F0 00 20 32 7F 13 20 7F"
CMD_write_all_presets = "F0 00 20 32 7F 13 21"
CMD_identify_device = "F0 00 20 32 7F 7F 01 F7"
Empty_Preset = CMD_write_current_preset + ' 00' * 57 + ' F7'

class BVamp():
	def __init__(self):
		self.data = self.convert_ascii_to_data(Empty_Preset)
		self.orig_data = self.convert_ascii_to_data(Empty_Preset)
		self.midi = None
		self.modified = 0
		self.device = 0
		self.all_data = None

	def load_current_preset(self):
		cmd = 'amidi -p hw:%s -S "%s" -r /dev/stdout -t 1' % \
				(self.midi, CMD_load_current_preset)
		aux = os.popen(cmd)
		result = aux.read(66)
		aux.close()
		self.data = result
		self.orig_data = result

	def load_all_presets(self):
		if not self.needs_refresh:
			return self.all_data
		cmd = 'amidi -p hw:%s -S "%s" -r /dev/stdout -t 1' % \
				(self.midi, CMD_load_all_presets)
		aux = os.popen(cmd)
		result = aux.read(7010)
		aux.close()
		self.all_data = result
		self.needs_refresh = False
		return self.all_data

	def write_current_preset(self):
		s = self.convert_preset_to_ascii()
		cmd = 'amidi -p hw:%s -S "%s%s" -r /dev/stdout -t 1' % \
					(self.midi, CMD_write_current_preset, s)
		aux = os.popen(cmd)
		result = aux.readlines()
		aux.close()

	def list_midi_devices(self):
		mididevice_list = []
		aux = os.popen("amidi -l")
		devlist = aux.readlines()[1:]
		aux.close()
		for i in devlist:
			mididevice_list.append(i[:-1])	
		return mididevice_list

	# hardcoded to use the 'UM-1G MIDI' midi device
	def setup_midi(self, device):
		self.midi = device.split()[1][3:]
		text = self.identify_vamp_device(self.midi)
		return text, self.midi

	def identify_vamp_device(self, midi):
		cmd = 'amidi -p hw:%s -S "%s" -r /dev/stdout -t 1' % \
					(midi, CMD_identify_device)
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

	def read_volume(self, source):
		return ord(source[13])

	def read_gain(self, source):
		return ord(source[9])

	def read_bass(self, source):
		return ord(source[12])

	def read_mid(self, source):
		return ord(source[11])

	def read_treble(self, source):
		return ord(source[10])

	def read_deep(self, source):
		return ord(source[19])

	def read_shift(self, source):
		return ord(source[18])

	def read_presence(self, source):
		return ord(source[14])

	def read_amp(self, source):
		return ord(source[16])

	def read_cabinet(self, source):
		return ord(source[24])

	def read_wah(self, source):
		return ord(source[36])

	def read_depth(self, source):
		return ord(source[37])

	def read_speed(self, source):
		return ord(source[38])

	def read_base(self, source):
		return ord(source[39])

	def read_stomp(self, source):
		return ord(source[30])

	def read_split(self, source):
		return ord(source[34])

	def read_drive(self, source):
		return ord(source[31])

	def read_tone(self, source):
		return ord(source[32])

	def read_boost(self, source):
		return ord(source[33])

	def read_density(self, source):
		return ord(source[15])

	def read_attack(self, source):
		return ord(source[20])

	def read_fx(self, source):
		return ord(source[17])

	def read_fxtype(self, source):
		return ord(source[40])

	def read_fxparm1(self, source):
		return ord(source[41])

	def read_fxparm2(self, source):
		return ord(source[42])

	def read_fxparm3(self, source):
		return ord(source[43])

	def read_fxparm4(self, source):
		return ord(source[44])

	def read_fxparm5(self, source):
		return ord(source[45])

	def read_fxparm6(self, source):
		return ord(source[46])

	def read_fxparm7(self, source):
		return ord(source[47])

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

	def get_preset_name(self, source):
		return source[-17:-1]

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
		self.orig_data = self.data
		aux.close()

	def get_preset_list(self):
		presets = []
		aux = self.load_all_presets()
		for i in range(1,126):
			# neat trick to get the preset name from data dump
			presets.append(aux[(i*56-7):(i*56+9)])
		return presets

	def get_preset_from_data(self, index):
		# I will try the commented code again, later
		#pos = index * 56 + 9
		#self.data = CMD_write_current_preset + chr(0x38)+ \
		#		self.all_data[pos:(pos+56)] + chr(0xF7)
		CMD_load_specific_preset
		cmd = 'amidi -p hw:%s -S "%s %02X F7" -r /dev/stdout -t 1' % \
				(self.midi, CMD_load_specific_preset, index)
		aux = os.popen(cmd)
		result = aux.read(66)
		aux.close()
		self.data = result
		self.orig_data = result


