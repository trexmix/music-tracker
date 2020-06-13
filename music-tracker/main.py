from initdb import SQLiteManager

if __name__ == '__main__':
	manager = SQLiteManager('C:\\Users\\T530\\Documents\\music-tracker\\db\\dev.db')
	manager.create_connection()