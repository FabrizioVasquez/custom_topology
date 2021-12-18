from mininet.node import Controller
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=2):
        switch = self.addSwitch('s1')
        for h in range(n):
            host = self.addHost('h%s' % (h + 1))
            self.addLink(host, switch)

class CustomSwitchTopoPDF(Topo):
    "Switch connected to n hosts."
    def build(self,n = 6):
        switch_home = []
        host_home = []

        # add switch
        
        for i in range(n):
            switch_home.append(self.addSwitch('S%s'%(i+1)))
            
            # add host
            host_home.append(self.addHost('H%s'%(i+1)))
        
        # add the last host
        host_home.append(self.addHost('H%s'%(n+1)))

        self.addLink(switch_home[0], host_home[0])
        self.addLink(switch_home[0], host_home[1])

        self.addLink(switch_home[1], switch_home[3])
        self.addLink(switch_home[1], switch_home[4])
        self.addLink(switch_home[2], switch_home[5])
        self.addLink(switch_home[2], host_home[6])

        self.addLink(switch_home[3],host_home[2])
        self.addLink(switch_home[4],host_home[3])

        self.addLink(switch_home[5],host_home[4])
        self.addLink(host_home[5],switch_home[5])

        print(switch_home,host_home)



def SingleSwitchTopoTest():
    "Create and test a simple network"
    topo = SingleSwitchTopo(n=4)
    net = Mininet(topo)
    net.start()
    #print( "Dumping host connections" )
    #dumpNodeConnections(net.hosts)
    print( "Testing network connectivity" )
    net.pingAll()
    net.stop()

def CustomSwitchTopoPDFTest():
    "Create and test to CustomSwitchTopoPDFTest"
    topo = CustomSwitchTopoPDF(n=6)
    net = Mininet(topo)
    net.start()
    #print( "Dumping host connections" )
    #dumpNodeConnections(net.hosts)
    print( "Testing network connectivity" )
    net.pingAll()
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    SingleSwitchTopoTest()
    CustomSwitchTopoPDFTest()