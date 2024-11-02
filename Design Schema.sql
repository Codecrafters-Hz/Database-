USE MyDatabase; 
CREATE TABLE Battch (
    BatchId UNIQUEIDENTIFIER PRIMARY KEY,
    BatchNumber VARCHAR(10) UNIQUE NOT NULL
);
CREATE TABLE Connector (
    Connector_ID UNIQUEIDENTIFIER PRIMARY KEY,
    BatchId UNIQUEIDENTIFIER,
    ConnectorNumber VARCHAR(10),
    Status VARCHAR(20),
    Timestamp DATETIME,
    FOREIGN KEY (BatchId) REFERENCES Batch(BatchId)
);
CREATE TABLE ConnectorData (
    Connector_ID UNIQUEIDENTIFIER,
    Data NVARCHAR(MAX),
    Timestamp DATETIME,
    FOREIGN KEY (Connector_ID) REFERENCES Connector(Connector_ID)
);

DECLARE @BatchId UNIQUEIDENTIFIER = NEWID();  
DECLARE @BatchNumber VARCHAR(10) = 'B1000';  

INSERT INTO dbo.Batch (BatchId, BatchNumber)
VALUES (@BatchId, @BatchNumber);

DECLARE @Connector_ID UNIQUEIDENTIFIER = NEWID();  
DECLARE @ConnectorNumber VARCHAR(10) = 'B1000-1';  
DECLARE @Status VARCHAR(20) = 'Connected'; 



BEGIN TRANSACTION;

DECLARE @BatchId UNIQUEIDENTIFIER = NEWID();  -- Generate new Batch ID
DECLARE @BatchNumber VARCHAR(10) = 'B1000';   -- Set Batch Number

INSERT INTO dbo.Batch (BatchId, BatchNumber)
VALUES (@BatchId, @BatchNumber);

COMMIT;




