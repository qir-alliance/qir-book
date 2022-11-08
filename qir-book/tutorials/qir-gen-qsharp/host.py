import qsharp
from Teleportation import TeleportClassicalMessage

to_send_binary = "010010000110010101101100011011000110111100100000011101110110111101110010011011000110010000100001"
to_send_list_bool = [bool(int(x)) for x in to_send_binary]
teleported=[]
for bit in to_send_list_bool:
   transferred = TeleportClassicalMessage.simulate(message = bit)
   teleported.append(transferred)
teleported_int = [int(x) for x in teleported]
teleported_str = ''.join(str(x) for x in teleported_int)
teleported_base2= int(teleported_str, 2)
teleported_base2_chunks= (teleported_base2.bit_length() +7) // 8
teleported_bytes = teleported_base2.to_bytes(teleported_base2_chunks, "big")
received =teleported_bytes.decode(encoding='utf-8')
print(received)