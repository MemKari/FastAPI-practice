fake_users = [
    {'id': 100, 'name': 'Bob', 'role': 'admin', 'degree': 'newbie', 'email': '', },
    {'id': 101, 'name': 'Mark', 'role': 'trader', 'degree': 'newbie', 'email': '', },
    {'id': 102, 'name': 'Lola', 'role': 'trader', 'degree': 'newbie', 'email': '', },
    {'id': 103, 'name': 'Robert', 'role': 'trader', 'degree':
        {'id': 2, 'created_at': '2024-05-22T21:09:33.072Z', 'type_degree': 'expert'},
     'email': 'alice@example.com', },
    {'id': 104, 'name': 'Ola', 'role': 'trader', 'degree':
        {'id': 1, 'created_at': '2024-05-22T21:09:33.072Z', 'type_degree': 'expert'},
     'email': '100500wrong@@example.com',
     },
]

fake_trades = [
    {'trade_id': 1005, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 0.37, 'amount': 100, },
    {'trade_id': 1006, 'user_id': 2, 'currency': 'BTC', 'side': 'sell', 'price': 0.37, 'amount': 200, },
    {'trade_id': 1007, 'user_id': 3, 'currency': 'BTC', 'side': 'sell', 'price': 0.37, 'amount': 300, },
    {'trade_id': 1008, 'user_id': 4, 'currency': 'BTC', 'side': 'buy', 'price': 0.37, 'amount': 400, },
    {'trade_id': 1009, 'user_id': 1, 'currency': 'BTC', 'side': 'sell', 'price': 0.37, 'amount': 500, },
    {'trade_id': 1010, 'user_id': 5, 'currency': 'BTC', 'side': 'sell', 'price': 0.37, 'amount': 600, },
    {'trade_id': 1011, 'user_id': 3, 'currency': 'BTC', 'side': 'buy', 'price': 0.37, 'amount': 700, },
]
