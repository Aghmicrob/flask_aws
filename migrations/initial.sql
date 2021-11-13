CREATE TABLE "monedero" ( 
	"id"	INTEGER NOT NULL,
	"cryptomoneda"	TEXT NOT NULL,
	"cantidad"	INTEGER NOT NULL,
	PRIMARY KEY("id")
)

CREATE TABLE "registro" (
	"id"	INTEGER,
	"momento"	TEXT NOT NULL,
	"moneda_inicial"	TEXT NOT NULL,
	"moneda_inicial_Q"	INTEGER NOT NULL,
	"moneda_final"	TEXT NOT NULL,
	"moneda_final_Q"	INTEGER NOT NULL,
	"precio_unitario"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
)

INSERT INTO "monedero" ( "cryptomoneda","cantidad" )
	VALUES ("EUR",0), ("BTC",0), ("ETH",0),("XRP",0),("LTC",0),("BCH",0),("BNB",0),("USDT",0),("EOS",0),("BSV",0),("XLM",0),("ADA",0),("TRX",0);