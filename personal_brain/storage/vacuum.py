def optimize_database(db_manager) -> None:
    cursor = db_manager.get_cursor()
    cursor.execute("VACUUM;")
    cursor.execute("ANALYZE;")
    db_manager.conn.commit()
