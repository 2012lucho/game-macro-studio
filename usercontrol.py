
class ControlesUsuario:
	comandos = {}
	configuracion = None
	teclado       = None
	mouse         = None

	escuchandoOrden = False
	
	def iniciar(self, configuracion, mouse, teclado):
		self.configuracion = configuracion.obtenerConfig("controles")
		self.teclado       = teclado
		self.mouse         = mouse

		self.teclado.registrarCallBackKU(self.escuchaTecla)
		#Se registra la tecla para ingresar comandos
		self.registrarComando(6,self.comandoPrincipal)
	
	def escuchaTecla(self, tecla):
		#Se solto una tecla, entonces se revisa si se trata de un comando
		for comandCnf in self.configuracion:
			#Si ya se ingreso el comando para escuchar orden
			if self.escuchandoOrden:
				if str(comandCnf["tecla"]) == str(tecla):
					self.ejecutarComando(comandCnf)
					self.escuchandoOrden = False			
			else: #En caso de que no se esten escuchando ordenes se verifica si se apreto la tecla para ingresar comando
				if str(comandCnf["tecla"]) == str(tecla) and str(comandCnf["comandoSup"]) == str(0):
					self.ejecutarComando(comandCnf)
					self.escuchandoOrden = True

	def ejecutarComando(self, comandCnf):
		print("\x1b[1;36m"+"Iniciando comando: "+comandCnf["descripcion"])
		self.comandos[int(comandCnf["id"])]()

	def comandoPrincipal(self):
		if self.escuchandoOrden:
			self.escucharOrdenDesabilitado()
		else:
			self.escucharOrdenHabilitado()

	def registrarComando(self, id,callback):
		self.comandos[id] = callback

	def escucharOrdenHabilitado(self):
		print("\x1b[1;36m"+"Se espera ingreso de nuevo comando")
		self.escuchandoOrden = True

	def escucharOrdenDesabilitado(self):
		print("\x1b[1;36m"+"No se esperan nuevos comandos")
		self.escuchandoOrden = False