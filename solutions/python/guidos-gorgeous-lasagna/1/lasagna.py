"""Funções para calcular os tempos de preparo da lasanha."""

# Tempo total necessário no forno, em minutos.
EXPECTED_BAKE_TIME = 40

# Tempo de preparo de cada camada, em minutos.
TEMPO_POR_CAMADA = 2


def bake_time_remaining(tempo_no_forno):
    """Calcula quantos minutos faltam para a lasanha assar."""
    return EXPECTED_BAKE_TIME - tempo_no_forno


def preparation_time_in_minutes(numero_de_camadas):
    """Calcula o tempo necessário para preparar as camadas."""
    return numero_de_camadas * TEMPO_POR_CAMADA


def elapsed_time_in_minutes(numero_de_camadas, tempo_no_forno):
    """Calcula o tempo total gasto no preparo e no forno."""
    tempo_de_preparo = preparation_time_in_minutes(numero_de_camadas)
    return tempo_de_preparo + tempo_no_forno