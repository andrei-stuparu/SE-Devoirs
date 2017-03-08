#author Stuparu Andrei 1221F
import sys, threading, logging, os

class Bonjour(threading.Thread):
    def __init__(self, personne):
        threading.Thread.__init__(self)
        self.personne = personne
    def run(self):
        #Fonction polie - saluer une personne
        print "Bonjour %(personne)s!\n" % \
          {"personne":self.personne},
        logging.info("Bonjour : %(personne)s" %{"personne":self.personne})
   
def utilisation():
    #Affichage mode d'utilisation
    mmeThread = []
    mmleThread = []
    mThread = []
    file = open("Liste_Noms.txt", "r")
    for x in file:
                if x[0:2] == "M.":
                    mThread.append(Bonjour(x.strip(' \r\n')))
                elif x[0:3]== "Mme":
                    mmeThread.append(Bonjour(x.strip(' \r\n')))
                else:
                    mmleThread.append(Bonjour(x.strip(' \r\n')))
    for mmle in mmleThread:
            mmle.start()
            mmle.join()
    for mme in mmeThread:
            mme.start()
            mme.join()
    for m in mThread:
            m.start()
            m.join()


         
def main(argv=None):
    working_dir = os.path.dirname(os.path.abspath(__file__)) + os.path.sep
    #Configurez le logging pour ecrire dans un fichier texte
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                        filename = working_dir + 'bonjour.log',
                        level=logging.INFO)    
    logging.info("Main start")
    
    #La boucle principale
    if argv is None:
        argv = sys.argv

    if len(argv) == 1:
        utilisation()
    else:
        #Argument 1 est le nom de fichier avec un noms per ligne
        mmeThread = []
        mmleThread = []
        mThread = []
        with open(working_dir + argv[1],'r') as f:
            #Dites bonjour a chaque personne de fichier
            for ligne in f:
                if ligne[0:2] == "M.":
                    mThread.append(Bonjour(ligne.strip(' \r\n')))
                elif ligne[0:3]== "Mme":
                    mme_local = Bonjour(ligne.strip(' \r\n'))
                    mmeThread.append(mmle_local)
                    mme_local.start()
                else:
                    mmle_local = Bonjour(ligne.strip(' \r\n'))
                    mmleThread.append(mme_local)
                    mmle_local.start()
        for mme in mmeThread:
            mme.start()
            mme.join()
        for m in mThread:
            m.start()
            m.join()
        for mmle in mmleThread:
            mmle.start()
            mmle.join()
    logging.info("Main stop")                
    return 0

if __name__ == "__main__":
    #Simplifiez la logique de la fonction principale
    sys.exit(main())
