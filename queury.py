import math
import unidecode
import string 

class Queury:
    content = None
    vocabularyList = []
    termsDict = {}
    TF_IDF_Dict = {}
    normalization = None


    def __init__(self, queury):
        self.content = queury
        termsList = queury.split()
        for term in termsList:
            term = term.lower()
            term = unidecode.unidecode(term)
            term = term.translate(str.maketrans('', '', string.punctuation))
            self.vocabularyList.append(term)
            self.termsDict.update({term: 0.0})

    def getQueuryTF_IDF(self, documentSet):
        TF_dict = self.getQueuryTF()
        IDF_dict = self.getQueuryIDF(documentSet)
        TF_IDF_dict = TF_dict.copy()
        for term, tf in TF_IDF_dict.items():
            TF_IDF = float(tf) * float(IDF_dict.get(term))
            TF_IDF_dict.update({term: TF_IDF})
        self.TF_IDF_Dict = TF_IDF_dict.copy()
        return self.TF_IDF_Dict

    def getQueuryTF(self):
        queuryTermFreqDict = self.termsDict.copy()
        for term in self.vocabularyList:
            termCount = self.vocabularyList.count(term)
            queuryTermFreqDict.update({term: termCount})
        for term, freq in queuryTermFreqDict.items():
            freq = int(freq)
            TF = 1 + math.log2(freq)
            queuryTermFreqDict.update({term: TF})
        return queuryTermFreqDict

    def getQueuryIDF(self, documentsSet):
        queuryIDF_dict = self.termsDict.copy()
        documentsSetTermNi_dict = documentsSet.setDictTermsNi()
        for term in queuryIDF_dict.keys():
            ni = documentsSetTermNi_dict.get(term)
            relativeFreq = documentsSet.length / ni
            IDF = math.log2(relativeFreq)
            queuryIDF_dict.update({term: IDF})
        return queuryIDF_dict

    def setNormalization(self):
        normalization = 0.0
        for tf_idf in self.TF_IDF_Dict.values():
            if tf_idf != 0.0:
                normalization = normalization + (tf_idf * tf_idf)

        normalization = math.sqrt(normalization)
        self.normalization = normalization