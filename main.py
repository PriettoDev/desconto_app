from src.models.desconto import DescontoVIP
from src.models.pedido import Pedido

if __name__ == "__main__":
    pedido = Pedido("Leonardo", DescontoVIP())

    valor_final = pedido.valor_final(100)
    print(f"Cliente: {pedido.cliente}")
    print(f"Valor final: {valor_final}")