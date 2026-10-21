"""Exercise updated libraries without audio playback or vehicle access."""

import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import msgpack
import requests


class DependencyCompatibilityTests(unittest.TestCase):
    def test_http_redirect_and_payload(self):
        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                if self.path == "/redirect":
                    self.send_response(302)
                    self.send_header("Location", "/sound")
                    self.send_header("Content-Length", "0")
                    self.end_headers()
                    return
                payload = b"sound-fixture"
                self.send_response(200)
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)

            def log_message(self, *_args):
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with requests.Session() as session:
                session.trust_env = False
                response = session.get(
                    f"http://127.0.0.1:{server.server_address[1]}/redirect", timeout=3
                )
                response.raise_for_status()
                self.assertEqual(response.content, b"sound-fixture")
                self.assertEqual(len(response.history), 1)
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=3)
        self.assertFalse(thread.is_alive())

    def test_msgpack_engine_state_roundtrip(self):
        state = {"engine": "McLarenF1.wav", "pitch": 1.25, "playing": False}
        self.assertEqual(msgpack.unpackb(msgpack.packb(state), raw=False), state)

    def test_synthetic_pitch_processing(self):
        import librosa
        import numpy as np

        samples = np.zeros(22050, dtype=np.float32)
        shifted = librosa.effects.pitch_shift(samples, sr=22050, n_steps=1)
        self.assertEqual(shifted.shape, samples.shape)
        self.assertTrue(np.isfinite(shifted).all())


if __name__ == "__main__":
    unittest.main()
