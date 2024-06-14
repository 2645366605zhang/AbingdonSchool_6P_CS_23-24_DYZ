import sqlite3 as sql
import os

FILE_PATH = "dbfile/tutorial.db"

if os.path.exists(FILE_PATH):
    os.remove(FILE_PATH)

databaseConnection = sql.connect(FILE_PATH)

databaseCursor = databaseConnection.cursor()

databaseCursor.execute("""
    CREATE TABLE
        movie(title, year, score)
""")

testResult = databaseCursor.execute("""
    SELECT
        name
    FROM
        sqlite_master
    WHERE
        name = "spam"
""")

print(testResult.fetchone() is None)
# True

databaseCursor.execute("""
    INSERT INTO
        movie
    VALUES
        ("Monty Python and the Holy Grail", 1975, 8.2), 
        ("And Now for Something Completely Different", 1971, 7.5)
""")

databaseConnection.commit()

testResult = databaseCursor.execute("""
    SELECT
        score
    FROM
        movie
""")

print(testResult.fetchall())
# [(8.2,), (7.5,)]

exampleData = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]

databaseCursor.executemany("""
    INSERT INTO
        movie
    VALUES(
        ?, ?, ?
    )
""", exampleData)

databaseConnection.commit()

for row in databaseCursor.execute("""
    SELECT
        year, 
        title
    FROM
        movie
    ORDER BY
        year
"""):
    print(row)
# (1971, 'And Now for Something Completely Different')
# (1975, 'Monty Python and the Holy Grail')
# (1979, "Monty Python's Life of Brian")
# (1982, 'Monty Python Live at the Hollywood Bowl')
# (1983, "Monty Python's The Meaning of Life")

databaseConnection.close()

newDatabaseConnection = sql.connect(FILE_PATH)

newCursor = newDatabaseConnection.cursor()

newResult = newCursor.execute("""
    SELECT
        year, 
        title
    FROM
        movie
    ORDER BY
        year
    DESC
""")

print(f"The The highest scoring Monty Python movie is {newResult.fetchone()[1]!r}, released in {newResult.fetchone()[0]}")
# The highest scoring Monty Python movie is 'Monty Python and the Holy Grail', released in 1975