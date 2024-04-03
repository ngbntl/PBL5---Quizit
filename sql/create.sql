--USE master;
--GO
--ALTER DATABASE trac_nghiem SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
--GO
--DROP DATABASE trac_nghiem;
--GO

-- admin
create table [admin] (
	[id]                char(8),
	[username]          varchar(255),
	[hash_pswd]         varchar(255),
	[name]              nvarchar(255),
	[is_banned]         bit            default 0,
	-- constraint
	constraint [pk_adm] primary key ([id]),
	constraint [unq_adm_username] unique ([username]),
)

-- student
create table [student] (
	[id]                char(8),
	[email]             varchar(100) not null,
	[name]              nvarchar(100),
	[hash_pswd]         varchar(255),
	[avatar_path]       varchar(255),
	[is_banned]         bit          default 0,
	[created_timestamp] datetime     default getdate(),
	[is_verified]       bit          default 0,
	-- constraint
	constraint [pk_stu]      primary key ([id]),
	constraint [unq_stu_ema] unique ([email])
)

CREATE INDEX [idx_stu_ema] ON [student] ([email]);

-- teacher
create table [teacher] (
	[id]                char(8),
	[email]             varchar(100)  not null,
	[name]              nvarchar(100),
	[hash_pswd]         varchar(255),
	[avatar_path]       varchar(255),
	[is_banned]         bit         default 0,
	[created_timestamp] datetime    default getdate(),
	[is_verified]       bit         default 0,
	-- constraint
	constraint [pk_tch]      primary key ([id]),
	constraint [unq_tch_ema] unique ([email])
)

CREATE INDEX [idx_tch_ema] ON [teacher] ([email]);

-- group
create table [group] (
	[id]                char(8),
	[name]              nvarchar(100),
	[teacher_id]        char(8)        not null,
	[created_timestamp] datetime       default getdate(),
	[is_show]           bit            default(1),
	-- constraint
	constraint [pk_grp]     primary key ([id]),
	constraint [fk_grp_tch] foreign key ([teacher_id]) references [teacher](id),
)

-- group student
create table [group_student] (
	[group_id]          char(8) not null,
	[student_id]        char(8) not null,
	[is_join]           bit     default 1,
	[request_timestamp] datetime       default getdate(),
	-- constraint
	constraint [pk_grstu] primary key ([group_id], [student_id]),
	constraint [fk_grstu_grp] foreign key ([group_id]) references [group](id),
	constraint [fk_grstu_stu] foreign key ([student_id]) references [student](id),
)

-- group_test
create table [group_test] (
	[id]                char(8),
	[group_id]          char(8)        not null,
	[test_path]         varchar(MAX),
	[start]             datetime,
	[end]               datetime,
	[created_timestamp] datetime       default getdate(),
	-- constraint
	constraint [pk_grtes] primary key ([id]),
	constraint [fk_grtes_grp] foreign key ([group_id]) references [group](id),
)

-- collection
create table [collection] (
	[id]                char(8),
	[teacher_id]        char(8)       not null,
	[name]              nvarchar(100),
	[created_timestamp] datetime       default getdate(),
	-- constraint
	constraint [pk_clt] primary key ([id]),
	constraint [fk_clt_tch] foreign key ([teacher_id]) references [teacher](id),
)

-- question_bank
create table [question_bank] (
	[id]                char(8),
	[collection_id]     char(8)         not null,
	[name]              nvarchar(100),
	[created_timestamp] datetime       default getdate(),
	-- constraint
	constraint [pk_quesbank] primary key ([id]),
	constraint [fk_quesbank_clt] foreign key ([collection_id]) references [collection](id),
)

-- generate_test
create table [generate_test] (
	[id]                char(8),
	[collection_id]     char(8)         not null,
	[name]              nvarchar(100),
	[created_timestamp] datetime       default getdate(),
	-- constraint
	constraint [pk_gentes] primary key ([id]),
	constraint [fk_gentes_clt] foreign key ([collection_id]) references [collection](id),
)

-- manual_test
create table [manual_test] (
	[id]                char(8),
	[collection_id]     char(8)         not null,
	[name]              nvarchar(100),
	[created_timestamp] datetime       default getdate(),
	-- constraint
	constraint [pk_manutes] primary key ([id]),
	constraint [fk_manutes_clt] foreign key ([collection_id]) references [collection](id),
)
