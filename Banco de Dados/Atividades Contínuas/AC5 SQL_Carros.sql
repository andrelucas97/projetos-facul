CREATE TABLE Cliente
(
cpf VARCHAR(15),
nome VARCHAR(50) NOT NULL,
rg VARCHAR(12) NOT NULL,
sexo CHAR(1) NOT NULL,
endereco VARCHAR(50),

CONSTRAINT PK_CPF PRIMARY KEY (cpf),
CONSTRAINT CK_SEXO CHECK (sexo IN ('F','M')),
CONSTRAINT UN_RG UNIQUE (rg)
)


CREATE TABLE Veiculo
(
placa VARCHAR(8),
ano INT NOT NULL,
cor VARCHAR(10),
modelo VARCHAR(14) NOT NULL,
marca VARCHAR(10) NOT NULL,
cpf_cliente VARCHAR(15),


CONSTRAINT PK_PLACA PRIMARY KEY (placa),
CONSTRAINT FK_CPF_CLIENTE FOREIGN KEY (cpf_cliente) REFERENCES Cliente (cpf),
)

insert into Cliente
values	(11111111111, 'Carla', 111111111, 'F', 'Rua barata ribeiro 408'),
		(22222222222, 'Fernando', 222222222, 'M', 'Rua da passagem 22'),
		(33333333333, 'Roberta', 333333333, 'F', 'Rua santo andre 55')

insert into Veiculo
values	('ABC-1234', 2002, 'azul', 'uno', 'fiat', 11111111111),
		('DEF-2345', 2005, 'prata', 'fox', 'volkswagen', 22222222222),
		('FGH-4567', 2007, 'preto', 'KA', 'ford', 33333333333)

select nome, cpf
from Cliente

select cpf
from Cliente

select *
from Cliente

select marca
from Veiculo

select nome, cpf
from Cliente
WHERE sexo = 'F'

select cpf
from Cliente
where sexo = 'M' and rg>111111111

select *
from Cliente
where sexo = 'M' or cpf=11111111111

select placa
from Veiculo
where modelo='KA' and cor='azul'

select modelo
from Veiculo
where marca='ford' or ano=2018

select modelo, marca, cor
from Veiculo
where marca IN ('ford', 'volkswagen')

select marca
from Veiculo
where ano between 2018 and 2020

select modelo, marca
from Veiculo
where ano between 2018 and 2020
order by ano 