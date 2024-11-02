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

# Example usage
batch1 = Batch(1, "Batch A", "2024-10-01", "active", "First batch description")
connector1 = Connector(1, "Type A", "Specifications for Type A")
connector2 = Connector(2, "Type B", "Specifications for Type B")

batch1.add_connector(connector1)
batch1.add_connector(connector2)

# Displaying batch and its connectors
print(f"Batch: {batch1.batch_name}")
for connector in batch1.connectors:
    print(f" - Connector: {connector.connector_type}, Specs: {connector.specifications}")
