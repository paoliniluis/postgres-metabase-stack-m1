Contents of this docker-compose
===============================


This is the old school Metabase + postgreSQL as the Application database + a postgres with the sample db and a postgres with fake data

- Metabase is exposed through port 3000
- PosgreSQL is exposed through port 5432, 5435 and 5433. You can see the credentials in the docker-compose.yaml file

All containers are in the same metanet1 network and you can wipe postgreSQL database by doing sudo `rm -rf /postgres_origin` on this folder (/environments/postgres)

The postgres DB's will be connected directly and through an SSH tunnel as well