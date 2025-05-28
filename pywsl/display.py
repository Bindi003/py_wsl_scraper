# function for displaying each table but removes default DataFrame index from each
def display_table(df):
    print(df.to_string(index=False))