import websocket
import ssl

# Set up SSL context
ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_REQUIRED
ssl_context.check_hostname = True
ssl_context.load_default_certs()

# Set up WebSocket connection
ws = websocket.create_connection("wss://cekirdektenyetisenler.kartaca.com/ws", sslopt={"cert_reqs": ssl.CERT_REQUIRED, "ssl_version": ssl.PROTOCOL_TLSv1_2, "ssl_context": ssl_context})

# Receive encrypted message
result = ws.recv()

# Close WebSocket connection
ws.close()