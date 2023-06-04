-- André Lucas Fabbris de Toledo
-- RA 1902777

USE BD_CARROS

CREATE TABLE Cliente (
	Cpf VARCHAR (14),
	Nome CHAR (30)NOT NULL,
	Rg VARCHAR (12)NOT NULL,
	Sexo CHAR NOT NULL,
	endereco VARCHAR (20)

	CONSTRAINT PK_Cpf PRIMARY KEY (Cpf),
	CONSTRAINT CK_Sexo CHECK (Sexo IN ('F', 'M')),
	CONSTRAINT UN_Rg UNIQUE (Rg)
	)

CREATE TABLE Veiculo (
	Placa VARCHAR,
	Ano INT NOT NULL,
	Cor CHAR,
	Modelo CHAR NOT NULL,
	Marca CHAR NOT NULL,
	Cpf_cliente VARCHAR (14)

	CONSTRAINT PK_Placa PRIMARY KEY (Placa),
	CONSTRAINT FK_Cpf_cliente FOREIGN KEY (Cpf_cliente) REFERENCES Cliente(Cpf)

	)










