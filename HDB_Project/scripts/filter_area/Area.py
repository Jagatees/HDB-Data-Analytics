import pandas as pd


'''
    Description : Cleaning Area for missing area in data
'''
def area_cleaning():
  df1 = pd.read_csv('centralized/merger/csv_merged_final.csv')

  df1['Location_Name'] = df1['Location_Name'].str.upper()

  df1['LocationChange'] = df1['Location_Name']

  #HOUGANG
  df1['LocationChange'] = df1['LocationChange'].replace(['HOUGANG CENTRAL', 'HOUGANG MEADOW', 'HOUGANG MEADOWS'], 'HOUGANG')
  #YISHUN
  df1['LocationChange'] = df1['LocationChange'].replace(['YISHUN CENTRAL', 'YISHUN RING', 'YISHUN GREENWALK', 'YISHUN GARDENS', 'ADORA GREEN', 'KHATIB COURT', 'KHATIB GARDENS', 'YISHUN RIVERWALK'], 'YISHUN')
  #BEDOK
  df1['LocationChange'] = df1['LocationChange'].replace(['BEDOK CENTRAL', 'FENGSHAN COMMUNITY CLUB', 'FENGSHAN GREENVILLE' ,'BEDOK NORTH', 'BEDOK RESERVOIR', 'BEDOK RESERVOIR CRESCENT', 'BEDOK SOUTH', 'CHAI CHEE', 
                                                      'JALAN DAMAI', 'LENGKONG TIGA', 'NEW UPPER CHANGI', 'PING YI GREENS'], 'BEDOK')
  #BUKIT BATOK
  df1['LocationChange'] = df1['LocationChange'].replace(['BUKIT BATOK WEST', 'BUKIT BATOK EAST', 'BUKIT BATOK CENTRAL'], 'BUKIT BATOK')
  #WOODLANDS
  df1['LocationChange'] = df1['LocationChange'].replace(['ADMIRALTY', 'ADMIRALTY LINK', 'MARSILING', 'MARSILING DRIVE', 'MARSILING RISE', 'MARSILING LANE', 'MARSILING GREENVIEW', 'MARSILING EDGE', 'WOODLANDS CIRCLE', 'WOODLANDS CRESCENT', 'WOODLANDS RING', 'WOODLANDS RISE'], 'WOODLANDS')
  #GEYLANG
  df1['LocationChange'] = df1['LocationChange'].replace(['ALJUNIED', 'ALJUNIED CRESCENT', 'BALAM', 'CIRCUIT', 'EUNOS', 'EUNOS CRESCENT', 'GEYLANG BAHRU', 'GEYLANG SERAI', 'MACPHERSON RESIDENCY', 'SIMS', 'UPPER ALJUNIED LANE'], 'GEYLANG')
  #SENGKANG
  df1['LocationChange'] = df1['LocationChange'].replace(['ANCHORVALE', 'ANCHORVALE CRESCENT', 'ANCHORVALE HARVEST', 'ANCHORVALE LANE', 'ANCHORVALE LINK', 'ANCHORVALE PARKVIEW', 'BUANGKOK LINK', 'BUANGKOK CRESCENT', 'BUANGKOK GREEN',
                                                        'BUANGKOK EDGEVIEW', 'BUANGKOK PARKVISTA', 'BUANGKOK SQUARE', 'BUANGKOK TROPICA', 'COMPASSVALE', 'COMPASSVALE BOW', 'COMPASSVALE CRESCENT', 'COMPASSVALE LANE', 'COMPASSVALE LINK',
                                                          'COMPASSVALE MAST', 'COMPASSVALE WALK', 'FERNVALE', 'FERNVALE CREST', 'FERNVALE GARDENS', 'FERNVALE LANE', 'FERNVALE LEA', 'FERNVALE LINK', 'FERNVALE LODGE', 'FERNVALE RESIDENCE',
                                                          'FERNVALE RIDGE', 'FERNVALE RIVERGROVE', 'JALAN KAYU', 'RIVERVALE', 'RIVERVALE CRESCENT', 'RIVERVALE WALK', 'SENGKANG CENTRAL', 'SENGKANG EAST', 'SENGKANG EAST WAY',
                                                            'SENGKANG WAST', 'SENGKANG WEST WAY', 'SENGKANG WEST'], 'SENGKANG')

  df1['LocationChange'] = df1['LocationChange'].replace(['BISHAN GREEN', 'BISHAN VIEW'], 'BISHAN')
  #BUKIT MERAH
  df1['LocationChange'] = df1['LocationChange'].replace(['DEPOT','DEPOT HEIGHTS','BUKIT MERAH VIEW', 'BEO CRESCENT', 'BOON TIONG', 'BOON TIONG VILLE', 'BUKIT PURMEI', 'HENDERSON','HENDERSON CRESCENT', 'JALAN BUKIT HO SWEE', 'JALAN BUKIT MERAH', 'JALAN KLINIK',
                                                      'JALAN MEMB', 'JALAN MEMBINA', 'KIM CHENG', 'KIM TIAN', 'KIM TIAN GREEN', 'LENGKOK BAHRU', 'LIM LIAK', 'REDHILL', 'SILAT', 'SPOTTISWOODE PARK', 'TELOK BLANGAH', 'TELOK BLANGAH CRESCENT', 'TELOK BLANGAH HEIGHTS', 
                                                      'TELOK BLANGAH RISE', 'TELOK BLANGAH TOWERS', 'TELOK BLANGAH WAY', 'TIONG BAHRU ESTATE', 'TIONG BAHRU VIEW', 'TIONG POH'], 'BUKIT MERAH')
  #BUKIT PANJANG
  df1['LocationChange'] = df1['LocationChange'].replace(['BUKIT PANJANG RING' 'FAJAR', 'FAJAR HILLS', 'GANGSA', 'JELAPANG', 'JELEBU', 'LOMPANG', 'PEND', 'PENDING', 'PETIR', 'SAUJANA', 'SEGAR', 'SENJA', 'SENJA LINK', 'TECK WHYE LANE', 'FAJAR', 'BUKIT PANJANG RING'], 'BUKIT PANJANG')
  #CENTRAL
  df1['LocationChange'] = df1['LocationChange'].replace(['BEACH', 'CANTONMENT CLOSE', 'CANTONMENT', 'CANTONMENT TOWERS', 'HAVELOCK', 'NORTH BRIDGE', 'SMITH', 'TAMAN HO SWEE', 'TANGLIN', 'TANJONG PAGAR PLAZA', 'UPPER CROSS'], 'CENTRAL AREA')
  #KALLANG/WHAMPOA
  df1['LocationChange'] = df1['LocationChange'].replace(['BENDEMEER', 'LORONG LIMAU','BOON KENG', 'JALAN BAHAGIA', 'JALAN TENTERAM', 'KALLANG BAHRU', 'KELANTAN', 'KLANG LANE', 'MCNAIR', 'ROWELL', 'SA', "SAINT GEORGE'S LANE", 'TENTERAM PEAK', 'TESSENSOHN', 
                                                      'TOWNER HEIGHTS', 'UPPER BOON KENG', 'WHAMPOA', 'WHAMPOA VIEW', 'WHAMPOA WEST'], 'KALLANG/WHAMPOA')
  #JURONG WEST
  df1['LocationChange'] = df1['LocationChange'].replace(['BOON LAY PLACE', 'BOON LAY', 'BOON LAY MEADOW', 'BOON LAY VIEW', 'CORPORATION', 'CORPORATION TIARA', 'HO CHING', 'KANG CHING', 'TAH CHING', 'YUAN CHING', 'YUNG KUANG', 'YUNG LOH', 'YUNG KUANG', 'YUNG KUANG COURT'], 'JURONG WEST')
  #SEMBAWANG
  df1['LocationChange'] = df1['LocationChange'].replace(['CANBERRA', 'CANBERRA CRESCENT', 'CANBERRA LINK', 'CANBERRA WALK', 'MONTREAL', 'MONTREAL DALE', 'MONTREAL LINK', 'MONTREAL VALLE', 'SEMBAWANG CLOSE', 'SEMBAWANG CRESCENT', 'SEMBAWANG RIVERLODGE', 'SEMBAWANG VISTA',
                                                      'SPRING LODGE', 'WELLINGTON', 'WELLINGTON VIEW', 'MONTREAL VILLE'], 'SEMBAWANG')
  #CLEMENTI
  df1['LocationChange'] = df1['LocationChange'].replace(['CASA CLEMENTI', 'CLEMENTI WEST', 'CLEMENTI RIDGES', 'CLEMENTI GATEWAY', 'CLEMENTI LINK', 'GHIM MOH', 'GHIM MOH LINK', 'GHIM MOH EDGE', 'GHIM MOH VALLEY', 'TRIVELIS', 'WEST COAST', 'WEST COAST VISTA'], 'CLEMENTI')
  #TAMPINES
  df1['LocationChange'] = df1['LocationChange'].replace(['CENTRALE 8 AT TAMPINES', 'PARC LUMIERE', 'SIMEI', 'TAMPINES GREENEDGE', 'TAMPINES GREENTERRACE', 'TAMPINES GREENRIDGES', 'TAMPINES RIA'], 'TAMPINES')
  #ANG MO KIO
  df1['LocationChange'] = df1['LocationChange'].replace(['CHENG SAN COURT', 'KEBUN BARU COURT', 'TECK GHEE PARKVIEW', 'TECK GHEE VISTA'], 'ANG MO KIO')
  #CHOA CHU KANG
  df1['LocationChange'] = df1['LocationChange'].replace(['CHOA CHU KANG CENTRAL', 'CHOA CHU KANG CRESCENT', 'CHOA CHU KANG LOOP','CHOA CHU KANG NORTH 5', 'CHOA CHU KANG NORTH 6', 'JALAN TECK WHYE', 'KEAT HONG CLOSE', 'KEAT HONG CREST',
                                                        'KEAT HONG MIRAGE', 'LIMBANG GREEN'], 'CHOA CHU KANG')
  #QUEENSTOWN
  df1['LocationChange'] = df1['LocationChange'].replace(['CLARENCE LANE','DOVER', 'FORFAR HEIGHTS' ,'DOVER CRESCENT', 'DOVER VILLE', 'COMMONWEALTH', 'COMMONWEALTH 10', 'COMMONWEALTH CLOSE', 'COMMONWEALTH CRESCENT', 'DAWSON',
                                                      'HOLLAND', 'HOLLAND CLOSE', 'HOLLAND VISTA', 'HOY FATT', 'JALAN RUMAH T', 'JALAN RUMAH TINGGI', 'MEI LING', 'MEI LING VISTA', 'MEI LINK', "QUEEN'S CLOSE", 'QUEENSWAY', 
                                                      'STRATHMORE'], 'QUEENSTOWN')
  #PUNGGOL
  df1['LocationChange'] = df1['LocationChange'].replace(['CORALINUS', 'EDGEDALE', 'EDGEFIELD', 'MATILDA EDGE', 'PARKLAND RESIDENCES', 'PUNGGOL ARCADIA', 'PUNGGOL BAYVIEW', 'PUNGGOL BREEZE', 'PUNGGOL CENTRAL', 'PUNGGOL CREST', 'PUNGGOL EAST', 
                                                      'PUNGGOL EMERALD', 'PUNGGOL FIELD', 'PUNGGOL PLACE', 'PUNGGOL REGALIA', 'PUNGGOL RESIDENCES', 'PUNGGOL SAILS', 'PUNGGOL SATTHIRE', 'PUNGGOL SPECTRA', 'PUNGGOL SPREING', 'PUNGGOL VUE', 
                                                      'PUNGGOL WALK', 'PUNGGOL WAVES', 'PUNGGOL WAY', 'SUMANG LANE', 'SUMANG LINK', 'SUMANG WALK', 'WATERWAY SUNRAY', 'WATERWAY VIEW', 'PUNGGOL SPRING', 'PUNGGOL SAPPHIRE'], 'PUNGGOL')
  #PASIR RIS
  df1['LocationChange'] = df1['LocationChange'].replace(['COSTA RIS', 'ELIAS', 'PASIR RIS ONE'], 'PASIR RIS')
  #BUKIT TIMAH
  df1['LocationChange'] = df1['LocationChange'].replace(['FARRER PARK', 'FARRER GARDENS', 'FARRER PARK VIEW', 'TOH YI'], 'BUKIT TIMAH')
  #MARINE PARADE
  df1['LocationChange'] = df1['LocationChange'].replace(['HAIG', 'JALAN BATU', 'JALAN DUA', 'JALAN TIGA', 'JOO CHIAT', 'MAR', 'MARINE', 'MARINE CRESCENT', 'MARINE CRESCENT VILLE', 'MARINE TERRACE', 'OLD AIRPORT', 'P', 'PINE GREEN', 'PINE CLOSE'], 'MARINE PARADE')
  #TOA PAYOH
  df1['LocationChange'] = df1['LocationChange'].replace(['JALAN MAMOR', 'JALAN RAJAH', 'KIM KEAT', 'LORONG 1 TOA PAYOH', 'LORONG 2 TOA PAYOH', 'LORONG 3 TOA PAYOH', 'LORONG 4 TOA PAYOH', 'LORONG 5 TOA PAYOH',
                                                      'LORONG 6 TOA PAYOH', 'LORONG 7 TOA PAYOH', 'LORONG 8 TOA PAYOH', 'POTONG PASIR', 'TOA PAYOH APEX', 'TOA PAYOH CENTRAL', 'TOA PAYOH EAST', 'TOA PAYOH GREEN', 'TOA PAYOH NORTH', 'TOA PAYOH SAPPHIRE', 
                                                      'TOA PAYOH SPRING'], 'TOA PAYOH')
  #SERANGOON
  df1['LocationChange'] = df1['LocationChange'].replace(['JOO SENG', 'LORONG AH SOO', 'LORONG LEW LIAN', 'SERANGOON CENTRAL', 'SERANGOON NORTH', 'UPPER SERANGOON', 'UPPER SERANGOON VIEW', 'UPPER SERANGOON CRESCENT'], 'SERANGOON')
  #BISHAN
  df1['LocationChange'] = df1['LocationChange'].replace(['NATURA LOFT', 'S', 'SHUNFU', 'SHUNFU GARDENS', 'SIN MING'], 'BISHAN')
  #JURONG EAST
  df1['LocationChange'] = df1['LocationChange'].replace(['PANDAN GARDENS', 'TEBAN GARDENS', 'TEBAN VISTA', 'TOH GUAN'], 'JURONG EAST')


  df1.to_csv("centralized/merger/csv_merged_final.csv", index=False)

  print("Done")