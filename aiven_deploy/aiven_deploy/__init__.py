import pymysql

pymysql.version_info = (2, 2, 1, "final", 0)  # Fake version >= 2.2.1
pymysql.install_as_MySQLdb()
