from telethon import TelegramClient
from telethon.sessions import StringSession
import time
import os, logging
from logging import basicConfig, getLogger, INFO
"""Dasha"""
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
 )
logging.basicConfig( format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)

StartTime = time.time()

SES = os.environ.get("SES")
URL = os.environ.get("URL")
OWNER_ID = os.environ.get("OWNER_ID")
AP_K = os.environ.get("AP_K")
AP_HS = os.environ.get("AP_HS")

ubot = TelegramClient(StringSession(SES), AP_K AP_HS)
tbot = TelegramClient(None, AP_K, AP_HS)
