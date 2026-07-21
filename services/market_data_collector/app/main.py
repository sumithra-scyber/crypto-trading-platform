# Entry point for market_data_collector service
# TODO: wire up rest_backfill, ws_manager, symbol_poller to run concurrently (asyncio)


def main():
    print("market_data_collector starting...")


if __name__ == "__main__":
    main()
