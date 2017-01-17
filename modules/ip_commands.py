"""
Obtain current local IP address.
"""
import platform
import socket
import subprocess


def run_command(cmd):
    """
    Execute this OS command and return the formated response.
    """
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return err if err else out.decode('UTF-8')


def get_ip():
    """
    Get the local IP.
    """
    if platform.system() == 'Linux':
        ip = run_command(['ip', 'route'])
    elif platform.system() == 'Windows':
        ip = run_command(['ipconfig'])
    else:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 0))
            ip = s.getsockname()[0]
        except:
            ip = '127.0.0.1'
        finally:
            s.close()
    return ip


whoami = socket.gethostname()

