__author__ = 'colinmoore-hill'

from hashlib import md5
from app import gdb


class Player():

    def createPlayer(self, jsonOBJ):
        pass

    def getPlayerList(self):
        pass

    def getPlayerById(self, ref):
        qry = "match ()"
        resp = gdb.cypher.execute( qry )
        pass

    def getPlayerByName(self, name):
        pass

    def getPlayerStock(self):
        pass


class Business():

    def completeSale(self, InvRef):
        pass

