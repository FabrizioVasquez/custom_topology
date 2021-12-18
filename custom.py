import pdb
from mininet.topo import Topo

class MyTopo(Topo):
    'Ejemplo de topologia'

    def __init__(self):
        'Creando una nueva topologia'

        Topo.__init__(self)

        S1 = self.addSwitch('S1')
        S2 = self.addSwitch('S2')
        S3 = self.addSwitch('S3')
        S4 = self.addSwitch('S4')
        S5 = self.addSwitch('S5')
        S6 = self.addSwitch('S6')
        H1 = self.addHost('H1')
        H2 = self.addHost('H2')
        H3 = self.addHost('H3')

        switch_list = (S1,S2,S3,S4,S5,S6)

        #add links

        for index in range(len(switch_list)):
            for index2 in range(index+1,len(switch_list)):
                self.addLink(switch_list[index],switch_list[index2])
        
        self.addLink(H1,S1)
        self.addLink(H2,S3)
        self.addLink(H3,S6)
    

topos = {'mytopo': (lambda: MyTopo())}