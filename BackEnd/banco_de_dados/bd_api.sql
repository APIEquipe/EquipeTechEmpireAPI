create database api;
use api;

create table comparacao(
comp_id int primary key not null auto_increment,
comp_nome varchar(50) not null
);

create table tipo_processo(
tp_id int primary key not null auto_increment,
tp_nome varchar(50) not null
);

create table processo(
pro_id int primary key not null auto_increment,
tp_id int not null,
foreign key(tp_id) references tipo_processo(tp_id),
pro_nome varchar(50) not null,
pro_desc varchar(150)
);

create table cidades(
cid_id int primary key not null auto_increment,
cid_nome varchar(50) not null
);

create table ano(
ano_id int primary key not null auto_increment,
ano_nome varchar(4) not null
);

create table consultar(
cons_id int primary key not null auto_increment,
cons_link varchar(200) not null,
cons_desc varchar(45),
comp_id int not null,
foreign key(comp_id) references comparacao(comp_id),
pro_id int not null,
foreign key(pro_id) references processo(pro_id),
cid_id int not null,
foreign key(cid_id) references cidades(cid_id),
ano_id int not null,
foreign key(ano_id) references ano(ano_id)
);

create table gastos(
gast_id int primary key not null auto_increment,
gast_link varchar(200) not null,
gast_desc varchar(45),
comp_id int not null,
foreign key(comp_id) references comparacao(comp_id),
pro_id int not null,
foreign key(pro_id) references processo(pro_id),
cid_id int not null,
foreign key(cid_id) references cidades(cid_id),
ano_id int not null,
foreign key(ano_id) references ano(ano_id)
);