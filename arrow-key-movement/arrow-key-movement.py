# Arrow Key Movement for VRChat
# Created by Tupper for someone who is a lefty
# and was tired of using WASD.

from pythonosc import udp_client
from typing import Optional
import keyboard

# Honestly ctypes is probably overkill and it baloons the size of the program when compiled
# but I can't find a better way to grab window names.
from ctypes import windll, create_unicode_buffer


def send_movement(input, client, val=1):
    if getForegroundWindowTitle() == "VRChat":
        client.send_message("/input/" + input, val)


# https://stackoverflow.com/a/58355052
def getForegroundWindowTitle() -> Optional[str]:
    hWnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hWnd)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hWnd, buf, length + 1)
    return buf.value if buf.value else None


if __name__ == "__main__":
    target_ip = "127.0.0.1"
    target_port = 9000
    client = udp_client.SimpleUDPClient(target_ip, target_port)
    print(
        "Press 'up', 'down', 'left', 'right' to move the player. Right Shift will run. Press Ctrl-C to exit this application."
    )

    while True:
        # Wait for the next event.
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == "left":
            send_movement("MoveLeft", client)
        elif event.event_type == keyboard.KEY_DOWN and event.name == "right":
            send_movement("MoveRight", client)
        elif event.event_type == keyboard.KEY_DOWN and event.name == "up":
            send_movement("MoveForward", client)
        elif event.event_type == keyboard.KEY_DOWN and event.name == "down":
            send_movement("MoveBackward", client)
        if event.event_type == keyboard.KEY_UP and event.name == "left":
            send_movement("MoveLeft", client, 0)
        elif event.event_type == keyboard.KEY_UP and event.name == "right":
            send_movement("MoveRight", client, 0)
        elif event.event_type == keyboard.KEY_UP and event.name == "up":
            send_movement("MoveForward", client, 0)
        elif event.event_type == keyboard.KEY_UP and event.name == "down":
            send_movement("MoveBackward", client, 0)
        if event.event_type == keyboard.KEY_DOWN and event.name == "right shift":
            send_movement("Run", client)
        elif event.event_type == keyboard.KEY_UP and event.name == "right shift":
            send_movement("Run", client, 0)

"""
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
"""
