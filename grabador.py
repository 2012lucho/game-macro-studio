from datetime import datetime

SEPARADOR = ','
FPS = 60
LINE_END = '\n'

FPS_TIME = 1/FPS

class Grabador():
    controles     = None
    configuracion = None
    file = {}

    grabandoTeclas = False
    grabandoMouse  = False
    teclado = None
    mouse = None

    def abrir_archivos(self):
        print("\x1b[1;33m"+"[Grabador] Se abren los archivos")
        self.file["mouse"]   = open(self.configuracion["archivo_mouse"], "a")
        self.file["teclado"] = open(self.configuracion["archivo_teclas"], "a")

    def inicializar(self, configuracion, controles, teclado, mouse):
        self.configuracion = configuracion.obtenerConfig("grabador")  
        self.controles     = controles

        self.teclado = teclado
        self.teclado.registrarCallBackKD(self.pulsa)
        self.teclado.registrarCallBackKU(self.suelta)
        
        self.mouse = mouse
        self.mouse.registrarCallBackMove(self.mouseMove)
        self.mouse.registrarCallBackScroll(self.mouseScroll)
        self.mouse.registrarCallBackPressed(self.mousePressed)
        self.controles.registrarComando(2, self.comandoGrabar)
        self.controles.registrarComando(3, self.comandoPararGrabar)

    def comandoGrabar(self):
        print("\x1b[1;33m"+"[Grabador] Se graban teclas y mouse")
        self.grabandoTeclas = True
        self.grabandoMouse  = True
        self.abrir_archivos()

    def comandoPararGrabar(self):
        print("\x1b[1;33m"+"[Grabador] Se para de grabar teclas y mouse")
        self.grabandoTeclas = False
        self.grabandoMouse  = False
        self.cerrar_archivos()

    def mouseMove(self, x, y):
        if self.grabandoMouse:
            print("\x1b[1;37m"+'[Grabador] Posicion mouse {0}'.format((x, y)))
            fecha_hora = datetime.today()
            self.file["mouse"].write(str(x) + SEPARADOR + str(y) + SEPARADOR + 'ninguno' + SEPARADOR + str(fecha_hora) + SEPARADOR + 'P' + LINE_END)

    def mouseScroll(self, x, y, dx, dy):
        if self.grabandoMouse:
            print("\x1b[1;37m"+'[Grabador] Mouse scroll {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))
            fecha_hora = datetime.today()
            self.file["mouse"].write(str(x) + SEPARADOR + str(y) + SEPARADOR + str(fecha_hora) + SEPARADOR + 'SC1' + LINE_END)
            self.file["mouse"].write(str(dx) + SEPARADOR + str(dy) + SEPARADOR + str(fecha_hora) + SEPARADOR + 'SC2' + LINE_END)

    def mousePressed(self, x, y, button, pressed):
        if self.grabandoMouse:
            fecha_hora = datetime.today()
            print("\x1b[1;37m"+'[Grabador] Boton mouse {0} at {1}'.format('Presionado' if pressed else 'Soltado',(x, y)))
            if pressed:
                self.file["mouse"].write(str(x) + SEPARADOR + str(y) + SEPARADOR + str(button) + SEPARADOR + str(fecha_hora) + SEPARADOR + 'MD' + LINE_END)
            else:
                self.file["mouse"].write(str(x) + SEPARADOR + str(y) + SEPARADOR + str(button) + SEPARADOR + str(fecha_hora) + SEPARADOR + 'MU' + LINE_END)

    def pulsa(self, tecla):
        if self.grabandoTeclas:
            fecha_hora = datetime.today()
            print("\x1b[1;37m"+'[Grabador] Se apreto la tecla ' + str(tecla))
            self.file["teclado"].write(str(tecla) + SEPARADOR + self.configuracion["tecla_pulsada"] + SEPARADOR + str(fecha_hora) + LINE_END)

    def suelta(self, tecla):
        fecha_hora = datetime.today()
        if self.grabandoTeclas:
            print("\x1b[1;37m"+'[Grabador] Se se solto la tecla ' + str(tecla))
            self.file["teclado"].write(str(tecla) + SEPARADOR + self.configuracion["tecla_soltada"] + SEPARADOR + str(fecha_hora) + LINE_END)
     
    def cerrar_archivos(self):
        if "mouse" in self.file:
            self.file["mouse"].close()
        if "teclado" in self.file:
            self.file["teclado"].close()
        print("\x1b[1;33m"+"[Grabador] Archivos cerrados")