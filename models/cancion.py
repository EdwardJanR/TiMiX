from models.album import Album
from models.artista import Artista
from models.categoria import Categoria
from models.generacion import Generacion
from models.userlist import UserList
from app import db


class Cancion(db.Model):

    __tablename__ = 'Canciones'

    idcancion = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String, nullable=False)
    Año = db.Column(db.Integer, nullable=False)
    ArtistaId = db.Column(db.Integer, db.ForeignKey('roles.idRol'), nullable=False)
    AlbumId = db.Column(db.Integer, db.ForeignKey('Albumes.idAlbum'), nullable=False)
    CategoriaId = db.Column(db.Integer, db.ForeignKey('Categorias.idCategoria'), nullable=False)
    GeneracionId = db.Column(db.Integer, db.ForeignKey('Generaciones.idGeneracion'), nullable=False)
    Duracion = db.Column(db.String, nullable=False)
    
    ListaCancion = db.relationship('Listas', secondary = UserList)
    
    
    def __init__(self, Nombre, Año, ArtistaId, AlbumId, CategoriaId, GeneracionId, Duracion):
        self.Nombre = Nombre
        self.Año = Año
        self.ArtistaId = ArtistaId
        self.AlbumId = AlbumId
        self.CategoriaId = CategoriaId
        self.GeneracionId = GeneracionId
        self.Duracion = Duracion
        
    def to_dict(self):
        return {
            'Nombre': self.Nombre,
            'Año': self.Año,
            'Duracion': self.Duracion
        }    
    
    def __str__(self):
        return f'Cancion {self.idcancion} , {self.Nombre} , {self.Año} , {self.ArtistaId} , {self.AlbumId} , {self.CategoriaId} , {self.GeneracionId} , {self.Duracion}'

    def create(self):
        db.session.add(self)
        db.session.commit()      

    @staticmethod
    def get_all():
        return Cancion.query.with_entities(
                    Cancion.Nombre, Cancion.Año, Cancion.Duracion, Categoria.NombreCat, Artista.NombreA, Album.Album, Generacion.NombreG).join(
                    Categoria, Cancion.CategoriaId==Categoria.idCategoria).join(
                    Artista, Cancion.ArtistaId==Artista.idArtista).join(Album, Cancion.AlbumId==Album.idAlbum).join(
                    Generacion, Cancion.GeneracionId==Generacion.idGeneracion)       
    @staticmethod
    def filtroCancion():
        return Cancion.query.with_entities(Cancion.Nombre, Cancion.Año, Cancion.Duracion).filter_by(CategoriaId=1).all()
    
    @staticmethod
    def filtroArtista():
        return Cancion.query.filter_by(ArtistaId=7).all()
    
    @staticmethod
    def filtroCategoria():
        return Cancion.query.filter_by(CategoriaId=2).all()
    
    @staticmethod
    def filtroGeneracion():
        return Cancion.query.filter_by(GeneracionId=2).all()
    
    
    

    @staticmethod
    def get_id():
        return Cancion.query.filter_by(idcancion = 2).first()
    
    @staticmethod
    def get_cancion(nombre):
        return Cancion.query.filter_by(Nombre=nombre).first()
    
  

