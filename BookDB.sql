create table book_bd
(
    bid     varchar(4)   null,
    book_bd varchar(100) null
);

create index book_id
    on book_bd (bid);

-- auto-generated definition
create table book_hrf
(
    id       int auto_increment
        primary key,
    bid      varchar(4)   null,
    itm_text varchar(100) null comment '书名',
    itm_er   varchar(100) null comment '作者',
    itm_href varchar(300) null comment '链接'
);

create trigger reset_auto_increment
    before insert
    on book_hrf
    for each row
BEGIN
    DECLARE current_count INT;
    SET current_count = (SELECT COUNT(*) FROM book_hrf);

    IF current_count = 0 THEN
        SET NEW.id = 1;
    ELSE
        SET NEW.id = current_count + 1;
    END IF;
END;
