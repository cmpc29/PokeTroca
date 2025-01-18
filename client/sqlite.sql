CREATE TABLE test (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dexID INTERGER NOT NULL,
    species TEXT NOT NULL,
    tipo1 TEXT NOT NULL,
    tipo2 TEXT,
    category TEXT NOT NULL,
    height INTEGER NOT NULL,
    weight INTEGER NOT NULL,
    description TEXT NOT NULL,
    ability TEXT NOT NULL
);

-- DROP TABLE dex

 
-- ALTER TABlE dex DROP COLUMN regiao;
-- INSERT INTO dex (pokeEspecie,tipo1,nivel,shiny)
-- VALUES ('pidgey','voador',12,'True');
-- DELETE FROM dex WHERE pokeEspecie='pidgey';
-- SELECT * FROM dex_local;

