CREATE TABLE Users
(
    username varchar2(30) primary key,
    password varchar2(30),
    first_name varchar2(30),
    last_name varchar2(30),
    clan_tag varchar2(30),
    points number(5),
    fail_counter number(3),
    success_counter number(3)
);

CREATE TABLE Tasks
(
    task_id number(4) primary key,
    title varchar2(30),
    description varchar2(200),
    difficulty varchar2(10),
    deadline date,
    duration date,
    task_type varchar2(20),
    username varchar(30),
    
    constraint FK_task_user foreign key (username) references users (username) on delete cascade
);
