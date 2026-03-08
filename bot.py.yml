name: Quotex Bot v4

on:
  schedule:
    - cron: '* * * * *'  # كل دقيقة
  workflow_dispatch:      # تشغيل يدوي

jobs:
  run-bot:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install packages
        run: pip install python-telegram-bot ccxt pandas ta requests

      - name: Run Bot
        run: python bot.py
        env:
          TOKEN: ${{ secrets.TOKEN }}
          CHAT_ID: ${{ secrets.CHAT_ID }}
