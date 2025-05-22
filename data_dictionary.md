
# 📘 Data Dictionary

This document describes the structure and key characteristics of the three datasets used in the challenge: **Users**, **Transactions**, and **Deliveries**. It also includes key definitions for data relationships.

---

## 🧑 user_info

| Column    | Type   | Description                | Example                              | Key     | Comments                                                                 |
|-----------|--------|----------------------------|--------------------------------------|---------|--------------------------------------------------------------------------|
| user_id   | string | Unique identifier for user | 1d10b266-b7b2-4258-88b3-3957de0461ea | PK      |                                                                          |
| name      | string | Full name of the user      | Angela Smith                         |         |                                                                          |
| email     | string | User's email address       | nfischer@yahoo.com                   |         |                                                                          |
| join_date | string | User registration date     | 02/06/2023                           |         | Mixed formats: `MM/DD/YYYY`, `YYYY-MM-DD`, etc.                         |

---

## 💳 transaction_info

| Column           | Type   | Description                          | Example                             | Key               | Comments                                                                 |
|------------------|--------|--------------------------------------|-------------------------------------|-------------------|--------------------------------------------------------------------------|
| transaction_id   | string | Unique transaction identifier        | 8b266b46-9ec7-4010-83e4-004b3bef400f | PK                |                                                                          |
| user_id          | string | Foreign key referencing Users        | 1d10b266-b7b2-4258-88b3-3957de0461ea | FK → Users.user_id |                                                                          |
| amount           | float  | Transaction amount                   | 865.48                              |                   | Round to 2 decimal places.                                               |
| timestamp        | string | Datetime of transaction              | 11/22/2023 01:09 AM                 |                   | Mixed formats: AM/PM, dot-separated, 24h.                                |
| transaction_type | string | Type of transaction                  | In-Store                            |                   | Possible values: `In-Store`, `Subscription`, `Online`.                  |

---

## 📦 package_delivery_info

| Column          | Type   | Description                          | Example                              | Key               | Comments                                                                 |
|-----------------|--------|--------------------------------------|--------------------------------------|-------------------|--------------------------------------------------------------------------|
| package_id      | string | Unique package identifier            | 80c09506-8a61-454a-a226-22e639d8795b | PK                |                                                                          |
| courier         | string | Delivery service provider            | DHL                                  |                   | Possible values: `DHL`, `ups`, `UPS`, `FEDEX`, `DHL   `. Normalize casing and trim whitespace. |
| delivery_date   | string | Date of delivery                     | 09-12-2022                           |                   | Mixed formats: `DD-MM-YYYY`, `MM/DD/YYYY`, `YYYY.MM.DD`.                |
| delivery_status | string | Status of package delivery           | Delivered                            |                   | Possible values: `Delivered`, `In Transit`, `Pending`, `Lost`.          |
| user_id         | string | Foreign key referencing Users        | 1d10b266-b7b2-4258-88b3-3957de0461ea | FK → Users.user_id |                                                                          |
