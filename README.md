# Crypto Trading Platform

Cloud-based algorithmic crypto trading platform (Binance).

## Skills / Modules
1. **Market Data Collection** — `services/market_data_collector` (in progress)
2. **Indicator Engine** — TBD
3. **Cloud Data Storage** — TimescaleDB (Postgres extension), schemas in `services/market_data_collector`
4. **Trading Engine** — TBD

## Local Dev Setup
1. Copy `.env.example` to `.env` and fill in secrets (never commit `.env`)
2. `docker compose up --build`
3. TimescaleDB available on `localhost:5432`
