from whisper_live.server import TranscriptionServer
from whisper_live.client import TranscriptionClient
import threading

if __name__ == "__main__":
    server = TranscriptionServer()
    server_thread = threading.Thread(target=server.run, args=("0.0.0.0",))
    server_thread.start()

    # client = TranscriptionClient("ssh.pistachio.life", 9097)
    client = TranscriptionClient("localhost", 9090)
    # sleep for 4 seconds to allow the server to start
    print("Starting client...")
    client()
