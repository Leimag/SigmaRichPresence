from pypresence import Presence
import time

while True:
        rpc = Presence("893399167324528700")
        rpc.connect()
        rpc.update(state = "Jello!", large_image="sigma", large_text="Sigma 5.0!", start=time.time())

