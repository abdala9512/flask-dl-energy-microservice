# Energy generation and capacity forecasting

Energy generation and capacity forecast as Flask microservice.

## Model predictions

### Energy Generation
![LSTM prediction 1](notebooks/img/eg_lstm.PNG)

### Energy capacity
![LSTM prediction 2](notebooks/img/ec_lstm.PNG)


### Build Docker image

```
docker build -t lstm-api . 
```
#### Host

```
 docker run -d -p 6600:6600 --name lstm-api lstm-api
```

### Running on heroku

Deploy the API on Heroku

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Data
http://www.upme.gov.co/Reports/Default.aspx?ReportPath=/SIEL+UPME/Indicadores/Indicadores+Oferta&ViewMode=Detail


## Contact
You can contribute or send me an email to miguel.arquez12@gmail.com :)
