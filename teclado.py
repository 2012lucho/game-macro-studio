from pynput import keyboard
import threading

class Teclado:
	app                   = None
	callbacksTeclaPulsada = []
	callbacksTeclaSoltada = []

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

	def escuchador(self):
		l = keyboard.Listener(self.pulsa, self.suelta)
		l.start()
		while True:
			a=0

	def iniciar(self, app):
		self.app = app
		#self.escuchador()
		hilo1 = threading.Thread(target = self.escuchador)
		hilo1.start()