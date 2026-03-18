import yfinance as yf
import pandas as pd
from datetime import datetime
import os

# --- Configuration ---

# 1. Your list of tickers
USER_TICKERS = [
  "EASEMYTRIP", "ALLCARGO", "RTNPOWER", "PCJEWELLER", "IDEA", "ALOKINDS", 
  "CCAVENUE", "JPPOWER", "HCC", "YESBANK", "JINDWORLD", "RPOWER", "RENUKA", 
  "TRIDENT", "OLAELEC", "PATELENG", "UCOBANK", "RTNINDIA", "NETWORK18", 
  "JISLJALEQS", "IOB", "CENTRALBK", "SOUTHBANK", "NSLNISP", "MSUMI", 
  "SAGILITY", "TTML", "IMAGICAA", "IRB", "SUZLON", "LLOYDSENGG", "LLOYDSENT", 
  "EMBDL", "GATEWAY", "UJJIVANSFB", "IFCI", "EQUITASBNK", "ABFRL", "RBA", 
  "WEBELSOLAR", "MMTC", "JAIBALAJI", "MAHABANK", "IDFCFIRSTB", "SJVN", 
  "NFL", "NIVABUPA", "HFCL", "ELECTCAST", "IDBI", "ZEEL", "NHPC", "RELINFRA", 
  "NMDC", "INOXWIND", "BAJAJHFL", "NBCC", "SBFC", "GMRAIRPORT", "TEXRAIL", 
  "MANINFRA", "EMIL", "THOMASCOOK", "IRFC", "NTPCGREEN", "ABLBL", "DBREALTY", 
  "GMRP&UI", "TVSSCS", "LEMONTREE", "VMM", "DEVYANI", "EDELWEISS", "PARKHOTELS", 
  "PNB", "WELSPUNLIV", "RAIN", "PARADEEP", "MOTHERSON", "ASHOKA", "IREDA", 
  "JSWCEMENT", "SPARC", "RCF", "KNRCON", "IEX", "JAMNAAUTO", "J&KBANK", 
  "LXCHEM", "PRSMJOHNSN", "TARC", "JMFINANCIL", "SHAREINDIA", "IRCON", 
  "DIACABS", "NIACL", "GAEL", "CANBK", "GREAVESCOT", "HEMIPROP", "ORIENTCEM", 
  "SAMMAANCAP", "PPLPHARMA", "INOXGREEN", "NCC", "IOC", "GAIL", "SAMHI", 
  "BANKINDIA", "EIEL", "SAIL", "GPPL", "ADANIPOWER", "CESC", "IGL", 
  "ITCHOTELS", "GSFC", "BANDHANBNK", "PTC", "TIMETECHNO", "KITEX", "IXIGO", 
  "MARKSANS", "DCAL", "CGCL", "SAPPHIRE", "HIKAL", "KANSAINER", "SWSOLAR", 
  "AWL", "FINPIPE", "UNIONBANK", "ASHOKLEY", "DCBBANK", "HUDCO", "QUESS", 
  "BELRISE", "CASTROLIND", "SANDUMA", "PURVA", "BECTORFOOD", "AEGISVOPAK", 
  "MRPL", "PNCINFRA", "STLTECH", "WIPRO", "ENGINERSIN", "TATASTEEL", "VIYASH", 
  "EPL", "GREENPANEL", "RITES", "JINDALSAW", "REFEX", "STARCEMENT", "SURYAROSNI", 
  "FIRSTCRY", "JYOTHYLAB", "VAIBHAVGBL", "APTUS", "SUNFLAG", "ZAGGLE", 
  "VSTIND", "RELIGARE", "FSL", "CAMPUS", "REDINGTON", "KTKBANK", "ANGELONE", 
  "SCI", "ICIL", "SONATSOFTW", "NYKAA", "ETERNAL", "RALLIS", "BLS", 
  "ACMESOLAR", "PRINCEPIPE", "JIOFIN", "CROMPTON", "CUB", "NAZARA", "PCBL", 
  "GSPL", "BHEL", "GPIL", "JSWINFRA", "NLCINDIA", "ITI", "ONGC", "JWL", 
  "LTF", "MANAPPURAM", "FEDERALBNK", "AWFIS", "RVNL", "CEIGALL", "HONASA", 
  "ADVENZYMES", "RAILTEL", "BANKBARODA", "LATENTVIEW", "KARURVYSYA", "IIFLCAPS", 
  "RELAXO", "TARIL", "AFCONS", "CMSINFO", "PETRONET", "KRBL", "MOIL", 
  "POWERGRID", "SWIGGY", "RBLBANK", "ITC", "BPCL", "SENCO", "NUVOCO", 
  "COHANCE", "PRAJIND", "EXIDEIND", "OSWALPUMPS", "M&MFIN", "HERITGFOOD", 
  "MIDHANI", "CYIENTDLM", "EIHOTEL", "SUNTECK", "TMPV", "SHILPAMED", 
  "ABCAPITAL", "GODIGIT", "VGUARD", "JKPAPER", "VIPIND", "TRIVENI", "IGIL", 
  "FDC", "AARTIDRUGS", "IONEXCHANG", "SWANCORP", "BAJAJELEC", "RECLTD", 
  "HINDPETRO", "OPTIEMUS", "SAREGAMA", "MAHLIFE", "SKYGOLD", "SKIPPER", 
  "JSFB", "GUJGASLTD", "MANYAVAR", "BSOFT", "ARVIND", "GICRE", "INDIACEM", 
  "THYROCARE", "TSFINV", "MAXESTATES", "KOTAKBANK", "FIVESTAR", "NTPC", 
  "BLUEJET", "RHIM", "BIOCON", "HAPPSTMNDS", "KPIGREEN", "NATIONALUM", 
  "SUMICHEM", "CSBBANK", "KALYANKJIL", "LTFOODS", "ELECON", "TATAPOWER", 
  "CELLO", "ARVINDFASN", "POONAWALLA", "THELEELA", "EMUDHRA", "USHAMART", 
  "EMAMILTD", "BERGEPAINT", "VBL", "SYNGENE", "ASKAUTOLTD", "GNFC", 
  "APOLLOTYRE", "ABDL", "DELHIVERY", "MSTCLTD", "ZYDUSWELL", "TANLA", 
  "PFC", "AGARWALEYE", "AARTIIND", "HEXT", "BORORENEW", "JKTYRE", "WESTLIFE", 
  "DBL", "INDUSTOWER", "CHAMBLFERT", "AMBUJACEM", "BEL", "TEJASNET", 
  "DABUR", "INDGN", "TI", "HSCL", "GHCL", "EUREKAFORB", "COALINDIA", 
  "NEWGEN", "BALUFORGE", "CONCOR", "STARHEALTH", "WELENT", "OIL", "ANANTRAJ", 
  "AADHARHFC", "JUBLFOOD", "BALRAMCHIN", "TRITURBINE", "CIEINDIA", "ROUTE", 
  "AKUMS", "AIIL", "ELGIEQUIP", "VESUVIUS", "IIFL", "HINDCOPPER", "PATANJALI", 
  "AJAXENGG", "HGINFRA", "LICHSGFIN", "MINDACORP", "JSWENERGY", "HEG", 
  "SONACOMS", "JKIL", "SHAKTIPUMP", "RATEGAIN", "ATGL", "TRANSRAILL", 
  "VARROC", "AGI", "SARDAEN", "VMART", "TIPSMUSIC", "JUSTDIAL", "RKFORGE", 
  "SFL", "PGEL", "HINDZINC", "ORCHPHARMA", "IRCTC", "VTL", "TATATECH", 
  "PRICOLLTD", "CEMPRO", "GALLANTT", "DLF", "GMDCLTD", "PNGJL", "NAVA", 
  "HCG", "MAHSEAMLES", "KEC", "ACI", "BANCOINDIA", "JUBLINGREA", "ZENSARTECH", 
  "ICICIPRULI", "GRANULES", "GODREJAGRO", "JBMA", "SUPRIYA", "GOKEX", 
  "BLACKBUCK", "SUNTV", "AEGISLOG", "JKLAKSHMI", "BIKAJI", "GANESHHOU", 
  "GRAPHITE", "GARFIBRES", "TATAINVEST", "UPL", "INDHOTEL", "HDFCLIFE", 
  "CHOICEIN", "TITAGARH", "TATACHEM", "AARTIPHARM", "PARAS", "CAMS", 
  "ASTERDM", "INTELLECT", "BATAINDIA", "KIMS", "YATHARTH", "APLLTD", 
  "VENTIVE", "VEDL", "CENTURYPLY", "HBLENGINE", "KSL", "KPITTECH", "BRIGADE", 
  "SUBROS", "MOTILALOFS", "CGPOWER", "SBICARD", "INNOVACAP", "DATAMATICS", 
  "CLEAN", "JSL", "INDIASHLTR", "AHLUCONT", "ATHERENERG", "CHALET", "MARICO", 
  "JYOTICNC", "INDIGOPNTS", "CARBORUNIV", "KSCL", "UNIMECH", "SYRMA", 
  "ARE&M", "LICI", "SHYAMMETL", "PNBHOUSING", "SIGNATURE", "KSB", "FACT", 
  "SUNDRMFAST", "SUDARSCHEM", "SYMPHONY", "EIDPARRY", "SHARDAMOTR", 
  "WELCORP", "GODREJIND", "AURIONPRO", "TDPOWERSYS", "KPRMILL", "GANECOS", 
  "INDUSINDBK", "HDFCBANK", "RAYMONDLSL", "WHIRLPOOL", "MEDPLUS", 
  "BIRLACORPN", "FORTIS", "ACE", "CANFINHOME", "JUBLPHARMA", "EPIGRAL", 
  "LODHA", "ASAHIINDIA", "WAAREERTL", "CYIENT", "PREMIERENE", "GMMPFAUDLR", 
  "GABRIEL", "INDIAGLYCO", "MAPMYINDIA", "FINCABLES", "NAM-INDIA", 
  "BAJFINANCE", "POLYPLEX", "KRN", "ADANIGREEN", "INDIANB", "ZYDUSLIFE", 
  "SCHNEIDER", "STAR", "ISGEC", "LUXIND", "GRINFRA", "HINDALCO", "AUBANK", 
  "ALIVUS", "AVALON", "VIJAYA", "DEEPAKFERT", "ASTRAMICRO", "KFINTECH", 
  "KAJARIACER", "NATCOPHARM", "GULFOILLUB", "ABSLAMC", "UTIAMC", "MAXHEALTH", 
  "RAMCOCEM", "HOMEFIRST", "LAURUSLABS", "NAUKRI", "DHANUKA", "MGL", 
  "SAILIFE", "SHARDACROP", "CHENNPETRO", "SHRIRAMFIN", "PVRINOX", "IFBIND", 
  "ADANIENSOL", "OLECTRA", "MEDANTA", "GODREJCP", "CCL"
]

# 2. Add ".NS" suffix for NSE tickers
TICKERS_NS = [t + ".NS" for t in USER_TICKERS]

# 3. The data points you want
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
            # This will catch errors for invalid tickers (like SWIGGY.NS, FIRSTCRY.NS)
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

    # --- THIS IS THE CORRECTED SECTION ---
    print(f"Saving {len(df)} rows to {OUTPUT_CSV} (overwriting file)...")
    
    # Use mode='w' to ALWAYS overwrite the file with the new data.
    # header=True ensures the column names are written every time.
    df.to_csv(OUTPUT_CSV, mode='w', header=True, index=False)
        
    print(f"Script finished. Data saved to {OUTPUT_CSV}.")

if __name__ == "__main__":
    fetch_snapshot_data()
