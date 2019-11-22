def twitter_premium_as_df(clean_data_path):
    """something like '../../data/clean/' maybe? """
    def listdir_fullpath(d):
        """Function in a functions, whaaaa??!!?!"""
        return [os.path.join(d, f) for f in os.listdir(d)]
    
    clean_data = pathlib.Path(clean_data_path)
    pickles = os.listdir(clean_data)
    full_pickles = listdir_fullpath(clean_data)
    # But this function is doing too much!!
    # Boo hoo 
    return pd.concat([pd.read_pickle(fp) for fp in full_pickles], ignore_index=True)