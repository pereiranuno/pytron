def report_active_users(event_list):
    # Passo 1: Inicializar estruturas de dados
    active_users_per_show = {}
    all_shows = set(event['show'] for event in event_list)
    
    # Passo 2: Ordenar a lista de eventos
    sorted_events = sorted(event_list, key=lambda x: x['timestamp'])
    
    # Passo 3: Processar cada evento
    for event in sorted_events:
        show = event['show']
        event_type = event['event']
        user_id = event['user_id']
        
        if event_type == 'start':
            if show not in active_users_per_show:
                active_users_per_show[show] = set()
            active_users_per_show[show].add(user_id)
        elif event_type == 'stop':
            if show in active_users_per_show and user_id in active_users_per_show[show]:
                active_users_per_show[show].remove(user_id)
    
    # Passo 4: Gerar o relatório
    print(all_shows)
    for show in all_shows:
        num_users = len(active_users_per_show.get(show, set()))
        print(f"{show}: {num_users}")

registry_list = [
    {
        "show": "The Witcher",
        "event": "start",
        "timestamp": 0,
        "user_id": 1
    },
    {
        "show": "The Witcher",
        "event": "start",
        "timestamp": 1,
        "user_id": 2
    },
    {
        "show": "The Witcher",
        "event": "stop",
        "timestamp": 3,
        "user_id": 2
    },
    {
        "show": "The Umbrella Academy",
        "event": "start",
        "timestamp": 4,
        "user_id": 1
    },
    {
        "show": "The Umbrella Academy",
        "event": "stop",
        "timestamp": 5,
        "user_id": 1
    },
]

report_active_users(registry_list)