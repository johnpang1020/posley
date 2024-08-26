Setup Instructions

1. Ensure Database Schema is Up-to-Date
Before inserting data, make sure your database schema is up-to-date. Apply any pending migrations with the following command:

***
docker-compose exec web python manage.py migrate
***

2. Insert Sample Data
After applying migrations, insert sample data into your database. Use the Django shell to create instances of the Wallet and Transaction models:

Open the Django shell:

***
docker-compose exec web python manage.py shell
***

Insert sample data:

***
from wallet.models import Wallet, Transaction

# Create Wallet instances
wallet1 = Wallet.objects.create(
    address='0x1234567890abcdef1234567890abcdef12345678',
    usdc_balance=1000.00,
    usdt_balance=500.00,
    eth_balance=1.50
)

wallet2 = Wallet.objects.create(
    address='0xabcdef1234567890abcdef1234567890abcdef12',
    usdc_balance=2000.00,
    usdt_balance=1500.00,
    eth_balance=2.00
)

# Create Transaction instances
transaction1 = Transaction.objects.create(
    wallet=wallet1,
    currency='USDC',
    amount=100.00
)

transaction2 = Transaction.objects.create(
    wallet=wallet1,
    currency='ETH',
    amount=0.50
)

transaction3 = Transaction.objects.create(
    wallet=wallet2,
    currency='USDT',
    amount=200.00
)
***

3. Test API Endpoints
Once the data is inserted, you can test the following API endpoints:

Wallet Balance Endpoint

1:Purpose: Returns the current balance of USDC, USDT, and ETH for a specific wallet.

Endpoint:

GET http://localhost:8000/api/wallet/<wallet_id>/balance/

Wallet Transfer Volume Endpoint

2:Purpose: Summarizes the total transfer volume of USDC, USDT, and ETH for a specific wallet over the past 24 hours.

Endpoint:

GET http://localhost:8000/api/wallet/<wallet_id>/transfer-volume/


Notes
Replace <wallet_id> with the actual ID of the wallet you want to query.
Ensure Docker is running before executing these commands.