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

    selectedArray = tree.arrays(['clusterPadCenterX','clusterPadCenterY','rechitCharge','rechitChamber','rechitX','rechitY'])

    padX = selectedArray.clusterPadCenterX[eventNumber]
    padY = selectedArray.clusterPadCenterY[eventNumber]
    hitCharge = selectedArray.rechitCharge[eventNumber]
    hitChamber = selectedArray.rechitChamber[eventNumber]
    stripX = selectedArray.rechitX[eventNumber]
    stripY = selectedArray.rechitY[eventNumber]

    fig, axs = plt.subplots(2,5,figsize=(25, 6),tight_layout=True)
    fig.suptitle('Run {}, Event {}'.format(runNumber,eventNumber))

    axs[0,0].bar(stripX[hitChamber==6],hitCharge[hitChamber==6],color='green',width=0.5)
    axs[0,0].set_title('TMM 1 X')
    axs[0,1].bar(stripX[hitChamber==7],hitCharge[hitChamber==7],color='green',width=0.5)
    axs[0,1].set_title('TMM 1 Y')
    axs[1,0].bar(stripX[hitChamber==8],hitCharge[hitChamber==8],color='green',width=0.5)
    axs[1,0].set_title('TMM 2 X')
    axs[1,1].bar(stripX[hitChamber==9],hitCharge[hitChamber==9],color='green',width=0.5)
    axs[1,1].set_title('TMM 2 Y')

    axs[0,2].scatter(stripX[hitChamber==0],stripY[hitChamber==0],s=20,c=hitCharge[hitChamber==0],marker='s')
    axs[0,2].set_title('Chamber 0')
    axs[0,3].scatter(stripX[hitChamber==1],stripY[hitChamber==1],s=20,c=hitCharge[hitChamber==1],marker='s')
    axs[0,3].set_title('Chamber 0')
    axs[0,4].scatter(stripX[hitChamber==2],stripY[hitChamber==2],s=20,c=hitCharge[hitChamber==2],marker='s')
    axs[0,4].set_title('Chamber 0')
    axs[1,2].scatter(stripX[hitChamber==3],stripY[hitChamber==3],s=20,c=hitCharge[hitChamber==3],marker='s')
    axs[1,2].set_title('Chamber 0')
    axs[1,3].scatter(stripX[hitChamber==4],stripY[hitChamber==4],s=20,c=hitCharge[hitChamber==4],marker='s')
    axs[1,3].set_title('Chamber 0')
    axs[1,4].scatter(stripX[hitChamber==5],stripY[hitChamber==5],s=20,c=hitCharge[hitChamber==5],marker='s')
    axs[1,4].set_title('Chamber 0')

    plt.show()

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
