from app import db

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_do_produto = db.Column(db.String(100), nullable=False)
    codigo_do_produto = db.Column(db.String(50), unique=True, nullable=False)
    descricao_do_produto = db.Column(db.String(200), nullable=False)
    preco_do_produto = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Produto {self.nome_do_produto}>'