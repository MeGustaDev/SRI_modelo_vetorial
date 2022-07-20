import os
import math
import document

class DocumentsCollection:
    name = None
    length = None
    documents_list = []
    vocabulary = []
    dictTermsIDF = {}
    dictDocQueurySimilarity = {} #doc.name, sim

    def __init__(self, name, length, dir_path):
        os.chdir(dir_path)
        self.name = name
        self.length = length

        for file in os.listdir():
            file_name = file
            f = open(file, 'rt')
            content = f.read()
            doc = document.Document(file_name, content)
            #seta o TF dos documentos
            #doc.setDictTF_IDF(self)
            self.documents_list.append(doc)
            

    def setDocCollectionVocabulary(self):
        for doc in self.documents_list:
            self.vocabulary = self.vocabulary + doc.vocabularyList
        self.vocabulary = list(
            dict.fromkeys(self.vocabulary))  #retira duplicatas
        self.vocabulary.sort()  #organiza em ordem alfabetica

    def getTermIDF(self):
        termNi_dict = self.setDictTermsNi()
        for term, ni in termNi_dict.items():
            relativeFreq = self.length / ni
            IDF = math.log2(relativeFreq)
            self.dictTermsIDF.update({term: IDF})

    def setDictTermsNi(self):
        termNi_dict = {}
        for term in self.vocabulary:
            ni = 0
            for doc in self.documents_list:
                if term in doc.vocabularyList:
                    ni = ni + 1
                    termNi_dict.update({term: ni})
        return termNi_dict

    def setDocumentsTF_IDF(self):
        for doc in self.documents_list:
            doc.setDictTF_IDF(self)

    def setDocumentsNormalization(self):
        for doc in self.documents_list:
            doc.setDocumentNormalization()

    def writeVocabularyInFile(self, dir_path, file_name):
        os.chdir(dir_path)
        file = open(file_name, "w")
        for term in self.vocabulary:
            file.write(term + "\n")
        file.close()