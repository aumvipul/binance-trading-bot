import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_inputs
from bot.logging_config import setup_logging

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price", required=False)

    args = parser.parse_args()

    try:
        validate_inputs(args.symbol, args.side, args.type, args.quantity, args.price)

        client = get_client()

        order = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n✅ ORDER SUCCESS")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))

    except Exception as e:
        print("\n❌ ERROR:", str(e))


if __name__ == "__main__":
    main()