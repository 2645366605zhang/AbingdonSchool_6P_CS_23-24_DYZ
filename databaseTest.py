import sqlite3 as sql
import os

FILE_PATH = "dbfile/tutorial.db"

# Ensure directory exists
os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)

if os.path.exists(FILE_PATH):
    os.remove(FILE_PATH)

with sql.connect(FILE_PATH) as conn:
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE movie(title, year, score)
    """)
    
    test_result = cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE name = "spam"
    """)
    
    print(test_result.fetchone() is None)  # True
    
    cursor.execute("""
        INSERT INTO movie VALUES (?, ?, ?),
            (?, ?, ?)
    """, (
        "Monty Python and the Holy Grail", 1975, 8.2,
        "And Now for Something Completely Different", 1971, 7.5
    ))
    
    test_result = cursor.execute("""
        SELECT score FROM movie
    """)
    
    print(test_result.fetchall())  # [(8.2,), (7.5,)]
    
    example_data = [
        ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
        ("Monty Python's The Meaning of Life", 1983, 7.5),
        ("Monty Python's Life of Brian", 1979, 8.0),
    ]
    
    cursor.executemany("""
        INSERT INTO movie VALUES (?, ?, ?)
    """, example_data)
    
    conn.commit()
    
    for row in cursor.execute("""
        SELECT year, title
        FROM movie
        ORDER BY year
    """):
        print(row)
    # (1971, 'And Now for Something Completely Different')
    # (1975, 'Monty Python and the Holy Grail')
    # (1979, "Monty Python's Life of Brian")
    # (1982, 'Monty Python Live at the Hollywood Bowl')
    # (1983, "Monty Python's The Meaning of Life")

with sql.connect(FILE_PATH) as new_conn:
    new_cursor = new_conn.cursor()
    
    new_result = new_cursor.execute("""
        SELECT year, title
        FROM movie
        ORDER BY year DESC
    """)
    
    print(f"The The highest scoring Monty Python movie is {new_result.fetchone()[1]!r}, released in {new_result.fetchone()[0]}")
    # The The highest scoring Monty Python movie is "Monty Python's The Meaning of Life", released in 1982
