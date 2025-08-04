create database bdBuffet;

use bdBuffet;

create table usuario(id integer primary key auto_increment,
                                        nome varchar (100),
                                        email varchar (70),
                                        celular varchar(20),
                                        cpf varchar (20),
                                        rua varchar (45),
                                        bairro varchar (45),
                                        numero varchar(10),
                                        cidade varchar (45),
                                        uf varchar (50),
                                        cep varchar(20),
                                        senha varchar (45));


create table admin(id integer primary key auto_increment,
                                    nome_adm varchar (45),
                                    email_adm varchar (45),
                                    celular_adm varchar(19),
                                    senha_adm varchar (45));
                        

                                        