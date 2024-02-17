const { Sequelize } = require('sequelize');
import { generate } from "random-words";

const config = {
  dialect: 'postgres',
  host: 'localhost',
  port: 5433,
  database: 'sample',
  username: 'metabase',
  password: 'metasample123',
};


const sequelize = new Sequelize(config);

let counter = 0;
let schema_name = generate().concat("_1");

while (true) {
  try {
    if (counter == 10) {
      counter = 0;
      schema_name = generate().concat(Math.floor(Math.random() * 100) + 1);
    }
    let table_name = generate().concat(Math.floor(Math.random() * 100) + 1);
    await sequelize.query(`CREATE SCHEMA IF NOT EXISTS "${schema_name}";`);
    await sequelize.query(`CREATE TABLE IF NOT EXISTS "${schema_name}"."${table_name}" (
      "${generate().concat(Math.floor(Math.random() * 100) + 1)}" SMALLINT,
      "${generate().concat(Math.floor(Math.random() * 100) + 1)}" VARCHAR(255),
      "${generate().concat(Math.floor(Math.random() * 100) + 1)}" CHAR(10),
      "${generate().concat(Math.floor(Math.random() * 100) + 1)}" BIGINT,
      "${generate().concat(Math.floor(Math.random() * 100) + 1)}" SMALLINT,
      "${generate().concat(Math.floor(Math.random() * 100) + 1)}" DECIMAL(10,2),
      "${generate().concat(Math.floor(Math.random() * 100) + 1)}" REAL,
      "${generate().concat(Math.floor(Math.random() * 100) + 1)}" DOUBLE PRECISION,
      "${generate().concat(Math.floor(Math.random() * 100) + 1)}" BOOLEAN,
      "${generate().concat(Math.floor(Math.random() * 100) + 1)}" DATE,
      "${generate().concat(Math.floor(Math.random() * 100) + 1)}" TIMESTAMP,
      "${generate().concat(Math.floor(Math.random() * 100) + 1)}" TIMESTAMPTZ,
      "${generate().concat(Math.floor(Math.random() * 100) + 1)}" VARCHAR(10),
      "${generate().concat(Math.floor(Math.random() * 100) + 1)}" CHAR(10)
    );`);
    await sequelize.query(`INSERT INTO "${schema_name}"."${table_name}" VALUES 
    (1, 'test', 'test', 1, 1, 1.1, 1.1, 1.1, true, '2021-01-01', '2021-01-01 00:00:00', '2021-01-01 00:00:00', 'test', 'test'),
    (1, 'test', 'test', 1, 1, 1.1, 1.1, 1.1, true, '2021-01-01', '2021-01-01 00:00:00', '2021-01-01 00:00:00', 'test', 'test'),
    (1, 'test', 'test', 1, 1, 1.1, 1.1, 1.1, true, '2021-01-01', '2021-01-01 00:00:00', '2021-01-01 00:00:00', 'test', 'test'),
    (1, 'test', 'test', 1, 1, 1.1, 1.1, 1.1, true, '2021-01-01', '2021-01-01 00:00:00', '2021-01-01 00:00:00', 'test', 'test'),
    (1, 'test', 'test', 1, 1, 1.1, 1.1, 1.1, true, '2021-01-01', '2021-01-01 00:00:00', '2021-01-01 00:00:00', 'test', 'test'),
    (1, 'test', 'test', 1, 1, 1.1, 1.1, 1.1, true, '2021-01-01', '2021-01-01 00:00:00', '2021-01-01 00:00:00', 'test', 'test'),
    (1, 'test', 'test', 1, 1, 1.1, 1.1, 1.1, true, '2021-01-01', '2021-01-01 00:00:00', '2021-01-01 00:00:00', 'test', 'test'),
    (1, 'test', 'test', 1, 1, 1.1, 1.1, 1.1, true, '2021-01-01', '2021-01-01 00:00:00', '2021-01-01 00:00:00', 'test', 'test'),
    (1, 'test', 'test', 1, 1, 1.1, 1.1, 1.1, true, '2021-01-01', '2021-01-01 00:00:00', '2021-01-01 00:00:00', 'test', 'test'),
    (1, 'test', 'test', 1, 1, 1.1, 1.1, 1.1, true, '2021-01-01', '2021-01-01 00:00:00', '2021-01-01 00:00:00', 'test', 'test'),
    (1, 'test', 'test', 1, 1, 1.1, 1.1, 1.1, true, '2021-01-01', '2021-01-01 00:00:00', '2021-01-01 00:00:00', 'test', 'test')
    ;`);
    counter++;
  } catch (err) {
    console.log(err);
  }
}