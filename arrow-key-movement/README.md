# arrow-key-movement.py

A pretty simple script that enables movement in VRChat with arrow keys instead of WASD. Doesn't send movement if you're not focused on VRChat. Especially useful for lefties.

I'm not a lefty, but I talked to one and was like "dang I bet I could whip something up right quick" and I did.

License, attributions, and minimal documentation in source.

The only thing I could think of improving is finding a way to get foreground window that doesn't include the monstrosity that is `ctypes.windll`. Creating an exe using pyinstaller baloons this from ~4000 bytes to 6 million. wew
