import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/fernando/AdR/p3_ws/src/install/p3_ekf_adr'
