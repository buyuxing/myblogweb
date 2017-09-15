drop database if exists myblog;

create database myblog;

use myblog;

grant select, insert, update, delete on myblog.* to 'buyuxing'@'localhost' identified by 'buyuxing';

create table BYXUser(
	`id` varchar(50) not null,
    `email` varchar(50) not null,
    `pwd` varchar(50) not null,
    `isAdmin` bool not null,
    `username` varchar(50) not null,
    `nickname` varchar(50),
    `img` varchar(500) not null,
    `createdAt` real not null,
    unique key `idx_email` (`email`),
    key `idx_createdAt` (`createdAt`),
    primary key (`id`)
)engine=innodb default charset=utf8;

create table BYXBlog (
    `id` varchar(50) not null,
    `userId` varchar(50) not null,
    `username` varchar(50) not null,
    `img` varchar(500) not null,
    `title` varchar(50) not null,
    `summary` varchar(200) not null,
    `content` mediumtext not null,
    `createdAt` real not null,
    key `idx_createdAt` (`createdAt`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table comments (
    `id` varchar(50) not null,
    `blogId` varchar(50) not null,
    `userId` varchar(50) not null,
    `username` varchar(50) not null,
    `img` varchar(500) not null,
    `content` mediumtext not null,
    `createdAt` real not null,
    key `idx_createdAt` (`createdAt`),
    primary key (`id`)
) engine=innodb default charset=utf8;