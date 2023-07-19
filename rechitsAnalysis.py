import uproot
import numpy as np
import matplotlib.pyplot as plt
from os import path

np.set_printoptions(threshold=np.inf)

#chambers 0,1,2,3,4,5 are the pad detectors, 6,7, is one TMM and the second TMM is 8,9 
#in local coordinates, vertical and horizontal coordinates are the same. In global frame, horizontal strips have coordinates
#at 90 degrees to coordinates of vertical strips - but this is not important here
#need to do filtering

def analysis(runNumber,eventNumber):
    filename = 'run' + str(runNumber) + 'rechits'
    theFile = '{}.root'.format(filename)
    if path.exists(theFile):
        print("Opening file...")
    else:
        print("File does not exist!")
        return 0
    rootFile = uproot.open('{}.root'.format(filename))
    print('File opened successfully')
    tree = rootFile['rechitTree']

    selectedArray = tree.arrays(['clusterPadCenterX','clusterPadCenterY','rechitCharge','rechitChamber','rechitX'])

    padX = selectedArray.clusterPadCenterX
    padY = selectedArray.clusterPadCenterY
    hitCharge = selectedArray.rechitCharge
    hitChamber = selectedArray.rechitChamber
    stripX = selectedArray.rechitX

    fig, axs = plt.subplots(2,2)
    plt.setp(axs, xlim=(-50,50))
    fig.suptitle('Run {}, Event {}'.format(runNumber, eventNumber))
    axs[0,0].bar(stripX[hitChamber==6][eventNumber],hitCharge[hitChamber==6][eventNumber],color='green')
    axs[0,0].set_title('TMM 1 X')
    axs[0,1].bar(stripX[hitChamber==7][eventNumber],hitCharge[hitChamber==7][eventNumber],color='green')
    axs[0,1].set_title('TMM 1 Y')
    axs[1,0].bar(stripX[hitChamber==8][eventNumber],hitCharge[hitChamber==8][eventNumber],color='green')
    axs[1,0].set_title('TMM 2 X')
    axs[1,1].bar(stripX[hitChamber==9][eventNumber],hitCharge[hitChamber==9][eventNumber],color='green')
    axs[1,1].set_title('TMM 2 Y')

    plt.tight_layout()
    plt.show()

    #fig2, axs2 = plt.subplots(2,3)
    #fig2.suptitle('Run {}, Event {}'.format(runNumber, eventNumber))

def doesFileExist(runNumber,eventNumber):
    if runNumber<0 or eventNumber<0:
        print('Run number or event number out of range (below 0)')
        return 0
    else:
        print('Attempting to open file: run', runNumber, "rechits.root", sep='')    

numberOfRun = int(input('Enter run number: '))
numberOfEvent = int(input('Enter event number: '))
doesFileExist(numberOfRun, numberOfEvent)
analysis(numberOfRun, numberOfEvent)
