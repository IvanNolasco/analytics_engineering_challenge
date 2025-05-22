def merge_data(users, transactions, deliveries):
    """
    Merges users data with transactions and deliveries to enrich each table
    with user information.

    This function performs:
    - A left join of `users` with `transactions` on `user_id`
    - A left join of `users` with `deliveries` on `user_id`

    This ensures that:
    - All users are retained (even those without transactions or deliveries)
    - Resulting tables are suitable for analytics and SQL queries

    Parameters:
        users (pd.DataFrame): Cleaned users DataFrame.
        transactions (pd.DataFrame): Cleaned transactions DataFrame.
        deliveries (pd.DataFrame): Cleaned deliveries DataFrame.

    Returns:
        tuple of pd.DataFrame:
            - transactions_merged: Transactions joined with user info
            - deliveries_merged: Deliveries joined with user info

    Example:
        tx_merged, dlv_merged = merge_data(users_df, transactions_df, deliveries_df)
    """
    transactions_merged = users.merge(transactions, on='user_id', how='left', suffixes=('', '_txn'))
    deliveries_merged = users.merge(deliveries, on='user_id', how='left', suffixes=('', '_dlv'))
    return transactions_merged, deliveries_merged
