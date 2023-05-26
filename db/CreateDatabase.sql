USE python;

CREATE TABLE carros (
    id integer not null auto_increment,
    marca varchar(100),
    modelo varchar(100),
    ano integer,
    PRIMARY KEY (id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

INSERT INTO carros (marca, modelo, ano) VALUES ('Toyota', 'Corola Trueno', 1986);
INSERT INTO carros (marca, modelo, ano) VALUES ('Nissan', 'Skyline GTR R34', 1998);
INSERT INTO carros (marca, modelo, ano) VALUES ('Mazda', 'Miata RX-7', 1994);
INSERT INTO carros (marca, modelo, ano) VALUES ('Toyota', 'Supra', 1999);
INSERT INTO carros (marca, modelo, ano) VALUES ('Honda', 'Civic Coupe', 1993);
