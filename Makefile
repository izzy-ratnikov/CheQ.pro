create_suite: # запускает тест создания suite
	pytest tests/test_cheq.py -k test_create_suite

log_out_of_account: # запускает тест выхода из системы
	pytest tests/test_cheq.py -k test_log_out_of_account

open_project: # запускает тест открытия проекта
	pytest tests/test_cheq.py -k test_open_project


login: # запускает тест входа
	pytest tests/test_cheq.py -k test_login


registration: # запускает тест регистрация
	pytest tests/test_cheq.py -k test_registration