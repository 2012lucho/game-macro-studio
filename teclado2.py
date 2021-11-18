import win32api
import threading
import time

class Teclado:
	app                   = None
	callbacksTeclaPulsada = []
	callbacksTeclaSoltada = []
	
	VK_CODE = [
		{ 'k':'backspace', 'v':0x08},
        { 'k':'tab', 'v':0x09},
        { 'k':'clear', 'v':0x0C},
        { 'k':'enter', 'v':0x0D},
        { 'k':'shift', 'v':0x10},
        { 'k':'ctrl', 'v':0x11},
        { 'k':'alt', 'v':0x12},
        { 'k':'pause', 'v':0x13},
        { 'k':'caps_lock', 'v':0x14},
        { 'k':'esc', 'v':0x1B},
        { 'k':'spacebar', 'v':0x20},
        { 'k':'page_up', 'v':0x21},
        { 'k':'page_down', 'v':0x22},
        { 'k':'end', 'v':0x23},
        { 'k':'home', 'v':0x24},
        { 'k':'left_arrow', 'v':0x25},
        { 'k':'up_arrow', 'v':0x26},
        { 'k':'right_arrow', 'v':0x27},
        { 'k':'down_arrow', 'v':0x28},
        { 'k':'select', 'v':0x29},
        { 'k':'print', 'v':0x2A},
        { 'k':'execute', 'v':0x2B},
        { 'k':'print_screen', 'v':0x2C},
        { 'k':'ins', 'v':0x2D},
        { 'k':'del', 'v':0x2E},
        { 'k':'help', 'v':0x2F},
        { 'k':'0', 'v':0x30},
        { 'k':'1', 'v':0x31},
        { 'k':'2', 'v':0x32},
        { 'k':'3', 'v':0x33},
        { 'k':'4', 'v':0x34},
        { 'k':'5', 'v':0x35},
        { 'k':'6', 'v':0x36},
        { 'k':'7', 'v':0x37},
        { 'k':'8', 'v':0x38},
        { 'k':'9', 'v':0x39},
        { 'k':'a', 'v':0x41},
        { 'k':'b', 'v':0x42},
        { 'k':'c', 'v':0x43},
        { 'k':'d', 'v':0x44},
        { 'k':'e', 'v':0x45},
        { 'k':'f', 'v':0x46},
        { 'k':'g', 'v':0x47},
        { 'k':'h', 'v':0x48},
        { 'k':'i', 'v':0x49},
        { 'k':'j', 'v':0x4A},
        { 'k':'k', 'v':0x4B},
        { 'k':'l', 'v':0x4C},
        { 'k':'m', 'v':0x4D},
        { 'k':'n', 'v':0x4E},
        { 'k':'o', 'v':0x4F},
        { 'k':'p', 'v':0x50},
        { 'k':'q', 'v':0x51},
        { 'k':'r', 'v':0x52},
        { 'k':'s', 'v':0x53},
        { 'k':'t', 'v':0x54},
        { 'k':'u', 'v':0x55},
        { 'k':'v', 'v':0x56},
        { 'k':'w', 'v':0x57},
        { 'k':'x', 'v':0x58},
        { 'k':'y', 'v':0x59},
        { 'k':'z', 'v':0x5A},
        { 'k':'numpad_0', 'v':0x60},
        { 'k':'numpad_1', 'v':0x61},
        { 'k':'numpad_2', 'v':0x62},
        { 'k':'numpad_3', 'v':0x63},
        { 'k':'numpad_4', 'v':0x64},
        { 'k':'numpad_5', 'v':0x65},
        { 'k':'numpad_6', 'v':0x66},
        { 'k':'numpad_7', 'v':0x67},
        { 'k':'numpad_8', 'v':0x68},
        { 'k':'numpad_9', 'v':0x69},
        { 'k':'multiply_key', 'v':0x6A},
        { 'k':'add_key', 'v':0x6B},
        { 'k':'separator_key', 'v':0x6C},
        { 'k':'subtract_key', 'v':0x6D},
        { 'k':'decimal_key', 'v':0x6E},
        { 'k':'divide_key', 'v':0x6F},
        { 'k':'F1', 'v':0x70},
        { 'k':'F2', 'v':0x71},
        { 'k':'F3', 'v':0x72},
        { 'k':'F4', 'v':0x73},
        { 'k':'F5', 'v':0x74},
        { 'k':'F6', 'v':0x75},
        { 'k':'F7', 'v':0x76},
        { 'k':'F8', 'v':0x77},
        { 'k':'F9', 'v':0x78},
        { 'k':'F10', 'v':0x79},
        { 'k':'F11', 'v':0x7A},
        { 'k':'F12', 'v':0x7B},
        { 'k':'F13', 'v':0x7C},
        { 'k':'F14', 'v':0x7D},
        { 'k':'F15', 'v':0x7E},
        { 'k':'F16', 'v':0x7F},
        { 'k':'F17', 'v':0x80},
        { 'k':'F18', 'v':0x81},
        { 'k':'F19', 'v':0x82},
        { 'k':'F20', 'v':0x83},
        { 'k':'F21', 'v':0x84},
        { 'k':'F22', 'v':0x85},
        { 'k':'F23', 'v':0x86},
        { 'k':'F24', 'v':0x87},
        { 'k':'num_lock', 'v':0x90},
        { 'k':'scroll_lock', 'v':0x91},
        { 'k':'left_shift', 'v':0xA0},
        { 'k':'right_shift ', 'v':0xA1},
        { 'k':'left_control', 'v':0xA2},
        { 'k':'right_control', 'v':0xA3},
        { 'k':'left_menu', 'v':0xA4},
        { 'k':'right_menu', 'v':0xA5},
        { 'k':'browser_back', 'v':0xA6},
        { 'k':'browser_forward', 'v':0xA7},
        { 'k':'browser_refresh', 'v':0xA8},
        { 'k':'browser_stop', 'v':0xA9},
        { 'k':'browser_search', 'v':0xAA},
        { 'k':'browser_favorites', 'v':0xAB},
        { 'k':'browser_start_and_home', 'v':0xAC},
        { 'k':'volume_mute', 'v':0xAD},
        { 'k':'volume_Down', 'v':0xAE},
        { 'k':'volume_up', 'v':0xAF},
        { 'k':'next_track', 'v':0xB0},
        { 'k':'previous_track', 'v':0xB1},
        { 'k':'stop_media', 'v':0xB2},
        { 'k':'play/pause_media', 'v':0xB3},
        { 'k':'start_mail', 'v':0xB4},
        { 'k':'select_media', 'v':0xB5},
        { 'k':'start_application_1', 'v':0xB6},
        { 'k':'start_application_2', 'v':0xB7},
        { 'k':'attn_key', 'v':0xF6},
        { 'k':'crsel_key', 'v':0xF7},
        { 'k':'exsel_key', 'v':0xF8},
        { 'k':'play_key', 'v':0xFA},
        { 'k':'zoom_key', 'v':0xFB},
        { 'k':'clear_key', 'v':0xFE},
        { 'k':'+', 'v':0xBB},
        { 'k':',', 'v':0xBC},
        { 'k':'-', 'v':0xBD},
        { 'k':'.', 'v':0xBE},
        { 'k':'/', 'v':0xBF},
        { 'k':'`', 'v':0xC0},
        { 'k':';', 'v':0xBA},
        { 'k':'[', 'v':0xDB},
        { 'k':'\\', 'v':0xDC},
        { 'k':']', 'v':0xDD},
        { 'k':"'", 'v':0xDE},
        { 'k':'`', 'v':0xC0}]

	key_status = {}

	def obtenerEstadoTeclas(self):
		estado = {}
		for key in self.VK_CODE:
			e = win32api.GetAsyncKeyState(key["v"])
			if e < 0:
				estado[str(key["k"])] = 1
			else:
				estado[str(key["k"])] = 0
		return estado

	def pulsa(self, tecla):
		if not self.app.ejecucion:
			return False
		else:
			for callback in self.callbacksTeclaPulsada:
				tecla = str(tecla).replace("'","")
				callback(tecla)

	def suelta(self, tecla):
		if not self.app.ejecucion:
			return False
		else:
			for callback in self.callbacksTeclaSoltada:
				tecla = str(tecla).replace("'","")
				callback(tecla)

	def registrarCallBackKD(self, callback):
		self.callbacksTeclaPulsada.append(callback)

	def registrarCallBackKU(self, callback):
		self.callbacksTeclaSoltada.append(callback)

	def encontrarDifEstadoTecla(self, estadoA, estadoN, callback):
		for key in self.VK_CODE:
			if estadoA[key["k"]] != estadoN[key["k"]]:
				callback(key["k"], estadoN[key["k"]])

	def diferenciaEstadoEncontrada(self, k, e):
		print(str(k)+"-"+str(e))

	def escuchador(self):
		while  self.app.ejecucion:
			s = self.obtenerEstadoTeclas()
			self.encontrarDifEstadoTecla(self.key_status, s, self.diferenciaEstadoEncontrada)
			self.key_status = self.obtenerEstadoTeclas()
			time.sleep(0.1)

	def iniciar(self, app):
		self.app = app
		self.key_status = self.obtenerEstadoTeclas()
		hilo1 = threading.Thread(target = self.escuchador)
		hilo1.start()