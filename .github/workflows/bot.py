name: Quotex Bot v4

on:
  schedule:
    - cron: '* * * * *'
  workflow_dispatch:

jobs:
  run-bot:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Setup Python​​​​​​​​​​​​​​​​
