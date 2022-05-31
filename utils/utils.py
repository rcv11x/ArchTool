import os
import socket as sock

class Utils:
    # Get current username
    username = os.getlogin()
    # Get hostname
    hostname = sock.gethostname()
    # Kernel release
    release  = os.uname()[2]
    # Promp Style
    promp_style = "archpent >> "


