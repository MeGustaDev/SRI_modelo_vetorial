import math
import vocabularyPreProcessing

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
            formatedTerm = vocabularyPreProcessing.termFormater(term)
            self.vocabularyList.append(formatedTerm)
            self.termsDict.update({formatedTerm: 0.0})

    def setQueuryTF_IDF(self, documentSet):
        TF_dict = self.getQueuryTF()
        IDF_dict = self.getQueuryIDF(documentSet)

        for term, tf in TF_dict.items():
            TF_IDF = float(tf) * float(IDF_dict.get(term))
            self.TF_IDF_Dict.update({term: TF_IDF})

    def getQueuryTF(self):
        queuryTermFreqDict = {}
        for term in self.vocabularyList:
            termCount = self.vocabularyList.count(term)
            queuryTermFreqDict.update({term: termCount})
        for term, freq in queuryTermFreqDict.items():
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