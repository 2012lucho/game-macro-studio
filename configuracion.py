
class Configuracion:
	configuracion = None

	def cargarConfig(self):
		self.configuracion = {
			"controles":[
				{ 
					"descripcion": "Cambiar Ventana",
					"tecla": "i",
					"id":1,
					"comandoSup": 6 
				},
				{
					"descripcion": "Comenzar grabar teclas",
					"tecla": "y",
					"id":2,
					"comandoSup": 6
				},
				{
					"descripcion": "Finalizar grabar teclas",
					"tecla": "u",
					"id":3,
					"comandoSup": 6
				},
				{
					"descripcion": "Comenzar grabar mouse",
					"tecla": "y",
					"id":4,
					"comandoSup": 6
				},
				{
					"descripcion": "Finalizar grabar mouse",
					"tecla": "u",
					"id":5,
					"comandoSup": 6
				},
				{
					"descripcion":"Comando habilitado, escuchando siguiente orden",
					"tecla": "ñ",
					"id":6,
					"comandoSup": 0
				},
				{
					"descripcion":"Salir",
					"tecla": "t",
					"id":7,
					"comandoSup": 6
				}
			],
			"ventanas":{
				"nombre_launcher":"WEMADE",
				"nombre_nuevas_ventanas":[
					{
						"nombre": "Mir4G[1]",
						"esVM": False,
					},
					{
						"nombre": "Mir4G[2]",
						"esVM": False,
					}
				],
				"ubicacion_botones_ventana":[
					{ "id":0, "x":0, "y":0 },
					{ "id":1, "x":0, "y":0 },
				]
			},
			"macros":[],
			"grabador":{
				"tecla_pulsada":"P",
				"tecla_soltada":"S",
				"archivo_teclas": "teclado.csv",
				"archivo_mouse":  "mouse.csv"
			}
		}

	def obtenerConfig(self, config):
		return self.configuracion[config]