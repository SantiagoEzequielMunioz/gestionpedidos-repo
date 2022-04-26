class Carro:
    def __init__(self,request):
        self.request = request
        # hay que igualar las sesiones
        self.session = request.session
        carro = self.session.get('carro')
        # si no hay ese objeto, hay que crearlo mediante un {}
        # {id-producto:{nombre:'',precio:'',etc}}
        if not carro:
            carro = self.session['carro']={}
        else:
            self.carro = carro

    def agregar(self,producto):
        # en caso de que no exista en el carro, lo creamos
        if (str(producto.id) not in self.carro.keys()):
            self.carro[producto.id] = {
                'producto_id':producto.id,
                'nombre':producto.nombre,
                'descripcion':producto.descripcion,
                'precio':str(producto.precio),
                'cantidad':1,
                'imagen':producto.imagen.url
            }
        else:
            # si ya existe, busco la coincidencia de id y lo agrego
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value['cantidad']+=1
                    break
        
        self.guardar_carro()
    
    def guardar_carro(self):
        self.session['carro']=self.carro
        self.session.modified=True

    def eliminar(self,producto):
        producto.id=str(producto.id)    #solo paso a string
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
    
    def restar_producto(self,producto):
        for key, value in self.carro.items():
            if key == str(producto.id):
                value['cantidad']-=1
                # en caso de que la cantidad de items sea 0, lo elimino del carro directamente
                if value['cantidad']==0:
                    self.eliminar(producto)
                break
        self.guardar_carro()
    
    def limpiar_carro(self):    # limpio de todos los productos
        self.session['carro']={}
        self.session.modified=True