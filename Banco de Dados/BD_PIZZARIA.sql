create table Cliente(

codigo INT,
nome VARCHAR (30) not null,
senha VARCHAR (15) not null,
email VARCHAR (150) not null,
rua CHAR (100) not null,
numero INT not null,
complemento VARCHAR(10),
telefone_comercial INT,
telefone_domestico INT not null 

constraint PK_CODIGO primary key (codigo)
)

create table Pedido(
numero INT,
dataPedido SMALLDATETIME not null,
origem VARCHAR(150) not null,
forma_pagamento VARCHAR(50) not null,
codigoCliente INT

constraint PK_NUMERO Primary key (numero),
constraint FK_CODIGOCLIENTE Foreign key (codigoCliente) REFERENCES Cliente(codigo)
)


create table Pizza(
codigo INT,
nome VARCHAR(100) not null,
ingrediente1 VARCHAR (100) not null,
ingrediente2 VARCHAR (100)

constraint PF_codigo Primary key (codigo)
)

create table Tamanho(
descricao VARCHAR(50),
codigoPizza INT

constraint PK_DESCRICAO_CODIGOPIZZA Primary key (descricao, codigoPizza),
constraint FK_CODIGOPIZZA Foreign key (codigoPizza) REFERENCES Pizza (codigo)
)

create table Contem(
descricao VARCHAR(50),
codigoPizza INT,
numeroPedido INT,
quantidade INT not null,
preco FLOAT(10) not null,

constraint PK_descricao_codigoPizza_numeroPedido Primary Key (descricao, codigoPizza, numeroPedido),
constraint FK_numeroPedido Foreign Key (numeroPedido) REFERENCES Pedido(numero),
constraint FK_descricao Foreign Key (descricao, codigoPizza) references Tamanho(descricao, codigoPizza)
)

insert into Cliente
values	(1, 'André Lucas', 'abcd1234', 'andrelucas97@email.com', 'Avenida Parada Pinto', 3696, '14C',NULL, '1111111111'),
		(2, 'Thiago Alberto', '1234abc', 'thiaguinho@email.com', 'Rua Joao Carlos', 150, NULL ,NULL, '1122222222')

insert into Pedido
values	(1, '20200519 21:39', 'Avenida Parada Pinto, 3696, 14C', 'dinheiro', 1),
		(2, '20200519 21:42', 'Rua Pedro Justos, 96', 'Cartão', 2)

insert into Pizza
values	(1, 'Frango c cat', 'frango', 'catupiry'),
		(5, 'Queijo', 'Queijo', NULL)

insert into Tamanho
values	('Grande', 1),
		('Brotinho', 5)

insert into Contem
values	('Grande', 1, 1, 2, 70.89),
		('Brotinho', 5, 2, 3, 105.75)

select nome
from Cliente

select origem
from Pedido

select ingrediente1
from Pizza

select rua, numero, complemento
from Cliente
WHERE complemento is not null

select nome, ingrediente1, ingrediente2
from Pizza
where ingrediente2 is not null

select numero, dataPedido, forma_pagamento
from Pedido
where forma_pagamento = 'dinheiro'

select descricao, codigoPizza
from Tamanho
where descricao = 'Grande' or 'Brotinho' = descricao

select ingrediente2, ingrediente1
from Pizza
where ingrediente1 = 'frango' or 'Queijo' = ingrediente1






