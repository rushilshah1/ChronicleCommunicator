create schema if not exists chronicle;

create table if not exists chronicle.user(
	user_id SERIAL primary key,
	first_name varchar not null,
	last_name varchar not null,
	email varchar not null,
	phone varchar not null,
	group_id integer,
	company_id integer not null,
	account_id integer not null,
	created_ts timestamp without time zone not null,
	updated_ts timestamp without time zone not null,
	active boolean not null
);

create table if not exists chronicle.group(
	group_id serial primary key,
	company_id varchar not null,
	description varchar,
	created_ts timestamp without time zone not null,
	updated_ts timestamp without time zone not null,
	active boolean not null
);
create table if not exists chronicle.message(
	template_id serial primary key,
	channel_type varchar not null,
	message_template varchar not null,
	subject varchar,
	user_id integer,
	group_id integer,
	company_id integer not null,
	active boolean not null
);

ALTER TABLE chronicle.user
ADD CONSTRAINT group_id_fk FOREIGN KEY (group_id) REFERENCES chronicle.group(group_id);
ALTER TABLE chronicle.message
ADD CONSTRAINT user_id_fk FOREIGN KEY (user_id) REFERENCES chronicle.user(user_id);
ALTER TABLE chronicle.message
ADD CONSTRAINT group_id_fk FOREIGN KEY (group_id) REFERENCES chronicle.group(group_id);