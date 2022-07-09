# EasyTally: A Personal Accounting Bot

## How this works

- Create a channel.
- Add the bot. 
- Add your costs on a daily basis.
- Ask the bot to calculate your income and costs for a given period using a bot command

## Format: 
The format you need to specify your costs is `value تومان/ریال  برداشت/واریز`:   
An example:  
```
24000 تومان برداشت خرید میوه
۱۰۰۰۰۰۰ ریال واریز درآمد اسنپ
```

## Deploy To Kubernetes (Bot Login)
- Create a secret file with key=value pairs for api-id, api-hash, and bot-token (keys are important) and save it as temp/bot
- Create secret file with `kubectl create secrets bot-secret --from-env-file=temp/bot`
- Apply the secret file with `kubectl apply -f temp/bot-secret.yaml`
- Apply the bot.yaml file with `kubectl apply -f bot-deploy.yaml`

## Note: 
- Currently the bot only supports Persian.
- The bot supports Latin, Persian, and Eastern Arabic digits (0123456789,۰۱۲۳۴۵۶۷۸۹, ٠١٢٣٤٥٦٧٨٩)



## Deploy To Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)