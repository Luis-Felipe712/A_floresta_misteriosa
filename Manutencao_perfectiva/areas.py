def get_area_description(area):
    descriptions = {
        "floresta": "Você está em uma floresta densa. Trilhas seguem para o norte, leste e oeste.",
        "cabana": "Você encontrou uma cabana misteriosa. Algo dentro chama sua atenção.",
        "rio": "Um rio de águas turbulentas bloqueia seu caminho. Talvez algo possa ajudar.",
        "bosque": "O bosque é silencioso e sombrio. Há algo brilhando ao longe.",
    }
    return descriptions.get(area, "Área desconhecida.")


def get_area_items(area):
    items = {
        "cabana": ["chave"],
        "bosque": ["poção"],
        "rio": [],
    }
    return items.get(area, [])


def get_area_enemy(area):
    enemies = {
        "rio": {"nome": "Crocodilo", "vida": 50, "ataque": 10},
        "bosque": {"nome": "Lobo", "vida": 30, "ataque": 8},
    }
    return enemies.get(area)


def is_final_area(area, inventory):
    if area == "cabana" and "chave" in inventory:
        return True
    return False
