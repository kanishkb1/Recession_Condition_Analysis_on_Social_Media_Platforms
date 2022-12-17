class SettingsTwitter:
    my_consumer_key = "O0ZgMWn3zv17ps3prBu8dzfkj"
    my_consumer_secret = "LENFwJF8dIP30xWkhhQH97vx13zAw886uEIGZhLC1hQKv8RWCm"

    my_access_token = "1445073787720962049-SQJwFHH379T8MrQpfrSeMpItJG98ms"
    my_access_secret = "nXXSLOCc6Wo2a0K60ITck7yf2ykSWeiGL4AMHJsvDQHD8"

    my_bearer_token = "AAAAAAAAAAAAAAAAAAAAAGKWiAEAAAAAOK9%2FyPL6DDNB1Sv4jVgMRP7%2F4UM%3DDZKp1GCjPLUuHEFChONTE4L6wuDzRcW64htS0uV2F8PJdu5Rdn"


creds_twitter = SettingsTwitter()


class SettingsSQL:
    username = "root"
    password = "admin123456"
    host = "localhost"
    port = 3306
    database = "dsp_tweets"


creds_sql = SettingsSQL()


class KeyWord:
    word = "rescission"


key_word = KeyWord()
