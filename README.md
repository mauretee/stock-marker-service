# stock-marker-service

A Stock Market API Service

# Run the local environment backend
run `docker-compose up -d`

# Usage of endpoint


## POST
`Create user and key` [/api/users/] <br/>

**Parameters**

|          Name | Required |  Type   | Description                                                                                                                                                           |
| -------------:|:--------:|:-------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     `email` | required | string  | the email of the user.                                                                     |
|     `first_name` | required | string  | the first name of the user.                                                                     |
|     `last_name` | required | string  | the last name of the user.                                                                     |


**Response**

```
{
    "email": "mauro.lopez@gmail.com",
    "first_name": "mauro",
    "last_name": "lopez",
    "key": "XTHy2RJd.3zUJhqLqbQKYlbcSX232i3PM3yeOfqvX"
}
```


## GET
`get stock market info` [/api/stock/symbol] <br/>
Set the authorization header to `Api-Key: <key>` with the key returned from `/api/users`

#### Examples

| Endpoint             | Description                              |
| -------------------- | ---------------------------------------- |
| `/api/market/FB`         | Get market info of facebook.  |


**Response**

```
{
    "user": "mauro@gmail.com",
    "data": {
        "Meta Data": {
            "1. Information": "Daily Prices (open, high, low, close) and Volumes",
            "2. Symbol": "MSFT",
            "3. Last Refreshed": "2021-11-12",
            "4. Output Size": "Compact",
            "5. Time Zone": "US/Eastern"
        },
        "Time Series (Daily)": {
            "2021-11-12": {
                "1. open": "333.9200",
                "2. high": "337.2300",
                "3. low": "333.7900",
                "4. close": "336.7200",
                "5. volume": "23484434"
            },
            "2021-11-11": {
                "1. open": "331.2500",
                "2. high": "333.7746",
                "3. low": "330.5100",
                "4. close": "332.4300",
                "5. volume": "16849844"
            }
        }
    }
}
```

# Throttling
The throttling limit for the get stock market info endpoint are:

| Time             | Call count                              |
| -------------------- | ---------------------------------------- |
| 1 second         | 1  |
| 1 minute         | 10  |
| 1 hour         | 100  |
| 1 day         | 1000  |


# Logging
The logging file to see all api call are in the file `/tmp/api.log`
