from app import db

class Pokemons(db.Model):
    __tablename__ = "pokemons"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    hp = db.Column(db.Float, nullable=False)
    regiao = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(255))

    def __init__(self, nome, tipo, descricao, hp, regiao, image=None):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.hp = hp
        self.regiao = regiao
        self.image = image
