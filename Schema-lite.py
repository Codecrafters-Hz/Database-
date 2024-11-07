import sqlite3
import uuid
from datetime import datetime

# Define the Batch and Connector classes
class Batch:
    def __init__(self, batch_id, batch_name, creation_date, status, description):
        self.batch_id = batch_id
        self.batch_name = batch_name
        self.creation_date = creation_date
        self.status = status
        self.description = description
        self.connectors = []

    def add_connector(self, connector):
        self.connectors.append(connector)

class Connector:
    def __init__(self, connector_id, connector_type, specifications):
        self.connector_id = connector_id
        self.connector_type = connector_type
        self.specifications = specifications

# Connect to SQLite database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS Batch (
    BatchId TEXT PRIMARY KEY,
    BatchName TEXT NOT NULL,
    CreationDate TEXT,
    Status TEXT,
    Description TEXT
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Connector (
    ConnectorId TEXT PRIMARY KEY,
    BatchId TEXT,
    ConnectorType TEXT,
    Specifications TEXT,
    FOREIGN KEY (BatchId) REFERENCES Batch(BatchId)
)
''')

# Insert data into Batch table

#sql lite does not ahve UNQIDEDENTIDIE so insted of that we create Uuid in below lines
batch_id = str(uuid.uuid4())
batch_name = "Batch A"
creation_date = "2024-10-01"
status = "active"
description = "First batch description"
cursor.execute('INSERT INTO Batch (BatchId, BatchName, CreationDate, Status, Description) VALUES (?, ?, ?, ?, ?)',
               (batch_id, batch_name, creation_date, status, description))

# Insert data into Connector table
connector1_id = str(uuid.uuid4())
connector2_id = str(uuid.uuid4())
connector1_type = "Type A"
connector2_type = "Type B"
specifications1 = "Specifications for Type A"
specifications2 = "Specifications for Type B"
cursor.execute('INSERT INTO Connector (ConnectorId, BatchId, ConnectorType, Specifications) VALUES (?, ?, ?, ?)',
               (connector1_id, batch_id, connector1_type, specifications1))
cursor.execute('INSERT INTO Connector (ConnectorId, BatchId, ConnectorType, Specifications) VALUES (?, ?, ?, ?)',
               (connector2_id, batch_id, connector2_type, specifications2))

# Commit the transaction
conn.commit()

# Retrieve data from the database
cursor.execute('SELECT * FROM Batch WHERE BatchId = ?', (batch_id,))
batch_row = cursor.fetchone()
batch = Batch(batch_row[0], batch_row[1], batch_row[2], batch_row[3], batch_row[4])

cursor.execute('SELECT * FROM Connector WHERE BatchId = ?', (batch_id,))
connector_rows = cursor.fetchall()
for row in connector_rows:
    connector = Connector(row[0], row[2], row[3])
    batch.add_connector(connector)

# Close the connection
conn.close()

# Displaying batch and its connectors
print(f"Batch: {batch.batch_name}")
for connector in batch.connectors:
    print(f" - Connector: {connector.connector_type}, Specs: {connector.specifications}")
