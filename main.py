from src.controllers.pedido_controller import PedidoController
from src.repositories.pedido_repository import PedidoRepository
from src.services.pedido_service import PedidoService
from src.database.connection import DatabaseConnection
from src.models.pedido import Pedido
from src.models.desconto import DescontoVIP, DescontoNormal, DescontoPremium

def main():
    #Configuração do repositório, controller e serviço
    database = DatabaseConnection()
    repo = PedidoRepository(database)
    service = PedidoService(repo)
    controller = PedidoController(service)

    #Criando pedido com desconto
    pedido1 = Pedido("Cliente 1", desconto=DescontoNormal())
    pedido1.valor_original=100

    pedido2 = Pedido("Cliente 2", desconto=DescontoVIP())
    pedido2.valor_original=100

    pedido3 = Pedido("Cliente 3", desconto=DescontoPremium())
    pedido3.valor_original=100

    controller.adicionar_pedido(pedido1)
    controller.adicionar_pedido(pedido2)
    controller.adicionar_pedido(pedido3)

    controller.processar_pedidos()

if __name__ == "__main__":
    main()