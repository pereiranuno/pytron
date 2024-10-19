class Evento:
    def __init__(self, show: str, event: str, timestamp: int, user_id: int):
        self.show = show
        self.event = event
        self.timestamp = timestamp
        self.user_id = user_id

    def __repr__(self):
        return f"Evento(show={self.show}, event={self.event}, timestamp={self.timestamp}, user_id={self.user_id})"


class ShowTracker:
    def __init__(self):
        self.active_users_show = {}

    def process_event(self, evento: Evento) -> None:
        """
        Processa um evento para atualizar o dicionário de utilizadores ativos por show.
        """
        show = evento.show
        user_id = evento.user_id

        if evento.event == 'start':
            if show not in self.active_users_show:
                self.active_users_show[show] = set()
            self.active_users_show[show].add(user_id)
        elif evento.event == 'stop':
            if show in self.active_users_show and user_id in self.active_users_show[show]:
                self.active_users_show[show].remove(user_id)

    def calculate_active_users_per_show(self, eventos: list[Evento]) -> None:
        """
        Calcula e imprime o número de utilizadores ativos por show.
        """
        eventos_ordenados = sorted(eventos, key=lambda x: x.timestamp)
        for evento in eventos_ordenados:
            self.process_event(evento)

        self.print_active_users()

    def print_active_users(self) -> None:
        """
        Imprime o número de utilizadores ativos por show.
        """
        print("\nActive Users per Show:")
        print("-" * 30)
        for show, users in self.active_users_show.items():
            print(f"Show: {show:25} | Active Users: {len(users)}")
        print("-" * 30 + "\n")


# --- DataSet Dictionary Registry List ---
registry_list = [
    Evento("The Witcher", "start", 0, 1),
    Evento("The Witcher", "start", 1, 2),
    Evento("The Witcher", "stop", 3, 2),
    Evento("The Umbrella Academy", "start", 4, 1),
    Evento("The Umbrella Academy", "stop", 5, 1),
]

def main() -> None:
    """
    Cria uma instância de ShowTracker e calcula os utilizadores ativos com base na lista de eventos.
    """
    tracker = ShowTracker()
    tracker.calculate_active_users_per_show(registry_list)


if __name__ == "__main__":
    main()
