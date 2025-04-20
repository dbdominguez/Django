import oracledb
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INSTANT_CLIENT_DIR = os.path.normpath(os.path.join(BASE_DIR, "..", "instantclient_23_7"))
WALLET_DIR = os.path.normpath(os.path.join(BASE_DIR, "..", "Wallet"))

oracledb.init_oracle_client(lib_dir=INSTANT_CLIENT_DIR)
os.environ["TNS_ADMIN"] = WALLET_DIR