import math
import vocabularyPreProcessing

class Document:
    name = ""
    content = ""
    documentVocabulary = []
    dictTermFreq = {}
    dictTF_IDF = {}
    documentNormalization = None

    def __init__(self, name, content):
        self.name = name
        self.content = content

        basicVocabulary = self.content.split()
        formatedVocabulary = []
        for term in basicVocabulary:
            formatedTerm = vocabularyPreProcessing.termFormater(term)
            formatedVocabulary.append(formatedTerm)
        self.vocabularyList = formatedVocabulary
    
    def setDictTF_IDF(self, collection):
        self.dictTF_IDF = self.getDocumentTF(collection)
        collection.setDictTermsNi()
        collection.getTermIDF()
        dictTermIDF = collection.dictTermsIDF.copy()

        for term, tf in self.dictTF_IDF.items():
            TF_IDF = float(tf) * float(dictTermIDF.get(term))
            self.dictTF_IDF.update({term: TF_IDF})

    def getDocumentTF(self, collection):
        TFdict = {}
        for term in collection.vocabulary:
            termCount = self.vocabularyList.count(term)
            if termCount != 0:
                TF = 1 + math.log2(termCount)
                TFdict.update({term: TF})
        return TFdict

    def setDocumentNormalization(self):
        normalization = 0.0
        for TF_IDF in self.dictTF_IDF.values():
            normalization = normalization + (TF_IDF * TF_IDF)
        normalization = math.sqrt(normalization)
        self.documentNormalization = normalization