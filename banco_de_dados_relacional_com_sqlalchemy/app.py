from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import (DECIMAL, 
                        Column, 
                        Integer, 
                        String, 
                        ForeignKey, 
                        create_engine, 
                        select)


Base = declarative_base()

class Cliente(Base):

    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    cpf = Column(String(11), nullable=False)

    conta = relationship("Conta", back_populates="cliente")

    def __repr__(self):
        return f"Cliente(id={self.id}, nome={self.nome}, cpf={self.cpf})"


class Conta(Base):

    __tablename__ = "conta"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String, nullable=False)
    agencia = Column(Integer, nullable=False)
    conta = Column(String, nullable=False)
    id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable=False)
    saldo = Column(DECIMAL(8,2), nullable=False)

    cliente = relationship("Cliente", back_populates="conta")

    def __repr__(self):
        return f"Conta(id={self.id}, tipo={self.tipo}, "\
               f"agencia={self.agencia}, conta={self.conta}, "\
               f"id_cliente={self.id_cliente}, saldo={self.saldo})"
    

engine = create_engine("sqlite://")
Base.metadata.create_all(engine)


with Session(engine) as session:
    cliente_1 = Cliente(nome="João", cpf="11111111111")
    cliente_2 = Cliente(nome="Maria", cpf="22222222222")
    cliente_3 = Cliente(nome="José", cpf="33333333333")

    session.add_all([cliente_1, cliente_2, cliente_3])
    session.commit()

    conta_1 = Conta(tipo="Corrente", 
                    agencia=1, 
                    conta="123-4",
                    id_cliente=1,
                    saldo=100)

    conta_2 = Conta(tipo="Corrente", 
                    agencia=1, 
                    conta="124-0",
                    id_cliente=2,
                    saldo=500)

    conta_3 = Conta(tipo="Poupança", 
                    agencia=1, 
                    conta="123-4",
                    id_cliente=3,
                    saldo=50)
    
    session.add_all([conta_1, conta_2, conta_3])
    session.commit()

stmt_join = select(Cliente, Conta).join_from(Cliente, Conta)


for result in session.execute(stmt_join):
    print(result)




