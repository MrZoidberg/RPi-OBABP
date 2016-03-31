from mpd import (MPDClient, CommandError)
from socket import error as SocketError
import traceback


class Player(object):

    def __init__(self,):
        self.setPort('6600')
        self.setHost('localhost')
        self.client = MPDClient()

    def setPort(self, _port):
        self.port = _port

    def setHost(self, _host):
        self.host = _host

    def connectMPD(self):
        try:
            con_id = {'host': self.host, 'port': self.port}
            self.client.connect(**con_id)
        except SocketError:
            print "mpd connection error"
            print traceback.print_exc()
            return False

        print self.client.status()
        return True

    def disconnect(self):
        try:
            self.client.disconnect()
        except SocketError:
            print "mpd connection error"
            print traceback.print_exc()

    def getState(self):
        try:
            return self.client.status()["state"]
        except SocketError:
            print "mpd connection error"
            print traceback.print_exc()

    def getPlaylistinfo(self):
        try:
            return self.client.playlistinfo()
        except SocketError:
            print "mpd connection error"
            print traceback.print_exc()
