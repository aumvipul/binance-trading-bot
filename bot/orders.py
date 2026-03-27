import logging

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            if not price:
                raise ValueError("Price required for LIMIT order")

            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        # ✅ Extract useful fields
        order_id = order.get("orderId")
        status = order.get("status")
        executed_qty = order.get("executedQty")
        avg_price = order.get("avgPrice", "N/A")

        # ✅ Log structured response
        logging.info(
            f"Order Response: ID={order_id}, Status={status}, "
            f"ExecutedQty={executed_qty}, AvgPrice={avg_price}"
        )

        # ✅ Return clean structured data
        return {
            "orderId": order_id,
            "status": status,
            "executedQty": executed_qty,
            "avgPrice": avg_price
        }

    except Exception as e:
        logging.error(f"Error placing order: {e}")
        raise