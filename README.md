# What's this

It's a simple stack of Metabase + a Postgres DB to test in Macs with M processor.

## Why

As the M chip can't work well with x86 containers, this is a project that wraps Metabase inside a Ubuntu container so it works

## How

1) install docker
2) clone this repo
3) do "docker-compose up --build" on the root

The Dockerfile on the root uses v46.4 of Metabase, so if you need to use another version, change that line to the version you need and rebuild

## Credentials

it's configured with a@b.com // metabot1 username and password