create schema if not exists chronicle;
--DDL to create tables
CREATE TABLE if not exists chronicle."user" (
	user_id serial NOT NULL,
	first_name text NOT NULL,
	last_name text NOT NULL,
	email text NOT NULL,
	phone text NULL,
	group_id int4 NULL,
	company_id int4 NOT NULL,
	account_id int4 NOT NULL,
	created_ts timestamp NOT NULL,
	updated_ts timestamp NOT NULL,
	active bool NOT NULL,
	CONSTRAINT user_pkey PRIMARY KEY (user_id)
);

CREATE TABLE if not exists chronicle."group" (
	group_id serial NOT NULL,
	description text NOT NULL,
	company_id int4 NOT NULL,
	created_ts timestamp NOT NULL,
	updated_ts timestamp NOT NULL,
	active bool NOT NULL,
	CONSTRAINT group_pkey PRIMARY KEY (group_id)
);
CREATE TYPE channeltype AS ENUM('SMS', 'EMAIL', 'APP', 'PUSH');
CREATE TABLE if not exists chronicle.message (
	message_id serial NOT NULL,
	channel_type channeltype NOT NULL,
	message_template text NOT NULL,
	group_id int4 NOT NULL,
	company_id int4 NOT NULL,
	created_ts timestamp NOT NULL,
	updated_ts timestamp NOT NULL,
	active bool NOT NULL,
	CONSTRAINT message_pkey PRIMARY KEY (message_id)
);

--Adding test data
INSERT INTO chronicle."user"
(first_name, last_name, email, phone, group_id, company_id, account_id, created_ts, updated_ts, active)
VALUES('Rushil', 'Shah', 'rushilrshah1@gmail.com', '4128004543', 1, 1, 1234563349, current_timestamp , current_timestamp, true);

INSERT INTO chronicle."group"
(description, company_id, created_ts, updated_ts, active)
VALUES('The main target demographic of Company 1', 1, current_timestamp, current_timestamp, true);

INSERT INTO chronicle."message"
(channel_type, message_template, group_id, company_id, created_ts, updated_ts, active)
VALUES('EMAIL', 'Hi :first_name,

This is a test email to remind you your minimum payment is due for :account_id by tomorrow. Please pay at https://www.google.com/

The link in the email can help measure engagement of the message (If I clicked and went to the site I can capture the activity from this message)

- Chronicle', 1, 1, '2020-04-14 00:56:25.549', '2020-04-14 01:09:47.390', true);


-- Skipping adding foreign keys to allow more flexibilty to test MVP (ex add user with groupId before groupId exists)
