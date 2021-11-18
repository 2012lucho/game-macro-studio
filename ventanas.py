import win32gui
import subprocess

class ManejaVentanas:
	topwindows          = []
	subprocess          = []
	ventanaACtualJuego  = None
	launcher_subprocess = None
	configuracion       = None

	def inicializar(self, configuracion):
		self.configuracion = configuracion.obtenerConfig("ventanas")
		self.buscarYmostrarVentana(self.configuracion["nombre_launcher"], True, True)

	def ejecutarPrograma(self, ruta):
		id = len(self.subprocess)
		self.subprocess.append(subprocess.Popen(ruta))
		return id

	def obtenerSubprocess(self, id):
		return self.subprocess[id]

	def obtenerListaVentanas(self, hwnd, topwindows):
		topwindows.append((hwnd, win32gui.GetWindowText(hwnd)))

	def mostrarListaVentanas(self):
		self.topwindows = []
		win32gui.EnumWindows(self.obtenerListaVentanas, self.topwindows)
		for hwin in self.topwindows:	
			sappname=str(hwin[1])
			nhwnd=hwin[0]
			print(str(nhwnd) + ": " + sappname)

	def buscarYmostrarVentana(self, swinname, bshow, bbreak):
		self.topwindows = []
		win32gui.EnumWindows(self.obtenerListaVentanas, self.topwindows)
		
		for hwin in self.topwindows:
				
			sappname=str(hwin[1])
			if sappname == swinname:
				print(bshow)	
				nhwnd=hwin[0]
				print(">>> Found: " + str(nhwnd) + ": " + sappname)
				if(bshow):
					win32gui.ShowWindow(nhwnd,5)
					win32gui.SetForegroundWindow(nhwnd)
				if(bbreak):
					break

	def obtenerPosicionVentana(self, ventana):
		print("algo")