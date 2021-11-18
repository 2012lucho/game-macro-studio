import win32api
from ctypes import windll, Structure, c_long, byref
import threading
import time

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

class Mouse:
	app                   = None
	state_left            = None
	state_right           = None
	mouse_pos             = None
	callbacksMouseMove    = []
	callbacksMousePressed = []
	callbacksMouseScroll  = []

	def obtenerPosicionMouse(self):
		pt = POINT()
		windll.user32.GetCursorPos(byref(pt))
		return { "x": pt.x, "y": pt.y}

	def registrarCallBackMove(self, callback):
		self.callbacksMouseMove.append(callback)

	def registrarCallBackPressed(self, callback):
		self.callbacksMousePressed.append(callback)

	def registrarCallBackScroll(self, callback):
		self.callbacksMouseScroll.append(callback)

	def escuchador(self):
		while  self.app.ejecucion:
			a = win32api.GetKeyState(0x01)
			b = win32api.GetKeyState(0x02)
			p = self.obtenerPosicionMouse()
			if self.mouse_pos != None and self.mouse_pos["x"] != p["x"] and self.mouse_pos["y"] != p["y"]:
				self.on_move(self.mouse_pos["x"],self.mouse_pos["y"])

			self.mouse_pos = self.obtenerPosicionMouse()
			if a != self.state_left:  # Button state changed
				self.state_left = a
				if a < 0:
					self.on_click(self.mouse_pos["x"], self.mouse_pos["y"], "L", True)
				else:
					self.on_click(self.mouse_pos["x"], self.mouse_pos["y"], "L", False)

			if b != self.state_right:  # Button state changed
				self.state_right = b
				if b < 0:
					self.on_click(self.mouse_pos["x"], self.mouse_pos["y"], "R", True)
				else:
					self.on_click(self.mouse_pos["x"], self.mouse_pos["y"], "R", False)
			time.sleep(0.001)

	def inicializar(self, app):
		self.app = app

		self.state_left  = win32api.GetKeyState(0x01) 
		self.state_right = win32api.GetKeyState(0x02) 

		hilo1 = threading.Thread(target = self.escuchador)
		hilo1.start()

	def on_move(self, x, y):
		if not self.app.ejecucion:
			return False
		else:
			for callback in self.callbacksMouseMove:
				callback(x,y)
    
	def on_click(self, x, y, button, pressed):
		if not self.app.ejecucion:
			return False
		else:
			for callback in self.callbacksMousePressed:
				callback(x,y, button, pressed)

	def on_scroll(self, x, y, dx, dy):
		if not self.app.ejecucion:
			return False
		else:
			for callback in self.callbacksMousePressed:
				callback(x,y, dx, dy)