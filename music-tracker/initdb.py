import sqlite3


class SQLiteManager:
	def __init__(self, db_file):
		self.db_file = db_file

	def create_connection(self):
		conn = None
		try:
			conn = sqlite3.connect(self.db_file)
			print(f'Running sqlite version {sqlite3.version}')
		except sqlite3.Error as e:
			print(e)
		finally:
			if conn:
				conn.close()

	def create_tables(self):
		pass
