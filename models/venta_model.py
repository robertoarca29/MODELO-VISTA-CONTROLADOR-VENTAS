from database import db

class Venta(db.Model):
    __tablename__ = "ventas"

    id = db.Column(db.Integer,primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'),nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'),nullable=False)
    cantidad = db.Column(db.Integer,nullable=False)
    fecha = db.Column(db.DateTime,nullable=False)

    # Especificar la relacion
    cliente = db.relationship('Cliente',back_populates='ventas')
    producto = db.relationship('Producto',back_populates='ventas')

    def __init__(self, cliente_id, producto_id, cantidad, fecha):
        self.cliente_id = cliente_id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.fecha = fecha

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Venta.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Venta.query.get(id)
    
    def update(self,cliente_id=None,producto_id=None,cantidad=None,fecha=None):
        if cliente_id and producto_id and cantidad and fecha:
            self.cliente_id = cliente_id
            self.producto_id = producto_id
            self.cantidad = cantidad 
            self.fecha = fecha       
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()