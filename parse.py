import gzip
import leveldb

def adr():
  count = 0
  db = leveldb.LevelDB("address.leveldb", error_if_exists=True)
  for address in gzip.open("AddressAccess.csv.gz"):
    address = filter(lambda x: ord(x) < 128 and x != '"', address).split(";")
    road = address[5]
    nr = address[6]
    postnr = address[8]
    lat = address[19]
    lng = address[20]
    address = "%s %s %s" % (postnr, road, nr)
    loc = "%s %s" % (lat, lng)
    db.Put(address, loc)
    count = count + 1
    if count % 10000 == 0:
      print count

def comp():
  db = leveldb.LevelDB("address.leveldb")
  for company in gzip.open("TOTAL_NYESTE.csv.gz"):
    company = company.split(";")
    """
    for i in range(0, len(company)):
      print i, company[i]
      """
    name = company[4]
    legalunit = company[1]
    productionUnit = company[2]
    startDate = company[7]
    activityCode = company[38]
    activityDesc = company[39]
    companyType = company[47]
    nr = company[12]
    road = filter(lambda x: ord(x) < 128,company[13])
    postnr = company[17]
    try:
      coord = db.Get("%s %s %s" % (postnr, road, nr))
      print startDate, activityCode, coord, name
    except:
      pass
    """
    if productionUnit != "0":
      print name, postnr, road, nr, startDate, activityDesc, companyType
      try:
        print db.Get("%s %s %s" % (postnr, road, nr))
      except:
        pass
        """

comp()

