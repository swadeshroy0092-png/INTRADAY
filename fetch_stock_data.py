import yfinance as yf
import pandas as pd
from datetime import datetime
import os

# --- Configuration ---

# 1. Your list of tickers
USER_TICKERS = [
"SCI", "SAMMAANCAP", "CREDITACC", "CHOLAHLDNG", "GRAVITA", "HINDALCO", 
"CHOLAFIN", "HINDCOPPER", "SCHNEIDER", "ELGIEQUIP", "INTELLECT", "SIGNATURE", 
"NATIONALUM", "SBFC", "GVT&D", "PNBHOUSING", "CHENNPETRO", "APTUS", 
"CUMMINSIND", "AADHARHFC", "THERMAX", "ECLERX", "VEDL", "CGCL", 
"CESC", "TATACOMM", "UTIAMC", "BLUESTARCO", "GPIL", "IEX", 
"COCHINSHIP", "BDL", "MOTILALOFS", "TATAINVEST", "ASAHIINDIA", "ADANIPOWER", 
"OBEROIRLTY", "KPITTECH", "FSL", "SAREGAMA", "VTL", "APLLTD", 
"HINDZINC", "HFCL", "TATAELXSI", "AARTIIND", "PRESTIGE", "ENGINERSIN", 
"AAVAS", "HAPPSTMNDS", "HONAUT", "IDEA", "PIIND", "AWL", 
"INDIAMART", "CROMPTON", "ICICIBANK", "HBLENGINE", "VMM", "FIRSTCRY", 
"PETRONET", "BHARTIARTL", "ACE", "GMRAIRPORT", "INOXWIND", "KEI", 
"SHRIRAMFIN", "ONGC", "GLAND", "NSLNISP", "BEL", "GRANULES", 
"SBICARD", "GODREJAGRO", "NESTLEIND", "ICICIGI", "CERA", "BEML", 
"APARINDS", "GUJGASLTD", "SARDAEN", "KFINTECH", "PVRINOX", "DEEPAKFERT", 
"POLICYBZR", "ZENTEC", "PTCIL", "INDUSTOWER", "DIVISLAB", "BASF", 
"LLOYDSME", "SUNDRMFAST", "GESHIP", "NTPCGREEN", "SWANCORP", "VGUARD", 
"CRISIL", "BSOFT", "GAIL", "ELECON", "NAVINFLUOR", "MAPMYINDIA", 
"GMDCLTD", "PFIZER", "VOLTAS", "COROMANDEL", "BERGEPAINT", "CAMPUS", 
"UNITDSPR", "MPHASIS", "JMFINANCIL", "RAILTEL", "SUNDARMFIN", "WELSPUNLIV", 
"ITC", "360ONE", "SCHAEFFLER", "ITCHOTELS", "OFSS", "SYRMA", 
"CONCOR", "BAYERCROP", "RAINBOW", "BHARTIHEXA", "NLCINDIA", "TIMKEN", 
"SUNPHARMA", "DOMS", "ITI", "BAJAJ-AUTO", "LINDEINDIA", "BIKAJI", 
"MGL", "COALINDIA", "TBOTEK", "JYOTHYLAB", "KALYANKJIL", "SIEMENS", 
"RAMCOCEM", "AMBER", "COFORGE", "IOC", "OIL", "IRB", 
"DRREDDY", "KIMS", "JWL", "FACT", "CAMS", "HSCL", 
"HONASA", "JSL", "ALKEM", "SKFINDIA", "RELIANCE", "APLAPOLLO", 
"SAGILITY", "ZENSARTECH", "SWIGGY", "MARICO", "GODREJPROP", "PREMIERENE", 
"RPOWER", "TATASTEEL", "FEDERALBNK", "TVSMOTOR", "GSPL", "RELINFRA", 
"CENTURYPLY", "ANGELONE", "HEG", "ASTRAZEN", "GRSE", "NBCC", 
"EIHOTEL", "PAYTM", "SAIL", "IKS", "JSWSTEEL", "HCLTECH", 
"UBL", "HAL", "LICHSGFIN", "BRIGADE", "IRCON", "SOBHA", 
"BATAINDIA", "MANYAVAR", "AJANTPHARM", "SRF", "ESCORTS", "ONESOURCE", 
"DATAPATTNS", "SUMICHEM", "BLUEDART", "SONACOMS", "SAILIFE", "KIRLOSENG", 
"BPCL", "TRENT", "ASIANPAINT", "ATGL", "EIDPARRY", "ABB", 
"BAJAJHFL", "AIAENG", "YESBANK", "NMDC", "IREDA", "NCC", 
"NAUKRI", "TATATECH", "M&MFIN", "CLEAN", "TRIVENI", "SYNGENE", 
"ARE&M", "SOLARINDS", "LTF", "POLYCAB", "ACMESOLAR", "PHOENIXLTD", 
"3MINDIA", "PGEL", "INOXINDIA", "TEJASNET", "MAHSEAMLES", "M&M", 
"IDBI", "HAVELLS", "POLYMED", "IRFC", "LEMONTREE", "TATAPOWER", 
"OLECTRA", "TARIL", "PRAJIND", "LODHA", "RVNL", "DCMSHRIRAM", 
"MAZDOCK", "KAYNES", "BRITANNIA", "DLF", "JPPOWER", "MMTC", 
"HOMEFIRST", "AFCONS", "PERSISTENT", "GODREJCP", "JSWENERGY", "ENRIN", 
"GRAPHITE", "ANANDRATHI", "FIVESTAR", "NIVABUPA", "IIFL", "ABREL", 
"SJVN", "INFY", "BANKBARODA", "TRIDENT", "PCBL", "VIJAYA", 
"POWERGRID", "BAJAJHLDNG", "UNOMINDA", "GLAXO", "LT", "INDHOTEL", 
"LTFOODS", "LATENTVIEW", "LUPIN", "EMAMILTD", "FINPIPE", "KEC", 
"INDIACEM", "TTML", "CANBK", "JINDALSTEL", "MINDACORP", "IPCALAB", 
"KIRLOSBROS", "SAPPHIRE", "TCS", "INDIGO", "ZYDUSLIFE", "RBLBANK", 
"SBILIFE", "WIPRO", "VENTIVE", "TORNTPOWER", "DEEPAKNTR", "REDINGTON", 
"MEDANTA", "ATUL", "FINCABLES", "BAJFINANCE", "PIDILITIND", "NUVAMA", 
"INDUSINDBK", "ACC", "RHIM", "NIACL", "MRPL", "RECLTD", 
"INDIANB", "BSE", "CASTROLIND", "ETERNAL", "SONATSOFTW", "METROPOLIS", 
"TMPV", "SHYAMMETL", "ABBOTINDIA", "HINDPETRO", "EXIDEIND", "RRKABEL", 
"KSB", "TATACONSUM", "EICHERMOT", "IRCTC", "GICRE", "JBMA", 
"TATACHEM", "NAVA", "PPLPHARMA", "ALKYLAMINE", "TECHM", "AKUMS", 
"PFC", "GODIGIT", "TITAGARH", "JBCHEPHARM", "GRASIM", "RCF", 
"DIXON", "CHOICEIN", "MANAPPURAM", "TORNTPHARM", "AUROPHARMA", "ABCAPITAL", 
"KAJARIACER", "LTTS", "ZFCVINDIA", "CDSL", "UPL", "NATCOPHARM", 
"AFFLE", "RITES", "MARUTI", "POONAWALLA", "HUDCO", "CYIENT", 
"PGHH", "BALKRISIND", "UNIONBANK", "VBL", "BAJAJFINSV", "NTPC", 
"BOSCHLTD", "INDGN", "HEXT", "SBIN", "ZEEL", "CANFINHOME", 
"NEWGEN", "ICICIPRULI", "ALOKINDS", "DABUR", "ADANIENSOL", "PAGEIND", 
"MANKIND", "BIOCON", "JUBLINGREA", "WELCORP", "DBREALTY", "ABLBL", 
"HEROMOTOCO", "IDFCFIRSTB", "BANDHANBNK", "SHREECEM", "TRITURBINE", "ASHOKLEY", 
"JUBLPHARMA", "GILLETTE", "CCL", "ERIS", "NETWEB", "MOTHERSON", 
"JIOFIN", "LTIM", "BLUEJET", "CENTRALBK", "FLUOROCHEM", "SUZLON", 
"LALPATHLAB", "MUTHOOTFIN", "CHALET", "PNB", "MAHABANK", "HDFCLIFE", 
"LAURUSLABS", "CARBORUNIV", "BHARATFORG", "LICI", "COHANCE", "NHPC", 
"STARHEALTH", "JYOTICNC", "AUBANK", "FORTIS", "HDFCAMC", "HYUNDAI", 
"TECHNOE", "BALRAMCHIN", "ADANIGREEN", "IFCI", "NYKAA", "WAAREEENER",
"CAPLIPOINT", "HDFCBANK", "BANKINDIA", "NEULANDLAB", "GODREJIND", "BHEL", 
"DMART", "MFSL", "MSUMI", "KPIL", "AXISBANK", "CGPOWER", 
"NH", "IOB", "AKZOINDIA", "BBTC", "JUBLFOOD", "MAHSCOOTER", 
"MRF", "CHAMBLFERT", "OLAELEC", "TITAN", "J&KBANK", "KOTAKBANK", 
"DALBHARAT", "TIINDIA", "GLENMARK", "GODFRYPHLP", "KARURVYSYA", "THELEELA", 
"IGL", "ADANIENT", "JSWINFRA", "DELHIVERY", "JKCEMENT", "NAM-INDIA", 
"SUNTV", "APOLLOHOSP", "ANANTRAJ", "AMBUJACEM", "ENDURANCE", "UCOBANK", 
"ADANIPORTS", "ABFRL", "POWERINDIA", "RKFORGE", "AEGISLOG", "AIIL", 
"ASTRAL", "ULTRACEMCO", "RADICO", "NUVOCO", "EMCURE", "DEVYANI", 
"WOCKPHARMA", "COLPAL", "ASTERDM", "WHIRLPOOL", "FORCEMOT", "JKTYRE", 
"USHAMART", "CRAFTSMAN", "MAXHEALTH", "PATANJALI", "BLS", "ABSLAMC", 
"IGIL", "APOLLOTYRE", "CONCORDBIO", "CUB", "MCX", "HINDUNILVR", 
"AEGISVOPAK", "SUPREMEIND"
]

# 2. Add ".NS" suffix for NSE tickers
TICKERS_NS = [t + ".NS" for t in USER_TICKERS]

# 3. The data points you want (based on your SBIN example)
# We will use .get() to avoid errors if a key doesn't exist for a ticker
KEYS_TO_EXTRACT = [
    'longName', 'industry', 'sector', 'fullExchangeName', 'website', 
    'city', 'zip', 'marketCap', 'regularMarketTime', 'currentPrice', 'open', 
    'dayHigh', 'dayLow', 'volume', 'previousClose', 'regularMarketChange', 
    'regularMarketChangePercent', 'fiftyTwoWeekLow', 'fiftyTwoWeekHigh', 'allTimeHigh', 'allTimeLow', 
    'fiftyDayAverage', 'fiftyDayAverageChange', 'fiftyDayAverageChangePercent', 'twoHundredDayAverage', 'twoHundredDayAverageChange', 'twoHundredDayAverageChangePercent', 'fiftyTwoWeekLowChange', 'fiftyTwoWeekLowChangePercent', 'fiftyTwoWeekHighChange', 'fiftyTwoWeekHighChangePercent', 'fiftyTwoWeekRange', 'averageVolume', 'averageDailyVolume10Day', 'averageDailyVolume3Month', 'floatShares', 'impliedSharesOutstanding', 
    'sharesOutstanding', 'heldPercentInsiders', 'heldPercentInstitutions',
    'totalCash', 'totalCashPerShare', 'totalDebt', 'totalRevenue', 'revenuePerShare', 'returnOnAssets', 'returnOnEquity', 'grossProfits', 'earningsGrowth', 'revenueGrowth', 'grossMargins', 'ebitdaMargins', 'operatingMargins', 'profitMargins',
    'bookValue', 'priceToBook', 'enterpriseValue', 'trailingPE', 'forwardPE', 'trailingEps', 'forwardEps',  'dividendRate', 
    'dividendYield', 'exDividendDate', 'payoutRatio', 'fiveYearAvgDividendYield', 'lastSplitFactor', 'enterpriseToRevenue', 'netIncomeToCommon', 'lastSplitDate', 'beta'
]

OUTPUT_CSV = "stock_snapshot_data.csv"
# ---------------------

def fetch_snapshot_data():
    all_stock_data = []
    # Get a single timestamp for this entire batch of data
    fetch_timestamp = datetime.now().isoformat()
    
    print(f"Starting data fetch for {len(TICKERS_NS)} tickers...")

    for ticker_symbol in TICKERS_NS:
        try:
            print(f"Fetching: {ticker_symbol}")
            ticker_obj = yf.Ticker(ticker_symbol)
            info = ticker_obj.info

            # Build a dictionary for this one ticker
            stock_data = {key: info.get(key, None) for key in KEYS_TO_EXTRACT}
            
            # Add our own custom fields
            stock_data['ticker'] = ticker_symbol # Add the ticker symbol itself
            stock_data['fetchTimestamp'] = fetch_timestamp # Add our timestamp

            all_stock_data.append(stock_data)

        except Exception as e:
            # This will catch errors for invalid tickers (like ETERNAL.NS, TMPV.NS)
            # The script will print the error and continue with the next ticker
            print(f"--- FAILED to fetch data for {ticker_symbol}. Error: {e}")
            continue
    
    if not all_stock_data:
        print("No data was fetched. Exiting.")
        return

    print("Data fetch complete. Converting to DataFrame...")
    
    # Convert our list of dictionaries into a pandas DataFrame
    df = pd.DataFrame(all_stock_data)
    
    # Re-order columns to put 'ticker' and 'fetchTimestamp' first
    cols = ['fetchTimestamp', 'ticker'] + [col for col in df.columns if col not in ['fetchTimestamp', 'ticker']]
    df = df[cols]

    # Check if the file already exists
    file_exists = os.path.exists(OUTPUT_CSV)
    
    if file_exists:
        print(f"Appending data to existing {OUTPUT_CSV}")
        # Append to the CSV without writing the header
        df.to_csv(OUTPUT_CSV, mode='a', header=False, index=False)
    else:
        print(f"Creating new file: {OUTPUT_CSV}")
        # Create the file and write the header
        df.to_csv(OUTPUT_CSV, mode='w', header=True, index=False)
        
    print(f"Script finished. Added {len(df)} rows to {OUTPUT_CSV}.")

if __name__ == "__main__":

    fetch_snapshot_data()

