{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "57735cfc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import re\n",
    "import os  # 👈 引入內建的作業系統模組\n",
    "\n",
    "# ================= 1. LINE 機器人設定區 =================\n",
    "# 改從雲端系統的環境變數（保險箱）讀取密鑰，確保安全\n",
    "LINE_TOKEN = os.environ.get(\"LINE_TOKEN\")\n",
    "USER_ID = os.environ.get(\"USER_ID\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
