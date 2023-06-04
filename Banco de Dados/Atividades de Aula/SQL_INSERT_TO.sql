USE BD_HOSPITAL

CREATE TABLE Convenio (
	codigo int,
	nome varchar not null,
	data_inicio datetime not null

	constraint PK_CODIGO primary key (codigo)
)

CREATE TABLE Paciente
(
	codigo INT,
	cd_convenio INT,
	nome VARCHAR(50) NOT NULL,
	sexo CHAR(1) NOT NULL,
	cpf VARCHAR(14) NOT NULL,
	rg VARCHAR(12) NOT NULL,
	nome_pai VARCHAR(50),
	nome_mae VARCHAR(50),
	endereco VARCHAR(150),
	telefone VARCHAR(13),
	email VARCHAR(150),

CONSTRAINT PK_CDPACIENTE PRIMARY KEY (codigo),
CONSTRAINT FK_CDCONVENIO FOREIGN KEY (cd_convenio) REFERENCES Convenio (codigo),
CONSTRAINT CK_SEXO CHECK (sexo IN ('F','M')),
CONSTRAINT UN_RG UNIQUE (rg)
)

INSERT INTO Paciente (Codigo, nome, sexo, CPF, RG, nome_pai, nome_mae, cd_convenio, endereco, telefone, email) VALUES (1, 'Patricia', 'f', 11111111111, 111111111, 'Carlos Souza', 'Anita Souza', 1, 'rua dos amores 3', 1111111111, 'patricia@gmail.com')
INSERT INTO Paciente (Codigo, nome, sexo, CPF, RG, nome_pai, nome_mae, cd_convenio, endereco, telefone, email) VALUES (2, 'Michele', 'f', 22222222222, 222222222, 'Abel Silva', 'Carla Silva', 2, 'rua das arvores 5', 1122222222, 'michele@gmail.com')
INSERT INTO Paciente (Codigo, nome, sexo, CPF, RG, nome_pai, nome_mae, cd_convenio, endereco, telefone, email) VALUES (3, 'Luisa', 'f', 33333333333, 333333333, 'Osvaldo Aranha', 'Marcia Ferreira', 1, 'av rudge 6', 1133333333, 'luisa@gmail.com')
INSERT INTO Paciente (Codigo, nome, sexo, CPF, RG, nome_pai, nome_mae, cd_convenio, endereco, telefone, email) VALUES (4, 'Alberto','m', 44444444444, 444444444, 'Sebastiao Mendonça', 'Helena Figueira', 3, 'avenida brasil 3', 1144444444, 'alberto@gmail.com')
INSERT INTO Paciente (Codigo, nome, sexo, CPF, RG, nome_pai, nome_mae, cd_convenio, endereco, telefone, email) VALUES (5, 'Emerson', 'm', 55555555555, 555555555, 'Roberto Damiao', 'Lucia Souza', 3, 'avenida são sebastiao 6', 1155555555, 'emerson@gmail.com')

INSERT INTO Convenio (Codigo, nome, data_inicio) VALUES (1, 'Unimed', 10/02/1995)
INSERT INTO Convenio (Codigo, nome, data_inicio) VALUES (2, 'Amil', 09/09/1998)
INSERT INTO Convenio (Codigo, nome, data_inicio) VALUES (3, 'Prevent Senior', 16/03/2000)
