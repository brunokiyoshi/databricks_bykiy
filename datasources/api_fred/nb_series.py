# Databricks notebook source
# DBTITLE 1,Definição do objeto série
class serie:
    def __init__(self, serie_id, frequency, aggregation_method, table_name, serie_description):
        self.serie_id = serie_id
        self.frequency = frequency
        self.aggregation_method = aggregation_method
        self.table_name = table_name
        self.serie_description = serie_description
        

# COMMAND ----------

# DBTITLE 1,Setagem das séries
series_list = []

# GDP
series_list.append(serie('CPMNACSCAB1GQEU272020', None, None, 'EU_GDP_QUARTERLY','EU GDP, quarterly'))

# Exchange rates
series_list.append(serie('AEXBZUS', None, None, 'EXCHANGE_RATE_BRL_USD_ANNUAL_AVG','BRL/USD exchange rate, annual average'))
series_list.append(serie('AEXJPUS', None, None, 'EXCHANGE_RATE_JPY_USD_ANNUAL_AVG','JPY/USD exchange rate, annual average'))
series_list.append(serie('AEXUSEU', None, None, 'EXCHANGE_RATE_USD_EUR_ANNUAL_AVG','USD/EUR exchange rate, annual average'))
series_list.append(serie('AEXUSUK', None, None, 'EXCHANGE_RATE_USD_GBP_ANNUAL_AVG','USD/GBP exchange rate, annual average'))
series_list.append(serie('EXBZUS', None, None, 'EXCHANGE_RATE_BRL_USD_MONTHLY_AVG','BRL/USD exchange rate, monthly average'))
series_list.append(serie('EXJPUS', None, None, 'EXCHANGE_RATE_JPY_USD_MONTHLY_AVG','JPY/USD exchange rate, monthly average'))
series_list.append(serie('EXUSEU', None, None, 'EXCHANGE_RATE_USD_EUR_MONTHLY_AVG','USD/EUR exchange rate, monthly average'))
series_list.append(serie('EXUSUK', None, None, 'EXCHANGE_RATE_USD_GBP_MONTHLY_AVG','USD/GBP exchange rate, monthly average'))
series_list.append(serie('DEXBZUS', None, None, 'EXCHANGE_RATE_BRL_USD_DAILY','BRL/USD exchange rate, daily'))
series_list.append(serie('DEXJPUS', None, None, 'EXCHANGE_RATE_JPY_USD_DAILY','JPY/USD exchange rate, daily'))
series_list.append(serie('DEXUSEU', None, None, 'EXCHANGE_RATE_USD_EUR_DAILY','USD/EUR exchange rate, daily'))
series_list.append(serie('DEXUSUK', None, None, 'EXCHANGE_RATE_USD_GBP_DAILY','USD/GBP exchange rate, daily')) 

# Interest rates

series_list.append(serie('DFEDTARU', None, None, 'FEDERAL_FUNDS_TARGET_RANGE_DAILY','Federal Funds Target Range, daily')) 
series_list.append(serie('DFEDTARU', 'm', 'avg', 'FEDERAL_FUNDS_TARGET_RANGE_MONTHLY_AVG','Federal Funds Target Range, monthly average')) 
series_list.append(serie('DFEDTARU', 'a', 'avg', 'FEDERAL_FUNDS_TARGET_RANGE_ANNUAL_AVG','Federal Funds Target Range, annual average')) 

series_list.append(serie('DGS10', None, None, 'TREASURY_NOTES_10Y_DAILY','10-year Treasury notes, daily')) 
series_list.append(serie('DGS10', 'm', 'avg', 'TREASURY_NOTES_10Y_MONTHLY_AVG','10-year Treasury notes, monthly average')) 
series_list.append(serie('DGS10', 'a', 'avg', 'TREASURY_NOTES_10Y_ANNUAL_AVG','10-year Treasury notes, annual average')) 

series_list.append(serie('RIFSPFFNB', None, None, 'FEDERAL_FUNDS_EFFECTIVE_RATE_DAILY','Federal Funds Effective Rate, daily')) 
series_list.append(serie('FEDFUNDS', 'm', 'avg', 'FEDERAL_FUNDS_EFFECTIVE_RATE_MONTHLY_AVG','Federal Funds Effective Rate, monthly average')) 
series_list.append(serie('FEDFUNDS', 'a', 'avg', 'FEDERAL_FUNDS_EFFECTIVE_RATE_ANNUAL_AVG','Federal Funds Effective Rate, annual average')) 

series_list.append(serie('IRLTLT01JPM156N', None, None, 'INTEREST_RATE_LP_JAPAN_MONTHLY','Long-term interest rate - Japan, monthly')) 
series_list.append(serie('IRLTLT01JPM156N', 'm', 'avg', 'INTEREST_RATE_LP_JAPAN_MONTHLY_AVG','Long-term interest rate - Japan, monthly average')) 
series_list.append(serie('IRLTLT01JPM156N', 'a', 'avg', 'INTEREST_RATE_LP_JAPAN_ANNUAL_AVG','Long-term interest rate - Japan, annual average')) 

# Price indices
series_list.append(serie('CPIAUCSL', None, None, 'CONSUMER_PRICE_INDEX_SEASONALLY_ADJUSTED','Consumer Price Index for All Urban Consumers: Seasonally Adjusted')) 
series_list.append(serie('CPIAUCNS', None, None, 'CONSUMER_PRICE_INDEX_NOT_SEASONALLY_ADJUSTED','Consumer Price Index for All Urban Consumers: Not Seasonally Adjusted')) 
series_list.append(serie('PPIFIS', None, None, 'PRODUCER_PRICE_INDEX_SEASONALLY_ADJUSTED','Producer Price Index by Commodity: Seasonally Adjusted')) 
series_list.append(serie('PPIACO', None, None, 'PRODUCER_PRICE_INDEX_NOT_SEASONALLY_ADJUSTED','Producer Price Index by Commodity: Not Seasonally Adjusted')) 
series_list.append(serie('CP0000EZ19M086NEST', None, None, 'HARMONIZED_INDEX_CONSUMER_PRICES','Harmonized Index of Consumer Prices'))
