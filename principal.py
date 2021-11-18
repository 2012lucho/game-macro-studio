from ventanas import ManejaVentanas
from configuracion import Configuracion
from usercontrol import ControlesUsuario
from mouse import Mouse
from teclado import Teclado
from grabador import Grabador

class Principal:
	maneja_ventanas = None
	configuracion   = None
	controles       = None
	mouse           = None
	teclado         = None
	grabador        = None
	macros          = None

	ejecucion = True

	def iniciar(self):
		self.configuracion   = Configuracion()
		self.configuracion.cargarConfig()

		self.mouse = Mouse()
		self.mouse.inicializar( self )
		self.teclado = Teclado()
		self.teclado.iniciar( self )

		self.controles = ControlesUsuario()
		self.controles.iniciar(self.configuracion, self.mouse, self.teclado)
		self.controles.registrarComando(7, self.comandoSalir)
		
		self.grabador  = Grabador()
		self.grabador.inicializar(self.configuracion, self.controles, self.teclado, self.mouse)

		self.maneja_ventanas = ManejaVentanas()
		self.maneja_ventanas.inicializar( self.configuracion )
		
		while self.ejecucion:
			a = 1

	def comandoSalir(self):
		self.grabador.comandoPararGrabar()
		self.ejecucion = False

app = Principal()
app.iniciar()