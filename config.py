config = {
    'WIN_SIZE': (1280, 720),
    'TASKS_1': 3, # 1 тип
    'TASKS_2': 3, # 2 тип(a.k.a. 1,5)
    'TASKS_3': 3, # 3 тип(его нету)
    'TIME': 60, # время в минутах
    'IP': 'localhost',
    'VRATES': [ # оценки
        90, # >=90% - 5
        70, # >=70% - 4
        50, # >=50% - 3
        1, # >=1% - 2
        0 # =0% - 1
    ]
}
