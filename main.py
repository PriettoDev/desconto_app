from src.models.desconto import DescontoVIP, DescontoNormal, DescontoPremium
from src.models.pedido import Pedido
from src.services.pedido_service import PedidoService

def main():
    servico = PedidoService()

    pedido1 = Pedido("Leonardo", DescontoNormal())
    pedido2 = Pedido("Pedro", DescontoVIP())
    pedido3 = Pedido("Lucas", DescontoPremium())

    pedido1.valor_final(100)
    pedido2.valor_final(200)
    pedido3.valor_final(300)

    servico.adicionar_pedido(pedido1)
    servico.adicionar_pedido(pedido2)
    servico.adicionar_pedido(pedido3)

    servico.processar_pedidos()


if __name__ == "__main__":
    main()