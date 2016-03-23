/*
This script allows to insert data into postgresql table markets_marketblu
from a csv file (configured with ; as delimiter) on the server.

The csv file must only contain the necessary columns in it and never
take the auto-filled columns like id or datec which are auto-filled
during the insertion server-side.
*/

delete from markets_marketblu;  -- comment out to prevent table wipe !!!

copy markets_marketblu(
    -- gid autocompleted db side !
      category
    , title
    , corpus
    , price_flo
    , price_com
    , price_hon
    , price_fav
    , price_con
    , created_date
    , reputation
    )
from
  '/home/sighil/vsite/markets/assets/marketblu-data.csv' -- path to csv on the server
  WITH NULL AS '' -- empty csv cells will be considered as null
  DELIMITER AS ';' -- must match the csv configuration (either space or ;)
  csv -- tells that the input file is csv
  HEADER; -- to ignore the first row of the csv file, with column names