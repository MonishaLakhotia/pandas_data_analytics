import joblib

joblib_file = "house_model.pkl"
# Load from file
model = joblib.load(joblib_file)

house_to_value = [
    1,  # Rooms
    20,  # Distance
    3,  # Bedroom2
    1,  # Bathroom
    0,  # Car
    534,  # Landsize
    220,  # BuildingArea
    1950,  # YearBuilt
    0,  # Suburb_Abbotsford
    0,  # Suburb_Aberfeldie
    0,  # Suburb_Airport West
    0,  # Suburb_Albanvale
    0,  # Suburb_Albert Park
    0,  # Suburb_Albion
    0,  # Suburb_Alphington
    1,  # Suburb_Altona
    0,  # Suburb_Altona Meadows
    0,  # Suburb_Altona North
    0,  # Suburb_Ardeer
    0,  # Suburb_Armadale
    0,  # Suburb_Ascot Vale
    0,  # Suburb_Ashburton
    0,  # Suburb_Ashwood
    0,  # Suburb_Aspendale
    0,  # Suburb_Aspendale Gardens
    0,  # Suburb_Attwood
    0,  # Suburb_Avondale Heights
    0,  # Suburb_Bacchus Marsh
    0,  # Suburb_Balaclava
    0,  # Suburb_Balwyn
    0,  # Suburb_Balwyn North
    0,  # Suburb_Bayswater
    0,  # Suburb_Bayswater North
    0,  # Suburb_Beaconsfield
    0,  # Suburb_Beaconsfield Upper
    0,  # Suburb_Beaumaris
    0,  # Suburb_Bellfield
    0,  # Suburb_Bentleigh
    0,  # Suburb_Bentleigh East
    0,  # Suburb_Berwick
    0,  # Suburb_Black Rock
    0,  # Suburb_Blackburn
    0,  # Suburb_Blackburn North
    0,  # Suburb_Blackburn South
    0,  # Suburb_Bonbeach
    0,  # Suburb_Boronia
    0,  # Suburb_Botanic Ridge
    0,  # Suburb_Box Hill
    0,  # Suburb_Braybrook
    0,  # Suburb_Briar Hill
    0,  # Suburb_Brighton
    0,  # Suburb_Brighton East
    0,  # Suburb_Broadmeadows
    0,  # Suburb_Brookfield
    0,  # Suburb_Brooklyn
    0,  # Suburb_Brunswick
    0,  # Suburb_Brunswick East
    0,  # Suburb_Brunswick West
    0,  # Suburb_Bulleen
    0,  # Suburb_Bullengarook
    0,  # Suburb_Bundoora
    0,  # Suburb_Burnley
    0,  # Suburb_Burnside
    0,  # Suburb_Burnside Heights
    0,  # Suburb_Burwood
    0,  # Suburb_Burwood East
    0,  # Suburb_Cairnlea
    0,  # Suburb_Camberwell
    0,  # Suburb_Campbellfield
    0,  # Suburb_Canterbury
    0,  # Suburb_Carlton
    0,  # Suburb_Carlton North
    0,  # Suburb_Carnegie
    0,  # Suburb_Caroline Springs
    0,  # Suburb_Carrum
    0,  # Suburb_Carrum Downs
    0,  # Suburb_Caulfield
    0,  # Suburb_Caulfield East
    0,  # Suburb_Caulfield North
    0,  # Suburb_Caulfield South
    0,  # Suburb_Chadstone
    0,  # Suburb_Chelsea
    0,  # Suburb_Chelsea Heights
    0,  # Suburb_Cheltenham
    0,  # Suburb_Chirnside Park
    0,  # Suburb_Clarinda
    0,  # Suburb_Clayton
    0,  # Suburb_Clayton South
    0,  # Suburb_Clifton Hill
    0,  # Suburb_Coburg
    0,  # Suburb_Coburg North
    0,  # Suburb_Collingwood
    0,  # Suburb_Coolaroo
    0,  # Suburb_Craigieburn
    0,  # Suburb_Cranbourne
    0,  # Suburb_Cranbourne North
    0,  # Suburb_Cremorne
    0,  # Suburb_Croydon
    0,  # Suburb_Croydon Hills
    0,  # Suburb_Croydon North
    0,  # Suburb_Croydon South
    0,  # Suburb_Dallas
    0,  # Suburb_Dandenong
    0,  # Suburb_Dandenong North
    0,  # Suburb_Deepdene
    0,  # Suburb_Deer Park
    0,  # Suburb_Delahey
    0,  # Suburb_Derrimut
    0,  # Suburb_Diamond Creek
    0,  # Suburb_Diggers Rest
    0,  # Suburb_Dingley Village
    0,  # Suburb_Doncaster
    0,  # Suburb_Doncaster East
    0,  # Suburb_Donvale
    0,  # Suburb_Doreen
    0,  # Suburb_Doveton
    0,  # Suburb_Eaglemont
    0,  # Suburb_East Melbourne
    0,  # Suburb_Edithvale
    0,  # Suburb_Elsternwick
    0,  # Suburb_Eltham
    0,  # Suburb_Eltham North
    0,  # Suburb_Elwood
    0,  # Suburb_Emerald
    0,  # Suburb_Endeavour Hills
    0,  # Suburb_Epping
    0,  # Suburb_Essendon
    0,  # Suburb_Essendon North
    0,  # Suburb_Essendon West
    0,  # Suburb_Fairfield
    0,  # Suburb_Fawkner
    0,  # Suburb_Ferntree Gully
    0,  # Suburb_Fitzroy
    0,  # Suburb_Fitzroy North
    0,  # Suburb_Flemington
    0,  # Suburb_Footscray
    0,  # Suburb_Forest Hill
    0,  # Suburb_Frankston
    0,  # Suburb_Frankston North
    0,  # Suburb_Frankston South
    0,  # Suburb_Gardenvale
    0,  # Suburb_Gisborne
    0,  # Suburb_Gisborne South
    0,  # Suburb_Gladstone Park
    0,  # Suburb_Glen Huntly
    0,  # Suburb_Glen Iris
    0,  # Suburb_Glen Waverley
    0,  # Suburb_Glenroy
    0,  # Suburb_Gowanbrae
    0,  # Suburb_Greensborough
    0,  # Suburb_Greenvale
    0,  # Suburb_Hadfield
    0,  # Suburb_Hallam
    0,  # Suburb_Hampton
    0,  # Suburb_Hampton East
    0,  # Suburb_Hampton Park
    0,  # Suburb_Hawthorn
    0,  # Suburb_Hawthorn East
    0,  # Suburb_Healesville
    0,  # Suburb_Heathmont
    0,  # Suburb_Heidelberg
    0,  # Suburb_Heidelberg Heights
    0,  # Suburb_Heidelberg West
    0,  # Suburb_Highett
    0,  # Suburb_Hillside
    0,  # Suburb_Hoppers Crossing
    0,  # Suburb_Hughesdale
    0,  # Suburb_Huntingdale
    0,  # Suburb_Hurstbridge
    0,  # Suburb_Ivanhoe
    0,  # Suburb_Ivanhoe East
    0,  # Suburb_Jacana
    0,  # Suburb_Kealba
    0,  # Suburb_Keilor
    0,  # Suburb_Keilor Downs
    0,  # Suburb_Keilor East
    0,  # Suburb_Keilor Lodge
    0,  # Suburb_Keilor Park
    0,  # Suburb_Kensington
    0,  # Suburb_Kew
    0,  # Suburb_Kew East
    0,  # Suburb_Keysborough
    0,  # Suburb_Kilsyth
    0,  # Suburb_Kings Park
    0,  # Suburb_Kingsbury
    0,  # Suburb_Kingsville
    0,  # Suburb_Knoxfield
    0,  # Suburb_Kooyong
    0,  # Suburb_Kurunjang
    0,  # Suburb_Lalor
    0,  # Suburb_Langwarrin
    0,  # Suburb_Lower Plenty
    0,  # Suburb_Lysterfield
    0,  # Suburb_Maidstone
    0,  # Suburb_Malvern
    0,  # Suburb_Malvern East
    0,  # Suburb_Maribyrnong
    0,  # Suburb_McKinnon
    0,  # Suburb_Meadow Heights
    0,  # Suburb_Melbourne
    0,  # Suburb_Melton
    0,  # Suburb_Melton South
    0,  # Suburb_Melton West
    0,  # Suburb_Mentone
    0,  # Suburb_Mernda
    0,  # Suburb_Mickleham
    0,  # Suburb_Middle Park
    0,  # Suburb_Mill Park
    0,  # Suburb_Mitcham
    0,  # Suburb_Mont Albert
    0,  # Suburb_Montmorency
    0,  # Suburb_Montrose
    0,  # Suburb_Moonee Ponds
    0,  # Suburb_Moorabbin
    0,  # Suburb_Mooroolbark
    0,  # Suburb_Mordialloc
    0,  # Suburb_Mount Evelyn
    0,  # Suburb_Mount Waverley
    0,  # Suburb_Mulgrave
    0,  # Suburb_Murrumbeena
    0,  # Suburb_Narre Warren
    0,  # Suburb_Newport
    0,  # Suburb_Niddrie
    0,  # Suburb_Noble Park
    0,  # Suburb_North Melbourne
    0,  # Suburb_North Warrandyte
    0,  # Suburb_Northcote
    0,  # Suburb_Notting Hill
    0,  # Suburb_Nunawading
    0,  # Suburb_Oak Park
    0,  # Suburb_Oakleigh
    0,  # Suburb_Oakleigh East
    0,  # Suburb_Oakleigh South
    0,  # Suburb_Officer
    0,  # Suburb_Ormond
    0,  # Suburb_Pakenham
    0,  # Suburb_Parkdale
    0,  # Suburb_Parkville
    0,  # Suburb_Pascoe Vale
    0,  # Suburb_Patterson Lakes
    0,  # Suburb_Plumpton
    0,  # Suburb_Point Cook
    0,  # Suburb_Port Melbourne
    0,  # Suburb_Prahran
    0,  # Suburb_Preston
    0,  # Suburb_Princes Hill
    0,  # Suburb_Research
    0,  # Suburb_Reservoir
    0,  # Suburb_Richmond
    0,  # Suburb_Riddells Creek
    0,  # Suburb_Ringwood
    0,  # Suburb_Ringwood East
    0,  # Suburb_Ringwood North
    0,  # Suburb_Ripponlea
    0,  # Suburb_Rosanna
    0,  # Suburb_Rowville
    0,  # Suburb_Roxburgh Park
    0,  # Suburb_Sandhurst
    0,  # Suburb_Sandringham
    0,  # Suburb_Scoresby
    0,  # Suburb_Seabrook
    0,  # Suburb_Seaford
    0,  # Suburb_Seaholme
    0,  # Suburb_Seddon
    0,  # Suburb_Skye
    0,  # Suburb_South Kingsville
    0,  # Suburb_South Melbourne
    0,  # Suburb_South Morang
    0,  # Suburb_South Yarra
    0,  # Suburb_Southbank
    0,  # Suburb_Spotswood
    0,  # Suburb_Springvale
    0,  # Suburb_Springvale South
    0,  # Suburb_St Albans
    0,  # Suburb_St Helena
    0,  # Suburb_St Kilda
    0,  # Suburb_Strathmore
    0,  # Suburb_Strathmore Heights
    0,  # Suburb_Sunbury
    0,  # Suburb_Sunshine
    0,  # Suburb_Sunshine North
    0,  # Suburb_Sunshine West
    0,  # Suburb_Surrey Hills
    0,  # Suburb_Sydenham
    0,  # Suburb_Tarneit
    0,  # Suburb_Taylors Hill
    0,  # Suburb_Taylors Lakes
    0,  # Suburb_Templestowe
    0,  # Suburb_Templestowe Lower
    0,  # Suburb_The Basin
    0,  # Suburb_Thomastown
    0,  # Suburb_Thornbury
    0,  # Suburb_Toorak
    0,  # Suburb_Travancore
    0,  # Suburb_Truganina
    0,  # Suburb_Tullamarine
    0,  # Suburb_Upwey
    0,  # Suburb_Vermont
    0,  # Suburb_Vermont South
    0,  # Suburb_Viewbank
    0,  # Suburb_Wallan
    0,  # Suburb_Wantirna
    0,  # Suburb_Wantirna South
    0,  # Suburb_Warrandyte
    0,  # Suburb_Waterways
    0,  # Suburb_Watsonia
    0,  # Suburb_Watsonia North
    0,  # Suburb_Wattle Glen
    0,  # Suburb_Werribee
    0,  # Suburb_West Footscray
    0,  # Suburb_West Melbourne
    0,  # Suburb_Westmeadows
    0,  # Suburb_Wheelers Hill
    0,  # Suburb_Whittlesea
    0,  # Suburb_Williams Landing
    0,  # Suburb_Williamstown
    0,  # Suburb_Williamstown North
    0,  # Suburb_Windsor
    0,  # Suburb_Wollert
    0,  # Suburb_Wyndham Vale
    0,  # Suburb_Yallambie
    0,  # Suburb_Yarra Glen
    0,  # Suburb_Yarraville
    0,  # CouncilArea_Banyule City Council
    0,  # CouncilArea_Bayside City Council
    0,  # CouncilArea_Boroondara City Council
    0,  # CouncilArea_Brimbank City Council
    0,  # CouncilArea_Cardinia Shire Council
    0,  # CouncilArea_Casey City Council
    0,  # CouncilArea_Darebin City Council
    0,  # CouncilArea_Frankston City Council
    0,  # CouncilArea_Glen Eira City Council
    0,  # CouncilArea_Greater Dandenong City Council
    1,  # CouncilArea_Hobsons Bay City Council
    0,  # CouncilArea_Hume City Council
    0,  # CouncilArea_Kingston City Council
    0,  # CouncilArea_Knox City Council
    0,  # CouncilArea_Macedon Ranges Shire Council
    0,  # CouncilArea_Manningham City Council
    0,  # CouncilArea_Maribyrnong City Council
    0,  # CouncilArea_Maroondah City Council
    0,  # CouncilArea_Melbourne City Council
    0,  # CouncilArea_Melton City Council
    0,  # CouncilArea_Mitchell Shire Council
    0,  # CouncilArea_Monash City Council
    0,  # CouncilArea_Moonee Valley City Council
    0,  # CouncilArea_Moorabool Shire Council
    0,  # CouncilArea_Moreland City Council
    0,  # CouncilArea_Nillumbik Shire Council
    0,  # CouncilArea_Port Phillip City Council
    0,  # CouncilArea_Stonnington City Council
    0,  # CouncilArea_Whitehorse City Council
    0,  # CouncilArea_Whittlesea City Council
    0,  # CouncilArea_Wyndham City Council
    0,  # CouncilArea_Yarra City Council
    0,  # CouncilArea_Yarra Ranges Shire Council
    1,  # Type_h
    0,  # Type_t
    0,  # Type_u
]

house_to_value = [house_to_value]

predicted_house_value = model.predict(house_to_value)

predicted_house_value = predicted_house_value[0]

# Print estimated value of the property to two decimal places

print("This property has an estimated value of AUD %.2f" %
      predicted_house_value)
