
# 📊 SQL Queries & Results

This document contains the SQL queries written to answer the analytical questions provided in the challenge, along with brief explanations and example results.

**Note:** The following answers are based solely on the sample datasets provided for this challenge. Results may vary if applied to a larger or updated production dataset.

---

## 1. How many users are there in total?

```sql
SELECT COUNT(DISTINCT user_id) AS total_users
FROM (
    SELECT user_id FROM user_transactions
    UNION
    SELECT user_id FROM user_deliveries
);
```

**Explanation:**  
This query counts all distinct users across both transaction and delivery records to ensure no user is missed.

**Answer:** `10,000 users`

---

## 2. How many users have transacted?

```sql
SELECT COUNT(DISTINCT user_id) AS users_with_transactions
FROM user_transactions
WHERE transaction_id IS NOT NULL;
```

**Explanation:**  
We count users that have at least one transaction by checking for non-null `transaction_id`.

**Answer:** `10,000 users`

---

## 3. What is the card delivery rate?

```sql
SELECT
    ROUND(
        COUNT(DISTINCT CASE WHEN delivery_status = 'Delivered' THEN user_id END) * 1.0
        / COUNT(DISTINCT user_id), 2
    ) AS card_delivery_rate
FROM user_deliveries;
```

**Explanation:**  
This calculates the percentage of users who have received at least one delivered package.

**Answer:** `25%`

---

## 4. Which is the most efficient package carrier?

```sql
SELECT courier,
       COUNT(CASE WHEN delivery_status = 'Delivered' THEN 1 END) * 1.0 / COUNT(*) AS delivery_success_rate
FROM user_deliveries
GROUP BY courier
ORDER BY delivery_success_rate DESC
LIMIT 1;
```

**Explanation:**  
Efficiency is defined here as the highest delivery success rate (ratio of delivered to total deliveries).

**Answer:** `FEDEX` with a delivery success rate of `25.17%`

---

## 5. Which are the top 10 categories with the most transactions?

```sql
SELECT transaction_type,
       COUNT(*) AS total_transactions
FROM user_transactions
WHERE transaction_id IS NOT NULL
GROUP BY transaction_type
ORDER BY total_transactions DESC
LIMIT 10;
```

**Explanation:**  
Assumes `transaction_type` represents a "category" such as `In-Store`, `Online`, or `Subscription`.

**Answer:**

| Transaction Type | Count |
|------------------|--------|
| In-Store         | 3,374  |
| Online           | 3,325  |
| Subscription     | 3,301  |


